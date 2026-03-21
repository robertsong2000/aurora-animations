#!/bin/bash
# 重试推送到GitHub的脚本

cd /home/ubuntu/.openclaw/workspace

echo "检查待推送的提交..."
git log --oneline origin/main..HEAD

echo ""
echo "尝试推送..."
for i in {1..5}; do
    echo "=== 尝试 $i/5 ==="
    if timeout 45 git push origin main; then
        echo "✅ 推送成功！"
        exit 0
    else
        echo "❌ 尝试 $i 失败，等待10秒..."
        sleep 10
    fi
done

echo ""
echo "❌ 所有尝试都失败了。请检查网络连接或手动推送。"
echo "待推送的提交："
git log --oneline origin/main..HEAD
exit 1
