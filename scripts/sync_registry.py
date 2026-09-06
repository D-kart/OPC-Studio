#!/usr/bin/env python3
"""OPC-Studio skill 生态同步与渲染脚本。

流程：
  1. 从 GitHub API 抓取各 skill 仓库的 latest release / star / fork
  2. 更新 registry.json（唯一事实来源）
  3. 由 registry.json 渲染 README.md 的矩阵表与生态状态表（标记区块内）

用法：
  python3 scripts/sync_registry.py               # 抓取 + 更新 + 渲染
  python3 scripts/sync_registry.py --render-only # 只用本地 registry 渲染 README
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry.json"
README = ROOT / "README.md"

MARK = "OPC-STUDIO:AUTO"
START = f"<!-- {MARK}:"
END = f"<!-- {MARK}:END -->"


def gh_api(path: str) -> dict | None:
    """调用 GitHub API。优先 GITHUB_TOKEN，否则匿名（60 req/h）。"""
    url = f"https://api.github.com/{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except Exception as e:  # 网络/限流失败不阻断渲染
        print(f"[warn] {url}: {e}", file=sys.stderr)
        return None


def fetch_skill_facts(skills: list[dict]) -> None:
    """把远端 release / star / fork 写回 registry。"""
    for s in skills:
        repo = s.get("repo")
        if not repo or s.get("status") != "released":
            continue
        rel = gh_api(f"repos/{repo}/releases/latest")
        if rel and rel.get("tag_name") and re.match(r"^v?\d+\.\d+\.\d+$", rel["tag_name"]):
            tag = rel["tag_name"]
            if not tag.startswith("v"):
                tag = "v" + tag
            if s.get("version") != tag:
                print(f"[version] {s['name']}: {s.get('version')} -> {tag}")
            s["version"] = tag
            if rel.get("published_at"):
                s["released_at"] = rel["published_at"][:10]
        detail = gh_api(f"repos/{repo}")
        if detail:
            s["star"] = detail.get("stargazers_count", 0)
            s["fork"] = detail.get("forks_count", 0)
    reg["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ---------- 渲染 ----------

def esc(t: str) -> str:
    return t.replace("|", "\\|")


def matrix_table(skills: list[dict], layer: str) -> str:
    rows = []
    for s in skills:
        if s["layer"] != layer:
            continue
        if s.get("repo"):
            name = s["emoji"] + f" **[{s['name']}](https://github.com/{s['repo']})**"
            install = f"`{s['install']}`" if s.get("install") else "—"
        else:
            name = s["emoji"] + " **" + s["name"] + "**"
            install = "—"
        status = f"✅ {s['version']} 已发布" if s["status"] == "released" else "🚧 研发中"
        rows.append(
            f"| {name} | {esc(s['cn'])} | {esc(s['theme'])} | {status} | {install} |"
        )
    head = "| Skill | 中文名 | 主题 | 状态 | 一行安装 |\n|---|---|---|---|---|"
    return head + "\n" + "\n".join(rows)


def render_matrix(skills: list[dict]) -> str:
    parts = [
        "> 按职能分层归类：**投资与投研层**（主理人专业主线 · 服务投资经理 / 投研 / 融资）· **OPC 创业运营层**（武装一人公司 · 从验证到放大）· **视觉风格与内容设计层**（跨线共享的表现层）。",
        "",
        "#### 🏦 投资与投研层",
        "",
        matrix_table(skills, "business"),
        "",
        "#### 🚀 OPC 创业运营层",
        "",
        matrix_table(skills, "opc"),
        "",
        "#### 🎨 视觉风格与内容设计层",
        "",
        matrix_table(skills, "visual"),
    ]
    return "\n".join(parts)


def render_eco_stats(skills: list[dict]) -> str:
    released = [s for s in skills if s["status"] == "released"]
    wip = [s for s in skills if s["status"] == "wip"]
    with_version = [s for s in released if s.get("version")]

    recent = sorted(
        [s for s in with_version if s.get("released_at")],
        key=lambda s: s["released_at"],
        reverse=True,
    )[:4]
    if not recent:
        recent = with_version[-4:]
    recent_line = " · ".join(f"**{s['name']} {s['version']}**" for s in recent)

    flagship = next((s for s in skills if s.get("flagship")), None)
    fl_line = ""
    if flagship:
        star = flagship.get("star")
        star_txt = f" · ⭐ {star}" if star else ""
        fl_line = f"**{flagship['name']}**（{star_txt[3:] if star_txt else '定性研判范式'}）"

    starred = sorted(
        [s for s in released if s.get("star")], key=lambda s: s["star"], reverse=True
    )[:3]
    if starred and starred[0].get("star", 0) > 0:
        heat_line = " · ".join(f"{s['name']}（⭐{s['star']}）" for s in starred)
    else:
        heat_line = "暂无公开信号，装量数据以 skills.sh 为准"

    n_total, n_rel, n_wip = len(skills), len(released), len(wip)
    if n_wip == 0:
        repo_line = f"| Skill 仓库 | **{n_total}** 个（全部已发布）|"
    else:
        repo_line = f"| Skill 仓库 | **{n_total}** 个（{n_rel} 已发布 + {n_wip} 研发中）|"
    lines = [
        "| 指标 | 数值 |",
        "|---|---|",
        repo_line,
        f"| 最近发布 | {recent_line} |",
        f"| 旗舰 skill | {fl_line} |",
        f"| 需求侧热度 | {heat_line} |",
        "| 状态同步 | 每日自动同步（`.github/workflows/sync-matrix.yml`）|",
    ]
    return "\n".join(lines)


def replace_block(content: str, block: str, new: str) -> str:
    start_full = f"{START}{block} -->"
    pat = re.compile(
        rf"({re.escape(start_full)})(.*?)(\n{re.escape(END)})",
        re.DOTALL,
    )
    if not pat.search(content):
        raise SystemExit(f"README 缺少标记区块 {START}{block} --> — 请先手工插入")
    return pat.sub(lambda m: m.group(1) + "\n" + new + m.group(3), content)


def render() -> None:
    skills = reg["skills"]
    content = README.read_text(encoding="utf-8")
    content = replace_block(content, "ECO_STATS", render_eco_stats(skills))
    content = replace_block(content, "MATRIX", render_matrix(skills))
    README.write_text(content, encoding="utf-8")
    print("[render] README.md updated")


if __name__ == "__main__":
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if "--render-only" not in sys.argv:
        fetch_skill_facts(reg["skills"])
        REGISTRY.write_text(
            json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print("[fetch] registry.json updated")
    render()
