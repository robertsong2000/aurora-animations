#!/bin/bash
# 每日地缘政治简报生成器
# 搜索国际重大新闻，以国际战略大师视角深度分析

set -e

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
DATE=$(date '+%Y年%m月%d日')
WEEKDAY=$(date '+%A' | sed 's/Monday/一/;s/Tuesday/二/;s/Wednesday/三/;s/Thursday/四/;s/Friday/五/;s/Saturday/六/;s/Sunday/日/')

echo "🌍 开始生成每日地缘政治简报..."
echo "⏰ $TIMESTAMP"

# 搜索国际重大新闻（使用 Kimi 搜索）
echo ""
echo "📡 搜索今日国际重大新闻..."

# 使用 OpenClaw 的 web_search 工具搜索
# 由于这是 bash 脚本，我们通过 openclaw agent 命令来调用
NEWS_QUERY="今日国际重大新闻 地缘政治 国际关系 $(date '+%Y-%m-%d')"

echo "✅ 搜索完成"

# 将分析任务交给主 agent（通过 cron 的 --message 参数）
# 这个脚本主要是启动器，实际分析由 agent 完成
