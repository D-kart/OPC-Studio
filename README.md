# OPC-Studio

> 看见每一个一人公司。  
> **One Person Company Studio powered by AI Agents.**

OPC-Studio 是一个面向 **OPC（One Person Company，一人公司）创业者** 的 AI 原生内容与服务平台。我们用「一个人 + 一组 AI Agent」的方式，记录、拆解、放大一人公司的真实创业过程，并逐步沉淀为服务 OPC 生态的工具与网络。

本项目为 **2026 WAIC FutureTech OPC 独立先锋挑战赛** 参赛 Demo。

---

## 项目愿景

AI 正在让个体创业者第一次拥有接近小团队甚至中型团队的生产力。

过去，一个创业者需要同时承担产品、内容、运营、销售、数据分析、客户沟通等大量工作；今天，AI Agent 可以成为独立创业者背后的「第二团队」。

OPC-Studio 想做的事情很简单：

> **让更多一人公司被看见、被理解、被连接。**

我们自己也以 OPC 的方式运行：一位主理人，协同 12 个 AI Agent，完成从内容生产、项目拆解、传播分发到需求匹配的全流程。

---

## Demo 亮点

当前 Demo 是一个轻量级单页应用，包含两个核心部分：

### 1. OPC-Studio Landing Page

用于展示项目定位、核心理念和商业模式：

- 「一人 + AI」的新型创业组织形态
- PitchRoom 结构化 7 问
- 12 个 AI Agent 的「一人军团作战室」
- OPC Toolkit + OPC Network 的增长飞轮

### 2. AI 拆机器

一个面向 OPC 创业者的互动体验：

用户输入自己的项目、AI 使用方式和未来目标后，系统会模拟完成一次「一人公司拆机」，并生成一张结构化评级卡。

评级维度包括：

- **引擎 Engine**：AI 是否真正进入核心流程
- **杠杆 Lever**：一个人是否能放大成多人的产能
- **韧性 Grit**：项目是否具备长期迭代能力
- **势能 Momentum**：当前增长信号是否清晰
- **愿力 Vision**：未来 12 个月目标是否明确

---

## PitchRoom：结构化 7 问

PitchRoom 不是传统访谈，也不是路演秀，而是一次对一人公司的结构化拆解。

我们把每个 OPC 看作一台正在运转的机器，通过 7 个问题理解它的内部结构：

| 问题 | 核心提问 |
|---|---|
| 拆壳 | 你的一人公司从外面看是什么？从里面看呢？ |
| 引擎 | AI 在你这里扮演什么角色？助手、合伙人，还是替身？ |
| 仪表盘 | 你每天盯着哪个数字？它现在是多少？ |
| 黑匣子 | 走到今天，哪个弯路差点让你死掉？ |
| 涡轮 | 如果给你 10 倍的用户，你的系统撑得住吗？ |
| 后视镜 | 回到起点，你会跳过什么、加速什么？ |
| 导航 | 12 个月后，你希望自己是什么样子？ |

这套 7 问既是内容框架，也是未来 OPC 项目分析、工具推荐和需求匹配的基础协议。

---

## 产品形态

OPC-Studio 将分为三个层次逐步发展：

### Phase 1：OPC Toolkit

将 OPC-Studio 自己验证过的 AI 工作流产品化，帮助更多一人公司创业者搭建自己的 AI 工作系统。

典型能力包括：

- 项目拆解
- 内容生成
- 选题规划
- 多平台分发
- 客户沟通
- 数据复盘

### Phase 2：OPC Network

当足够多的一人公司被结构化记录后，OPC-Studio 将成为一个高质量 OPC 项目网络。

一边是希望找到靠谱独立服务者的企业与机构，另一边是需要优质客户和合作机会的一人公司创业者。OPC-Studio 负责做可信匹配。

### Phase 3：品牌生态

当 OPC-Studio 成为 OPC 生态的内容入口后，将叠加品牌赞助、工具联名、生态合作等收入模式，形成内容、工具、网络之间的增长飞轮。

---

## 技术栈

当前 Demo 为纯前端实现：

- HTML
- CSS
- Vanilla JavaScript
- 响应式移动端适配
- 无后端依赖，可直接部署到 GitHub Pages / Vercel / Netlify

> 注：当前版本中的 AI 分析为前端模拟逻辑，用于展示产品交互原型。后续版本将接入真实 LLM API，实现更准确的项目拆解与个性化建议。

---

## 本地运行

直接打开 `index.html` 即可预览：

```bash
open index.html
```

或使用任意静态服务器：

```bash
python3 -m http.server 8080
```

然后访问：

```text
http://localhost:8080
```

---

## 项目结构

```text
opc-studio-demo/
├── index.html   # Demo 单页应用
└── README.md    # 项目说明文档
```

---

## 路线图

- [x] 完成 Landing Page 原型
- [x] 完成 AI 拆机器交互 Demo
- [x] 完成移动端适配
- [ ] 接入真实 LLM API
- [ ] 生成可下载/分享的评级卡图片
- [ ] 增加 OPC 项目投递入口
- [ ] 搭建 OPC Toolkit 的 Agent 模板库
- [ ] 建立 OPC Network 的项目/需求匹配机制

---

## 参赛信息

- **赛事**：2026 WAIC FutureTech OPC 独立先锋挑战赛
- **赛道**：创业赛道
- **项目名称**：OPC-Studio
- **项目口号**：看见每一个一人公司
- **项目形态**：AI 原生内容平台 + OPC 工具服务 + 项目网络

---

## 关于 OPC-Studio 主理人

OPC-Studio 由一位独立创业者发起。

我们相信，未来会出现越来越多由 AI Agent 放大的「一人公司」。这些公司也许规模不大，但足够灵活、专业、真实，并且能够在垂直场景中创造高密度价值。

OPC-Studio 希望成为这个新生态最早的记录者、连接者和基础设施建设者。

---

## License

This project is currently for competition demo and concept validation.  
All rights reserved.
