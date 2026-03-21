#!/bin/bash
# 统一搜索脚本：同时搜索 OpenClaw 记忆 + agent-knowledge

QUERY="$1"

echo "=========================================="
echo "🔍 搜索: $QUERY"
echo "=========================================="
echo ""

echo "📁 OpenClaw 记忆 (memory/)"
echo "----------------------------------------"
rg -i "$QUERY" ~/.openclaw/workspace/memory/ 2>/dev/null | head -20
echo ""

echo "📚 agent-knowledge 知识库"
echo "----------------------------------------"
rg -i "$QUERY" ~/.soulshare/agent/knowledge/ 2>/dev/null | head -20
echo ""

echo "=========================================="
echo "✅ 搜索完成"
