# OPC-Studio

![made by](https://img.shields.io/badge/made%20by-OPC--Studio-1a1a4e) ![license](https://img.shields.io/badge/license-MIT-green) ![compat](https://img.shields.io/badge/compat-Claude%20%7C%20WorkBuddy%20%7C%20OpenClaw%20%7C%20Hermes%20%7C%20SkillHub-orange) ![skill repos](https://img.shields.io/badge/skill%20repos-17-blue) ![last commit](https://img.shields.io/github/last-commit/D-kart/OPC-Studio?style=flat-square) ![stars](https://img.shields.io/github/stars/D-kart/OPC-Studio?style=flat-square)

> 看见每一个一人公司。
> **The AI-native showcase, workflow, and opportunity network for One Person Companies.**

OPC-Studio 服务 **一人公司（One Person Company）** 生态——一个 AI 原生平台，让优秀的独立创业者被看见，也让客户、投资人和生态伙伴更高效地找到彼此。

---

## 🛠️ AI Skill 工坊

OPC-Studio 同时维护一套**专业 AI Skill**：把投资投研、创业运营、视觉设计里的高价值工作流，做成一键安装的「技能包」，直接装进你的 AI Agent。

每个 Skill 独立成仓、开箱即用，兼容 Claude / WorkBuddy / OpenClaw / Hermes / SkillHub 五大平台。

> 新增或更新 Skill：在 `registry.json` 加一条即可，下方矩阵与生态状态由脚本自动渲染，无需手改本页。

---

## 📊 生态实时状态

<!-- OPC-STUDIO:AUTO:ECO_STATS -->
| 指标 | 数值 |
|---|---|
| Skill 仓库 | **17** 个（全部已发布）|
| 最近发布 | **validate-skill v1.0.0** · **build-skill v1.0.0** · **growth-skill v1.0.0** · **price-skill v1.0.0** |
| 旗舰 skill | **investor-skill**（⭐ 8） |
| 需求侧热度 | investor-skill（⭐8） · presenter-skill（⭐1） |
| 状态同步 | 每日自动同步（`.github/workflows/sync-matrix.yml`）|
<!-- OPC-STUDIO:AUTO:END -->

**近期更新：**

- **OPC 创业运营层 7 连发** — 覆盖一人公司「验证 → 构建 → 获客 → 定价 → 放大 → 复盘 → 被 AI 看见」完整生命周期
- **investor-skill v1.0.3** — 定性研判范式升级，以事实证据取代打分

---

## 🧩 Skill 矩阵

<!-- OPC-STUDIO:AUTO:MATRIX -->
> 按职能分层归类：**投资与投研层**（主理人专业主线 · 服务投资经理 / 投研 / 融资）· **OPC 创业运营层**（武装一人公司 · 从验证到放大）· **视觉风格与内容设计层**（跨线共享的表现层）。

#### 🏦 投资与投研层

| Skill | 中文名 | 主题 | 状态 | 一行安装 |
|---|---|---|---|---|
| 🧭 **[investor-skill](https://github.com/D-kart/investor-skill)** | 投资人.skill | 一级市场职业投资人工作流（行研 / 尽调 / BP 速析 / 竞争格局 / 技术产品 / 投资备忘录） | ✅ v1.0.3 已发布 | `npx skills add D-kart/investor-skill` |
| 🎤 **[presenter-skill](https://github.com/D-kart/presenter-skill)** | 路演者.skill | 创始人融资路演工作流（叙事打磨 / 市场机会结构化 / 产品数据通俗化 / 护城河论证 / Q&A 异议 / 估值退出） | ✅ v1.0.1 已发布 | `npx skills add D-kart/presenter-skill` |
| 📝 **[summary-skill](https://github.com/D-kart/summary-skill)** | 纪要官.skill | 投资经理访谈纪要官（关键事实抽取 / 主题归并 / 三档时间戳 / 5 大类 20 小项覆盖核查 / 待确认问题清单 / Markdown + docx 双格式） | ✅ v2.0.3 已发布 | `npx skills add D-kart/summary-skill` |
| 📊 **[ma-pitch-skill](https://github.com/D-kart/ma-pitch-skill)** | 并购pitch.skill | M&A 并购标的推介书（年报数据提取 / 多年财务分析 / 买方战略匹配矩阵 / 可比交易分析 / 风险矩阵 / 整合路线图 / 16:9 宽幅 HTML 输出） | ✅ v1.0.0 已发布 | `npx skills add D-kart/ma-pitch-skill` |

#### 🚀 OPC 创业运营层

| Skill | 中文名 | 主题 | 状态 | 一行安装 |
|---|---|---|---|---|
| 🧪 **[validate-skill](https://github.com/D-kart/validate-skill)** | 验证官.skill | 7 步验证法——用投资人视角帮 OPC 创业者判断「这个想法值不值得做」（问题 / 方案 / 市场 / 竞争 / 能力 / 经济 / 风险七关），输出 GO / NO-GO / PIVOT + 关键证据 | ✅ v1.0.0 已发布 | `npx skills add D-kart/validate-skill` |
| 🏗️ **[build-skill](https://github.com/D-kart/build-skill)** | 建造师.skill | 构建流水线——把验证通过的想法直接构建成能用的 MVP 产物（识别产品类型 / 初始化产物目录 / 逐步产出 / 交付），不交报告交产物 | ✅ v1.0.0 已发布 | `npx skills add D-kart/build-skill` |
| 🌱 **[growth-skill](https://github.com/D-kart/growth-skill)** | 获客官.skill | 冷启动 5 步法——不靠烧钱，从 0 找到第一个付费客户再滚出增长飞轮（ICP 定位 / 渠道选择 / 冷启动动作 / 首次转化 / 飞轮设计） | ✅ v1.0.0 已发布 | `npx skills add D-kart/growth-skill` |
| 💰 **[price-skill](https://github.com/D-kart/price-skill)** | 定价官.skill | 定价 5 步法——把「值多少」变成「收多少」（定价模式 / 价值锚点 / 三档定价 / 收钱话术 / 价格测试） | ✅ v1.0.0 已发布 | `npx skills add D-kart/price-skill` |
| 🤖 **[automate-skill](https://github.com/D-kart/automate-skill)** | 自动化官.skill | 自动化 5 步法——把重复劳动交给 AI 和脚本，一个人放大到一支团队的产能（识别自动化点 / 选方式 / 搭建 / 跑起来 / 迭代） | ✅ v1.0.0 已发布 | `npx skills add D-kart/automate-skill` |
| 🔁 **[retrospect-skill](https://github.com/D-kart/retrospect-skill)** | 复盘官.skill | 复盘 5 步法——把每次经历沉淀成下次能直接用的资产（回顾事实 / 找差距 / 挖原因 / 沉淀资产 / 归档进化） | ✅ v1.0.0 已发布 | `npx skills add D-kart/retrospect-skill` |
| 🧲 **[opc-geo-skill](https://github.com/D-kart/opc-geo-skill)** | GEO官.skill | GEO 6 步法——让内容成为 AI 回答「一人公司」问题时被引用的来源（问题地图 / 引用归因 / 内容差距 / 可引用改造 / 技术落地 / 验证闭环） | ✅ v1.0.0 已发布 | `npx skills add D-kart/opc-geo-skill` |

#### 🎨 视觉风格与内容设计层

| Skill | 中文名 | 主题 | 状态 | 一行安装 |
|---|---|---|---|---|
| 📰 **[gazette-skill](https://github.com/D-kart/gazette-skill)** | 公报.skill | 古典公报/金融大报网站设计风格（FT / Economist / Monocle / WSJ 数字版 HTML · 衬线字体 · 黑白单色 · 报头元素 · drop cap · 中英双语重建规则 · 长文档侧边栏导航 + 锚点跳转滚动高亮） | ✅ v1.1.0 已发布 | `npx skills add D-kart/gazette-skill` |
| 🐼 **[panda-skill](https://github.com/D-kart/panda-skill)** | 熊猫.skill | 双色 SaaS 落地页风格（白底为主 + 黑色反色锚点 · 阿里普惠体 + Barlow + Dream + 故障黑 · toB 量化 / AI Agent 平台 / Dashboard · 5 步闭环 · 4 档套餐 · Combo + VS 对比 · 11 区块落地页架构） | ✅ v1.0.0 已发布 | `npx skills add D-kart/panda-skill` |
| 🌌 **[nocturne-skill](https://github.com/D-kart/nocturne-skill)** | 深空.skill | 深空终端暗色科技风（复刻 getspine.ai / Spine Swarm · 真·深空黑底 #0a0a0a 主态 + 琥珀金唯一强调 + 全视口光晕环 + 星尘粒子 + JetBrains Mono 终端标签 · 羊皮纸暖亮态孪生 · Outfit + JetBrains Mono · copyweb 首个端到端产物） | ✅ v1.0.0 已发布 | `npx skills add D-kart/nocturne-skill` |
| 🎓 **ai-investment-course-skill** | AI投研课.skill | 「AI 增强投资」培训课程设计体系（4 模块 / 20 门课 / 690 分钟 · 募投管退全流程 + 政府招商/基金管理等探索课题 · 每课五段式详情含可复制 prompt · gazette 风格课程表 HTML 模板含 SPA 详情系统 · 海报文案规范 · 与 gazette-skill 协同：内容层 + 视觉层） | ✅ v1.0.0 已发布 | — |
| 🏭 **[copyweb-skill](https://github.com/D-kart/copyweb-skill)** | 扒站.skill | 视觉风格 skill 工厂（元 skill）：输入参考站 URL 输出符合规范的风格 skill 包 · 六阶段（命名去重 / 双通道扒站采集 / 风格分析防翻车 / 提炼 / 三层封装 / 发布）· 固化 gazette+panda 复刻经验与「变量定义≠实际使用」血泪教训 · 产出即可入矩阵 | ✅ v1.0.0 已发布 | `npx skills add D-kart/copyweb-skill` |
| 📐 **[helvet-skill](https://github.com/D-kart/helvet-skill)** | 瑞士风.skill | Swiss 国际主义排版单文件信息图工作流（纯白底 + 纯黑字 + 瑞士红唯一强调 · 规则线四级分隔 + 五级字阶 · 8 类内联 SVG 图表配方坐标先算后写防溢出 · 涨红跌绿 A 股惯例 · 原文引用 vs 检索补充双轨数据核查 · 零外链单文件 HTML 离线可开） | ✅ v1.0.0 已发布 | `npx skills add D-kart/helvet-skill` |
<!-- OPC-STUDIO:AUTO:END -->

---

## 🖼️ 工坊作品

工坊不止写 Skill，还用它们做出了这些成果（按时间倒序）：

| # | 作品 | 时间 | 用到的 Skill | 链接 |
|---|---|---|---|---|
| #002 | 一级市场资源集中信息图 | 2026-08 | helvet-skill | [showcase/2026-08-primary-market-concentration/](./showcase/2026-08-primary-market-concentration/) |
| #001 | AI 赋能全流程投研实战 · 课程表 | 2026-08 | ai-investment-course-skill + gazette-skill | [showcase/2026-08-ai-investment-course/](./showcase/2026-08-ai-investment-course/) |

---

## 关于

OPC-Studio 由一位前职业投资人发起，现在是一家 AI 原生的一人公司。我们相信，未来会出现越来越多被 AI Agent 放大的一人公司——团队很小，却能在垂直场景里创造高密度价值。

我们保持「专业、克制、真实、有审美、有判断」。

OPC-Studio 想做这个新生态的记录者、展示者和连接者。

---

## License

This project is currently for concept validation and ecosystem building.
All rights reserved.
