# MEMORY.md - 长期记忆

> 小罗的持久化记忆，记录重要的上下文、偏好和知识索引。

---

## 👤 关于 Robert

- **名字**：Robert
- **时区**：Asia/Shanghai (GMT+8)
- **第一个和我对话的人类**

### 📁 项目管理规则

- **Workspace (`~/.openclaw/workspace/`)**：仅保留 Agent 配置文件，不放代码项目
- **代码项目 (`~/projects/`)**：所有代码项目、Git 仓库都放这里
  - `~/projects/html-samples/` - HTML 动画项目（209个文件）

---

## 📚 知识库整合方案

### 两套记忆系统

| 系统 | 位置 | 用途 | 搜索方式 |
|------|------|------|----------|
| **OpenClaw 记忆** | `~/.openclaw/workspace/memory/` | 每日日志、会话上下文 | `memory_search` (语义) |
| **agent-knowledge** | `~/.soulshare/agent/knowledge/` | URL、文章、视频、研究成果 | `rg` / `fzf` (文本) |

### 使用场景

**存入 OpenClaw 记忆 (memory/YYYY-MM-DD.md)**：
- 每日工作记录
- 重要决定和事件
- 临时笔记和想法
- 需要语义搜索的内容

**存入 agent-knowledge**：
- 网页 URL 收藏
- 视频/文章/论文摘要
- 社交媒体内容
- 深度研究报告
- 需要长期保存的结构化知识

### 快速搜索命令

```bash
# 统一搜索（同时搜索两个知识库）
~/.openclaw/workspace/scripts/search-knowledge.sh "关键词"

# 单独搜索 OpenClaw 记忆（语义搜索）
# 直接说：帮我搜索记忆中的"关键词"

# 单独搜索 agent-knowledge（文本搜索）
rg "关键词" ~/.soulshare/agent/knowledge/

# 模糊搜索文件
find ~/.soulshare/agent/knowledge -type f -name "*.md" | fzf
```

### 🤖 智能搜索规则

当用户问以下问题时，我会同时搜索两个知识库：
- "帮我搜索/查找/找一下..."
- "我们之前讨论过..."
- "我记得保存过..."
- "知识库里有...吗？"

---

## 🧠 记忆系统架构（2026-03-21 更新）

### 三层记忆架构

| 类型 | 位置 | 用途 | 示例 |
|------|------|------|------|
| **Episodic** | `memory/episodic/` | 每日事件日志 | `2026-03-21.md` |
| **Semantic** | `memory/semantic/` | 知识库/事实 | `geopolitics-analysis.md` |
| **Procedural** | `memory/procedural/` | 工作流/流程 | `geopolitics-monitoring-workflow.md` |

### 核心功能

- **压缩检测** - 防止上下文丢失
- **自动快照** - 保存重要上下文
- **语义搜索** - 检索历史记忆
- **统计监控** - 追踪使用模式
- **判断修正** - 记录错误，避免重复（案例1：伊朗政权韧性，案例2：忽略霍尔木兹海峡，案例3：不要"八面玲珑"）

### 记忆索引

**快速查找**：[memory/INDEX.md](memory/INDEX.md)

### 现实主义核心公理

**第一公理：人性不变**
> **历史会重演，因为人性不变。**

**第二公理：权力至上**
> **权力、恐惧、利益** - 修昔底德

**第三公理：明确判断，敢于犯错** ⭐️ 新增
> **现实主义不是"八面玲珑"，而是"明确判断，敢于犯错"。**
> **"宁愿犯错，不愿模糊"。**

### 使用方式

```bash
# 检查压缩风险
~/.openclaw/workspace/skills/memory-manager/detect.sh

# 整理记忆
~/.openclaw/workspace/skills/memory-manager/organize.sh

# 搜索记忆
~/.openclaw/workspace/skills/memory-manager/search.sh episodic "关键词"

# 查看统计
~/.openclaw/workspace/skills/memory-manager/stats.sh
```

