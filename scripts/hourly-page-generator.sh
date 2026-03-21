#!/bin/bash
# 每小时自动生成创意HTML页面的脚本（AI驱动版 - 直连）

set -e

WORKSPACE="/home/ubuntu/.openclaw/workspace"
OUTPUT_DIR="$WORKSPACE"
DATA_DIR="$WORKSPACE/scripts/data"
LOG_FILE="$DATA_DIR/page-generator.log"
HISTORY_FILE="$DATA_DIR/page-history.json"

# 创建目录
mkdir -p "$DATA_DIR"

# 记录日志
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# 主题池
declare -A THEMES
THEMES["粒子动画"]="交互式粒子系统，粒子跟随鼠标移动并相互连接，霓虹配色，点击产生爆炸效果"
THEMES["星空效果"]="夜空星星闪烁和流星划过效果，深蓝渐变背景，鼠标移动产生星光拖尾"
THEMES["波浪动画"]="多层波浪叠加的海洋效果，深浅蓝渐变，鼠标控制波浪高度，点击产生涟漪"
THEMES["几何万花筒"]="旋转几何图形组合，万花筒效果，渐变色边框，鼠标控制旋转速度"
THEMES["霓虹时钟"]="创意模拟时钟，霓虹指针，秒针平滑转动，背景粒子动画"
THEMES["烟花盛宴"]="点击触发烟花爆炸，多彩粒子，自动随机烟花，拖尾效果"
THEMES["矩阵雨"]="黑客帝国风格字符雨，绿色字符下落，鼠标影响下落方向"
THEMES["分形艺术"]="曼德博集合或朱利亚集合分形，可缩放探索，颜色渐变"
THEMES["极光效果"]="北极光波浪动画，绿色紫色渐变，星星背景，缓慢流动"
THEMES["水波纹"]="点击产生水波纹扩散效果，多重波纹叠加，反射折射"
THEMES["火焰效果"]="逼真火焰动画，橙红色渐变，粒子系统，可调节风力方向"
THEMES["雨滴效果"]="雨滴落在水面的效果，涟漪扩散，倒影，灰蓝色调"
THEMES["银河系"]="银河系旋转效果，星星密集区域和暗区，中心明亮"
THEMES["DNA螺旋"]="3D DNA双螺旋结构旋转，彩色节点，发光效果"
THEMES["城市天际线"]="动态城市轮廓，窗户灯光闪烁，日夜变化，流星划过"

# 读取历史
read_history() {
    [ -f "$HISTORY_FILE" ] && cat "$HISTORY_FILE" || echo '{"recent_themes":[]}'
}

# 获取最近使用的主题
get_recent_themes() {
    local history=$(read_history)
    echo "$history" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for theme in data.get('recent_themes', [])[:8]:
    print(theme)
" 2>/dev/null || echo ""
}

# 选择主题
select_theme() {
    local recent=$(get_recent_themes)
    local all_keys=("${!THEMES[@]}")
    local available=()
    
    for key in "${all_keys[@]}"; do
        [ -z "$(echo "$recent" | grep "^$key$")" ] && available+=("$key")
    done
    
    [ ${#available[@]} -eq 0 ] && { log "所有主题已用，重置"; available=("${all_keys[@]}"); }
    
    echo "${available[$RANDOM % ${#available[@]}]}"
}

# 更新历史
update_history() {
    python3 << PYEOF
import json, os
theme, history_file = "$1", "$HISTORY_FILE"
data = {"recent_themes": [], "total": 0}
if os.path.exists(history_file):
    with open(history_file) as f: data = json.load(f)
if theme in data["recent_themes"]: data["recent_themes"].remove(theme)
data["recent_themes"].insert(0, theme)
data["recent_themes"] = data["recent_themes"][:30]
data["total"] = data.get("total", 0) + 1
with open(history_file, 'w') as f: json.dump(data, f, indent=2)
PYEOF
}

# 主流程
log "========================================"
log "开始生成新页面（AI直连版）"
log "========================================"

cd "$WORKSPACE"

# 确保在 main 分支
git checkout main 2>/dev/null || log "已在 main 分支"

# 选择主题
THEME=$(select_theme)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FILENAME="ai-${THEME}-${TIMESTAMP}.html"
OUTPUT_FILE="$OUTPUT_DIR/$FILENAME"

log "选择主题: $THEME"
log "目标文件: $FILENAME"

# 构建任务
DESCRIPTION=${THEMES[$THEME]}

TASK="请为以下主题生成一个完整的、可直接运行的HTML页面，保存到文件 $OUTPUT_FILE

**主题**: $THEME

**设计要求**:
$DESCRIPTION

**技术要求**:
1. 单文件HTML - 所有CSS和JavaScript必须内联
2. 响应式设计 - 适配桌面和移动设备
3. 60fps流畅动画 - 使用 requestAnimationFrame 或 CSS动画
4. 交互功能 - 至少2种鼠标交互（移动、点击等）
5. Canvas或CSS3实现动画
6. 性能优化 - 避免内存泄漏

**代码规范**:
- 添加清晰的中文注释
- 页面左上角显示标题和简单说明（半透明背景）
- 独特的配色方案（避免紫色渐变）

**输出要求**:
1. 只输出完整的HTML代码
2. 直接保存到文件: $OUTPUT_FILE
3. 不要有任何解释文字或markdown代码块标记
4. 确保文件可以正常运行

现在请生成完整的HTML代码并保存到指定文件。"

log "调用 AI 生成页面..."

# 调用 openclaw agent 直接生成
RESULT=$(openclaw agent --local --message "$TASK" --timeout 180 2>&1)

if [ $? -eq 0 ]; then
    log "AI 生成完成"
    
    # 检查文件是否存在
    if [ -f "$OUTPUT_FILE" ]; then
        log "文件已生成: $FILENAME"
        
        # 更新历史
        update_history "$THEME"
        
        # Git 提交
        git add "$OUTPUT_FILE"
        git commit -m "feat: AI生成页面 - $THEME ($TIMESTAMP)

- 主题: $THEME
- 技术: Canvas/CSS3 动画
- 交互: 鼠标交互
- 生成时间: $(date '+%Y-%m-%d %H:%M:%S')" || {
            log "没有需要提交的更改"
        }
        
        # 推送
        log "推送到 GitHub..."
        if timeout 60 git push origin main 2>&1 | tee -a "$LOG_FILE"; then
            log "✅ 页面已成功推送到 GitHub"
            echo "✅ 完成: $FILENAME (主题: $THEME)"
            echo "🌐 GitHub: https://github.com/robertsong2000/html_sample"
        else
            log "⚠️ GitHub 推送失败"
            echo "⚠️ 本地已完成，推送失败: $FILENAME"
        fi
    else
        log "❌ 文件未生成"
        echo "❌ 生成失败: AI 未生成文件"
        echo "$RESULT"
    fi
else
    log "❌ AI 生成失败"
    echo "❌ AI 调用失败"
    echo "$RESULT"
fi
