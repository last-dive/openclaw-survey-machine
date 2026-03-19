#!/bin/bash
# 一键安装脚本

echo "🚀 安装综述永动机..."
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 检查依赖
echo "📦 检查依赖..."

# Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

# XeLaTeX
if ! command -v xelatex &> /dev/null; then
    echo "⚙️  安装 LaTeX..."
    sudo apt-get update
    sudo apt-get install -y texlive-xetex texlive-lang-chinese \
        texlive-fonts-recommended texlive-latex-extra
fi

# Python依赖
echo "📦 安装Python依赖..."
pip3 install pyyaml pillow numpy requests --user

# 创建配置
if [ ! -f config/config.yaml ]; then
    cp config/config.template.yaml config/config.yaml
    echo "⚙️  配置文件已创建，请编辑 config/config.yaml 填入API Keys"
fi

# 设置权限
chmod +x survey-machine.sh
chmod +x core/*/workflows/*.sh 2>/dev/null || true

echo ""
echo "✅ 安装完成！"
echo ""
echo "📝 下一步:"
echo "   1. 编辑 config/config.yaml 填入API Keys"
echo "   2. 运行 ./verify.sh 验证安装"
echo "   3. 开始撰写: ./survey-machine.sh '主题'"