### 当前状态（2026-03-21）

```
📅 Episodic: 12 files, 116K
🧠 Semantic: 3 files, 16K  ← 新增 judgment-corrections.md
⚙️  Procedural: 3 files, 24K
💾 Total: 18 files, 196K
✅ Health: 11% usage (Safe)
```

### 知识库快速索引

| 知识领域 | 文件 | 核心内容 |
|---------|------|----------|
| **地缘政治** | `semantic/geopolitics-analysis.md` | 现实主义框架、伊朗战争、台海窗口期 |
| **学习记录** | `semantic/judgment-corrections.md` | ✨ 判断错误案例、修正过程、核心教训 |
| **监控流程** | `procedural/geopolitics-monitoring-workflow.md` | 每日监控、判断修正流程 |
| **飞书工作流** | `procedural/feishu-document-workflow.md` | 文档创建、更新、验证 |

---

## 🛠️ 已安装的 Skills

| Skill | 用途 | 安装日期 |
|-------|------|----------|
| tencent-finance-stock-price | A股/港股/美股实时行情查询 | 2026-03-18 |
| investment-analyst | 投资分析框架 | 2026-03-18 |
| agent-knowledge | 知识库管理 | 2026-03-18 |
| agent-browser-core | 浏览器自动化 CLI（基于Rust） | 2026-03-18 |
| **memory-manager** | **三层记忆管理系统** | **2026-03-21** |
| video-prompt-generator | Seedance 视频提示词生成 | 2026-03-21 |

---

## 🧠 记忆系统架构（2026-03-21 更新）

### 三层记忆架构

| 类型 | 位置 | 用途 | 示例 |
|------|------|------|------|
| **Episodic** | `memory/episodic/` | 每日事件日志 | `2026-03-21.md` |
| **Semantic** | `memory/semantic/` | 知识库/事实 | `moltbook.md` |
| **Procedural** | `memory/procedural/` | 工作流/流程 | `skill-launch.md` |

### 核心功能

- **压缩检测** - 防止上下文丢失
- **自动快照** - 保存重要上下文
- **语义搜索** - 检索历史记忆
- **统计监控** - 追踪使用模式

### 使用方式

```bash
# 检查压缩风险
~/.openclaw/workspace/skills/memory-manager/detect.sh

# 整理记忆
~/.openclaw/workspace/skills/memory-manager/organize.sh

# 搜索记忆
~/.openclaw/workspace/skills/memory-manager/search.sh episodic "关键词"

# 查看统计
~/.openclaw/workspace/skills/memory-manager/stats.sh
```

### 当前状态（2026-03-21）

```
📅 Episodic: 11 files, 112K
🧠 Semantic: 1 file, 8K
⚙️  Procedural: 1 file, 8K
💾 Total: 13 files, 160K
✅ Health: 10% usage (Safe)
```

---

## 📝 重要事件

### 2026-03-18
- 完成中国铝业 (601600) 深度分析报告
- 报告已保存到知识库：`~/.soulshare/agent/knowledge/research/china-aluminum-analysis-20260318.md`
- 安装了 ripgrep 和 fzf 增强知识库搜索能力

---

## 🎯 现实主义判断原则

### 第三公理：明确判断，敢于犯错

> **现实主义不是"八面玲珑"，而是"明确判断，敢于犯错"。**
> **"宁愿犯错，不愿模糊"。**
> - Robert（2026-03-21）

**核心原则**：
1. ✅ **不要"八面玲珑"** - 给出唯一判断，不是多场景概率
2. ✅ **敢于犯错** - 不要给自己留"安全空间"
3. ✅ **通过复盘修正** - 错了就承认，分析原因，修正判断
4. ✅ **基于必然，不是概率** - 基于历史规律，给出"必然"

**详细文档**：
- memory/semantic/core-realism-principles.md（第三公理）
- memory/semantic/judgment-corrections.md（案例3）

