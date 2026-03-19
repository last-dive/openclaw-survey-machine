#!/bin/bash
# 综述永动机 - 主入口脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 显示Banner
cat << 'EOF'
╔═══════════════════════════════════════════════════════════════╗
║                   综述永动机 v1.0                             ║
║              Survey Machine - One-click Survey                ║
╚═══════════════════════════════════════════════════════════════╝
EOF

# 帮助信息
if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "用法: ./survey-machine.sh [选项] <主题>"
    echo ""
    echo "选项:"
    echo "  -t, --topic <主题>      综述主题"
    echo "  -s, --subtopics <列表>  子主题，逗号分隔"
    echo "  -p, --pages <数量>      目标页数"
    echo "  -c, --config <文件>     配置文件"
    echo "  -h, --help              显示帮助"
    echo ""
    echo "示例:"
    echo "  ./survey-machine.sh '无人机通信时延'"
    exit 0
fi

# 解析参数
TOPIC=""
SUBTOPICS=""
PAGES="50"
CONFIG="config/config.yaml"

while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--topic) TOPIC="$2"; shift 2 ;;
        -s|--subtopics) SUBTOPICS="$2"; shift 2 ;;
        -p|--pages) PAGES="$2"; shift 2 ;;
        -c|--config) CONFIG="$2"; shift 2 ;;
        *) TOPIC="$1"; shift ;;
    esac
done

if [ -z "$TOPIC" ]; then
    echo "错误: 请提供综述主题"
    echo "用法: ./survey-machine.sh '主题'"
    exit 1
fi

echo "主题: $TOPIC"
echo "子主题: ${SUBTOPICS:-无}"
echo "目标页数: $PAGES"
echo ""

# 创建工作目录
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
WORK_DIR="outputs/${TOPIC// /_}_${TIMESTAMP}"
mkdir -p "$WORK_DIR"
mkdir -p "$WORK_DIR/figures"

echo "工作目录: $WORK_DIR"
echo ""

# 运行工作流编排器
python3 core/survey-writer/workflows/run_all.sh "$TOPIC" "$SUBTOPICS" "$WORK_DIR" 2>/dev/null || \
python3 utils/orchestrator.py \
    --topic "$TOPIC" \
    --subtopics "$SUBTOPICS" \
    --pages "$PAGES" \
    --config "$CONFIG" \
    --work-dir "$WORK_DIR"

echo ""
echo "✅ 综述生成完成！"
echo "输出目录: $WORK_DIR"
