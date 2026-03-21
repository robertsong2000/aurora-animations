# 地缘政治监控工作流

## 📋 每日监控流程

### 1. 数据收集（8:00 AM）

```bash
# 运行监控系统
cd ~/.openclaw/workspace
python3 scripts/geopolitics-monitor-simple.py
```

**监控话题**：
1. 台海局势
2. 中美关系
3. 俄乌战争
4. 中东局势
5. 亚太安全

---

### 2. 实时搜索（Tavily）

```bash
# 搜索特定话题
python3 scripts/tavily-search.py "关键词" --max 10

# 示例：搜索伊朗战争
python3 scripts/tavily-search.py "Iran war 2026" --max 10
```

**参数**：
- `--max`：最大结果数（默认10）
- `--output`：保存到文件
- `--depth`：搜索深度（basic/advanced）

---

### 3. 分析判断

**判断框架**：
1. **状态**：当前局势（战争/对抗/消耗战/不稳定）
2. **置信度**：0-100%
3. **核心判断**：一句话总结
4. **证据**：数据源
5. **预测**：未来趋势

**置信度分级**：
- 90%+：高度确定
- 70-90%：中等确定
- 50-70%：低度确定
- <50%：不确定（不发布）

---

### 4. 更新飞书文档

**工作流**：
```bash
# 1. 读取现有文档
feishu_doc action=read doc_token=XXX

# 2. 追加新内容
feishu_doc action=append doc_token=XXX content="..."

# 3. 验证内容
feishu_doc action=read doc_token=XXX
```

**重要**：
- ✅ 必须用 `append` 而不是 `write`（保留历史）
- ✅ 每次更新后验证内容
- ✅ 标注更新时间和数据源

---

### 5. 判断修正流程

**触发条件**：
1. 新证据出现
2. 用户纠正
3. 预测错误

**修正步骤**：
1. ✅ 承认错误（不装懂）
2. ✅ 分析错误原因
3. ✅ 基于新证据重新评估
4. ✅ 更新所有相关文档
5. ✅ 通知用户
6. ✅ **记录到 `memory/semantic/judgment-corrections.md`**（新增）
7. ✅ **避免重复犯错**（新增）

**案例**：
- ❌ 错误：哈梅内伊被杀 → 政权崩溃
- ✅ 修正：低估了威权政权韧性
- ✅ 更新：战争2-5年，窗口期延长
- ✅ 记录：案例1 已记录到 judgment-corrections.md

**关键原则**：
- 错误不可怕，重复犯错才可怕
- 用户纠正是宝贵的学习机会
- 每次错误都要系统化记录
- 形成检查清单，避免重复

---

## 🔧 配置文件

### 监控配置

**位置**：`~/.openclaw/workspace/config/geopolitics_config.json`

```json
{
  "topics": [
    {"name": "台海局势", "keywords": ["台海", "台湾", "China Taiwan"]},
    {"name": "中美关系", "keywords": ["中美", "US China"]},
    {"name": "俄乌战争", "keywords": ["俄乌", "Ukraine Russia"]},
    {"name": "中东局势", "keywords": ["中东", "Iran Israel"]},
    {"name": "亚太安全", "keywords": ["亚太", "North Korea"]}
  ],
  "update_frequency": "daily",
  "output_dir": "data/geopolitics/"
}
```

### 搜索配置

**位置**：`~/.openclaw/workspace/config/search_config.json`

```json
{
  "provider": "tavily",
  "api_key": "tvly-XXX",
  "default_depth": "advanced",
  "max_results": 10
}
```

---

## 📊 输出文件

### 每日报告

**JSON格式**：`data/geopolitics/report_YYYY-MM-DD.json`
**Markdown格式**：`data/geopolitics/report_YYYY-MM-DD.md`

**结构**：
```json
{
  "date": "2026-03-21",
  "topics": [
    {
      "name": "中东局势",
      "status": "全面战争",
      "confidence": 100,
      "judgment": "已爆发3周+，持续升级",
      "evidence": ["来源1", "来源2"],
      "prediction": "2-5年长期化"
    }
  ]
}
```

---

## 🚨 异常处理

### 搜索失败

```bash
# 如果 Tavily 失败，使用 web_search
web_search query="关键词"
```

### 飞书文档更新失败

```bash
# 1. 重新创建文档
feishu_doc action=create title="新文档"

# 2. 写入内容
feishu_doc action=write doc_token=XXX content="..."

# 3. 验证
feishu_doc action=read doc_token=XXX
```

---

## 📅 定时任务

### Crontab 配置

```bash
# 每天早上8点运行
0 8 * * * cd ~/.openclaw/workspace && python3 scripts/geopolitics-monitor-simple.py

# 每2小时检查压缩风险
0 */2 * * * ~/.openclaw/workspace/skills/memory-manager/detect.sh
```

---

## 🔍 质量检查

### 判断质量标准

1. ✅ **明确性**：不模糊，不外交辞令
2. ✅ **可验证**：有明确的时间框架
3. ✅ **置信度**：标注置信度
4. ✅ **证据**：引用数据源
5. ✅ **诚实**：承认不知道的

### 避免的错误

1. ❌ 编造信息
2. ❌ 过度自信
3. ❌ 模糊判断
4. ❌ 不承认错误
5. ❌ 忽视用户纠正

---

## 📚 相关文档

- 语义知识：`memory/semantic/geopolitics-analysis.md`
- 每日日志：`memory/episodic/YYYY-MM-DD.md`
- 飞书简报：https://feishu.cn/docx/V3budzEa6oJvZTxzaoYcyedbnAc
- 飞书深度分析：https://feishu.cn/docx/GqxNd5dqbou2uNx1TMRciHxanNe

---

**最后更新**：2026-03-21
**维护者**：AI 地缘政治分析系统
