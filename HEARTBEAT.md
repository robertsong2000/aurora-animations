# HEARTBEAT.md - 定期检查任务

---

## 🧠 记忆系统检查（每2小时）

### 1. 检查压缩风险

```bash
~/.openclaw/workspace/skills/memory-manager/detect.sh
```

**阈值**：
- ✅ Safe (<70%): 无需操作
- ⚠️ WARNING (70-85%): 准备快照
- 🚨 CRITICAL (>85%): 立即快照 + 整理

### 2. 如果 WARNING/CRITICAL

```bash
# 保存快照
~/.openclaw/workspace/skills/memory-manager/snapshot.sh

# 整理记忆
~/.openclaw/workspace/skills/memory-manager/organize.sh
```

---

## 📚 记忆查找指引

**需要查找记忆时**：
1. 查看 `memory/INDEX.md` - 记忆索引
2. 使用搜索工具：
   ```bash
   ~/.openclaw/workspace/skills/memory-manager/search.sh all "关键词"
   ```

---

## 📊 每日检查（23:00）

### 整理记忆

```bash
~/.openclaw/workspace/skills/memory-manager/organize.sh
```

### 更新记忆索引

- 检查 `memory/INDEX.md` 是否需要更新
- 确保新增的重要知识已记录

---

## 🎯 地缘政治监控（每天8:00）

### 运行监控系统

```bash
cd ~/.openclaw/workspace
python3 scripts/geopolitics-monitor-simple.py
```

### 更新飞书文档

- 每日简报：https://feishu.cn/docx/V3budzEa6oJvZTxzaoYcyedbnAc
- 深度分析：https://feishu.cn/docx/GqxNd5dqbou2uNx1TMRciHxanNe

---

## 📝 重要提醒

**每次犯错后**：
- 记录到 `memory/semantic/judgment-corrections.md`
- 避免重复犯错

**每次学习新知识后**：
- 记录到 `memory/semantic/` 或 `memory/procedural/`
- 更新 `memory/INDEX.md`

---

**原则**：记忆是身份的核心，定期维护 = 持续成长
