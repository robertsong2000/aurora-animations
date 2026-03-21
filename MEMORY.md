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

## 🛠️ 已安装的 Skills

| Skill | 用途 | 安装日期 |
|-------|------|----------|
| tencent-finance-stock-price | A股/港股/美股实时行情查询 | 2026-03-18 |
| investment-analyst | 投资分析框架 | 2026-03-18 |
| agent-knowledge | 知识库管理 | 2026-03-18 |
| agent-browser-core | 浏览器自动化 CLI（基于Rust） | 2026-03-18 |

---

## 📝 重要事件

### 2026-03-18
- 完成中国铝业 (601600) 深度分析报告
- 报告已保存到知识库：`~/.soulshare/agent/knowledge/research/china-aluminum-analysis-20260318.md`
- 安装了 ripgrep 和 fzf 增强知识库搜索能力
