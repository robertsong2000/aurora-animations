# 飞书文档工作流

## ⚠️ 重要教训（2026-03-23）

**问题**：`feishu_doc action=create` 创建的文档是空的！

**根本原因**：
- ❌ `create` 只创建空白文档
- ❌ `content` 参数在 `create` 中无效
- ✅ 必须在 `create` 后立即调用 `write`

**正确流程**：
```bash
# 1. 创建文档
feishu_doc action=create title="标题"

# 2. 写入内容（必须！）
feishu_doc action=write doc_token=XXX content="内容"

# 3. 验证内容（必须！）
feishu_doc action=read doc_token=XXX
```

**验证标准**：
- ✅ `block_count > 1`（至少有内容块）
- ✅ `read` 返回的内容不为空

---

## 📝 文档创建流程

### ⚠️ 重要：必须三步走

**错误方式**：
```bash
# ❌ 错误：create 后内容不会自动写入
feishu_doc action=create title="标题" content="内容"
```

**正确方式**：
```bash
# ✅ 正确：三步走
# 1. 创建文档
feishu_doc action=create title="标题"

# 2. 写入内容
feishu_doc action=write doc_token=XXX content="内容"

# 3. 验证内容
feishu_doc action=read doc_token=XXX
```

---

## 🔧 完整工作流

### 1. 创建新文档

```bash
# 创建文档
feishu_doc action=create title="文档标题"

# 记录返回的 doc_token
# 示例输出：
# {
#   "document_id": "V3budzEa6oJvZTxzaoYcyedbnAc",
#   "url": "https://feishu.cn/docx/V3budzEa6oJvZTxzaoYcyedbnAc"
# }
```

### 2. 写入内容

```bash
# 写入完整内容（会替换所有内容）
feishu_doc action=write doc_token=V3budzEa6oJvZTxzaoYcyedbnAc content="# 标题

内容..."

# 追加内容（在文档末尾添加）
feishu_doc action=append doc_token=V3budzEa6oJvZTxzaoYcyedbnAc content="

## 新章节

更多内容..."
```

### 3. 验证内容

```bash
# 读取文档内容
feishu_doc action=read doc_token=V3budzEa6oJvZTxzaoYcyedbnAc

# 检查输出是否包含预期内容
# 示例输出：
# {
#   "title": "文档标题",
#   "content": "完整内容...",
#   "block_count": 150
# }
```

---

## 📊 常见操作

### 读取文档

```bash
feishu_doc action=read doc_token=XXX
```

**返回信息**：
- `title`：文档标题
- `content`：纯文本内容
- `block_count`：块数量
- `revision_id`：版本号

### 更新文档

```bash
# 方式1：追加内容（推荐）
feishu_doc action=append doc_token=XXX content="新内容"

# 方式2：完全重写
feishu_doc action=write doc_token=XXX content="完整内容"
```

### 获取文档列表

```bash
feishu_drive action=list
```

---

## 🎯 最佳实践

### 1. 内容格式

**推荐使用 Markdown**：
```markdown
# 标题

## 二级标题

### 三级标题

- 列表项1
- 列表项2

**粗体** *斜体*

| 列1 | 列2 |
|-----|-----|
| 内容 | 内容 |
```

### 2. 大文档处理

**如果内容很长**：
1. ✅ 分段写入（append 多次）
2. ✅ 使用标题分隔章节
3. ✅ 定期验证内容

### 3. 错误处理

**如果写入失败**：
```bash
# 1. 检查 doc_token 是否正确
# 2. 检查内容格式
# 3. 重新创建文档
feishu_doc action=create title="新文档"
```

---

## 📁 文档管理

### 文档类型

| 类型 | 用途 | 更新频率 |
|------|------|----------|
| **每日简报** | 日常监控报告 | 每天 |
| **深度分析** | 专题研究 | 不定期 |
| **知识库** | 长期知识 | 按需 |

### 当前文档

| 文档 | URL | 用途 |
|------|-----|------|
| 每日简报 | https://feishu.cn/docx/V3budzEa6oJvZTxzaoYcyedbnAc | 地缘政治每日更新 |
| 深度分析 | https://feishu.cn/docx/GqxNd5dqbou2uNx1TMRciHxanNe | 伊朗战争专题 |

---

## 🔍 验证清单

创建/更新文档后，检查：

- ✅ 文档标题正确
- ✅ 内容已写入（block_count > 0）
- ✅ 内容可读（read 返回正确内容）
- ✅ 链接可访问

---

## 🚨 常见问题

### Q1: create 后内容为空？

**原因**：`create` 只创建文档，不会写入 `content` 参数

**解决**：使用 `write` 或 `append`

### Q2: write 后内容没变化？

**原因**：可能是 doc_token 错误

**解决**：
```bash
# 验证 doc_token
feishu_doc action=read doc_token=XXX

# 如果失败，重新创建
feishu_doc action=create title="新文档"
```

### Q3: 如何追加内容？

**正确方式**：
```bash
feishu_doc action=append doc_token=XXX content="

## 新章节

内容..."
```

**注意**：追加内容前先加换行，避免格式混乱

---

## 📚 相关命令

```bash
# 创建文档
feishu_doc action=create title="标题"

# 写入内容
feishu_doc action=write doc_token=XXX content="内容"

# 追加内容
feishu_doc action=append doc_token=XXX content="内容"

# 读取内容
feishu_doc action=read doc_token=XXX

# 列出文档
feishu_drive action=list

# 删除文档（谨慎使用）
feishu_drive action=delete file_token=XXX
```

---

## 🔗 集成到其他流程

### 地缘政治监控

```bash
# 1. 生成报告
python3 scripts/geopolitics-monitor-simple.py

# 2. 读取报告
report=$(cat data/geopolitics/report_2026-03-21.md)

# 3. 追加到飞书
feishu_doc action=append doc_token=V3budzEa6oJvZTxzaoYcyedbnAc content="

---

$report"
```

---

**最后更新**：2026-03-21
**维护者**：AI 记忆管理系统
