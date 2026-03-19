#!/bin/bash
# Survey Writer - 完整工作流程
# 基于UAV_Delay_Survey_v3成功经验

set -e

# 参数
TOPIC="${1:-UAV communication delay}"
SUBTOPICS="${2:-time delay identification,guidance prediction,compensation control}"
OUTPUT_DIR="${3:-./outputs}"

echo "======================================"
echo "Survey Writer - 完整工作流程"
echo "======================================"
echo ""
echo "主题: $TOPIC"
echo "子领域: $SUBTOPICS"
echo "输出目录: $OUTPUT_DIR"
echo ""

mkdir -p "$OUTPUT_DIR"

# Phase 1: 文献调研
echo ""
echo "======================================"
echo "Phase 1/6: 文献调研"
echo "======================================"
./workflows/phase1.sh "$TOPIC" "$SUBTOPICS" "$OUTPUT_DIR"

# Phase 2: 框架构建
echo ""
echo "======================================"
echo "Phase 2/6: 框架构建"
echo "======================================"
cat > "$OUTPUT_DIR/framework.yaml" << EOF
survey_title: "$TOPIC"
survey_title_en: "A Comprehensive Survey on ${TOPIC}"
keywords: ["keyword1", "keyword2", "keyword3"]

total_pages: 35
estimated_words: 15000

chapters:
  - id: 1
    title: 引言
    sections: 4
    pages: 3
  - id: 2
    title: 基础理论
    sections: 3
    pages: 4
  - id: 3
    title: 方法A
    sections: 4
    pages: 6
  - id: 4
    title: 方法B
    sections: 4
    pages: 6
  - id: 5
    title: 方法C
    sections: 4
    pages: 6
  - id: 6
    title: 实验与应用
    sections: 3
    pages: 5
  - id: 7
    title: 未来研究方向
    sections: 3
    pages: 4
EOF
echo "✓ 框架构建完成"

# Phase 3: 内容撰写 (提示用户)
echo ""
echo "======================================"
echo "Phase 3/6: 内容撰写"
echo "======================================"
echo "⚠️  请使用以下prompt生成内容："
echo ""
echo "请基于以下框架撰写综述："
echo "主题: $TOPIC"
echo "框架: $OUTPUT_DIR/framework.yaml"
echo "文献: $OUTPUT_DIR/key_papers.md"
echo ""
echo "要求："
echo "1. 使用templates/main.tex模板"
echo "2. 生成30+页内容"
echo "3. 每类方法包含局限性分析"
echo "4. 使用表格替代孤立列举"
echo ""
read -p "按Enter继续..."

# Phase 4: 可视化
echo ""
echo "======================================"
echo "Phase 4/6: 可视化"
echo "======================================"
echo "⚠️  请生成以下图表："
echo "  1. 系统架构图 (TikZ)"
echo "  2. 方法分类框架图 (TikZ)"
echo "  3. 关键技术框图 (TikZ)"
echo "  4. 方法对比表 (三线表)"
echo "  5. 性能对比表 (三线表)"
echo ""
echo "参考: templates/figure_tikz.tex"
echo ""
read -p "按Enter继续..."

# Phase 5: 引用系统
echo ""
echo "======================================"
echo "Phase 5/6: 引用系统"
echo "======================================"
echo "⚠️  请检查引用系统："
echo "  1. 使用thebibliography环境"
echo "  2. 每条文献有\\bibitem{标签}"
echo "  3. 正文使用\\cite{标签}"
echo "  4. 无[??]引用失败"
echo ""
read -p "按Enter继续..."

# Phase 6: 质量检查
echo ""
echo "======================================"
echo "Phase 6/6: 质量检查"
echo "======================================"

if [ -f "$OUTPUT_DIR/survey.tex" ]; then
    python3 tools/quality_checker.py "$OUTPUT_DIR/survey.tex" -o "$OUTPUT_DIR/quality_report.md"
else
    echo "⚠️  未找到survey.tex，请先生成内容"
fi

echo ""
echo "======================================"
echo "工作流程完成!"
echo "======================================"
echo ""
echo "输出文件:"
echo "  - $OUTPUT_DIR/literature_pool.json"
echo "  - $OUTPUT_DIR/key_papers.md"
echo "  - $OUTPUT_DIR/framework.yaml"
echo "  - $OUTPUT_DIR/survey.tex"
echo "  - $OUTPUT_DIR/survey.pdf"
echo "  - $OUTPUT_DIR/quality_report.md"
echo ""
echo "下一步:"
echo "  1. 检查质量报告"
echo "  2. 根据反馈迭代优化"
echo "  3. 重复Phase 3-6直到满意"
echo ""
