# Survey Writer Skill

基于UAV_Delay_Survey_v3成功经验构建的高质量学术综述撰写助手。

## 快速开始

```bash
# 1. 进入skill目录
cd ~/clawd/skills/survey-writer

# 2. 运行完整工作流程
./workflows/run_all.sh "主题" "子领域1,子领域2,子领域3"

# 3. 或分阶段执行
./workflows/phase1.sh "UAV communication delay" \
  "time delay identification,guidance prediction,compensation control"
```

## 目录结构

```
survey-writer/
├── SKILL.md                 # 主文档
├── README.md               # 本文件
├── prompts/                # Prompt模板
│   ├── 01_decomposition.txt
│   ├── 02_research.txt
│   ├── 03_framework.txt
│   ├── 04_content.txt
│   ├── 05_visualization.txt
│   ├── 06_citation.txt
│   └── 07_review.txt
├── templates/              # LaTeX模板
│   ├── main.tex
│   ├── section.tex
│   ├── table.tex
│   └── figure_tikz.tex
├── workflows/              # 工作流程脚本
│   ├── phase1.sh          # 文献调研
│   ├── phase2.sh          # 框架构建
│   ├── phase3.sh          # 内容撰写
│   ├── phase4.sh          # 可视化
│   ├── phase5.sh          # 引用系统
│   └── phase6.sh          # 质量检查
├── tools/                  # 工具脚本
│   └── quality_checker.py # 质量检查
├── lessons/                # 经验教训
│   ├── v3_iteration_log.md
│   └── failure_cases.md
└── config/                 # 配置文件
    ├── quality_standards.yaml
    └── checklists.yaml
```

## 核心特性

### 1. 6阶段标准化流程

| 阶段 | 名称 | 时长 | 输出 |
|------|------|------|------|
| 1 | 文献调研 | 30min | 120篇文献库 |
| 2 | 框架构建 | 20min | 7章结构 |
| 3 | 内容撰写 | 2-3h | 30+页初稿 |
| 4 | 可视化 | 30min | 5+张图表 |
| 5 | 引用系统 | 20min | 标准引用 |
| 6 | 质量检查 | 30min | 质量报告 |

### 2. 7章标准结构

```
第1章 引言
第2章 基础理论
第3章 方法A
第4章 方法B
第5章 方法C
第6章 实验与应用
第7章 未来方向
```

### 3. 6维度质量检查

- 结构完整性 (20分)
- 引用系统 (20分)
- 排版格式 (15分)
- 图表质量 (15分)
- 内容深度 (15分)
- 编译状态 (15分)

**总分**: 100分
**评级**: A+ (90+) / A (80-89) / B+ (70-79) / B (60-69) / C (<60)

## 使用示例

### 示例1: 无人机通信时延综述

```bash
./workflows/run_all.sh \
  "无人机通信时延预测与补偿技术" \
  "时滞辨识,制导信息预测,时滞补偿控制"
```

### 示例2: 使用质量检查工具

```bash
python3 tools/quality_checker.py survey.tex -o report.md
```

输出:
```
======================================
综述质量检查报告
======================================
总分: 90/100 (90.0%)
评级: A+ (优秀，可投稿顶刊)
======================================
```

## 关键成功因素

基于UAV_Delay_Survey_v3经验:

1. **先框架后内容** - 避免返工
2. **迭代式优化** - 每章立即检查
3. **可视化优先** - 确保技术路线清晰
4. **引用系统化** - 从开始就规范
5. **批判性思维** - 每方法必分析局限

## 失败案例规避

| 问题 | 现象 | 规避策略 |
|------|------|---------|
| 文档截断 | 只有5页 | 检查`\end{document}`唯一性 |
| 引用失败 | `[??]` | 使用`thebibliography` |
| 孤立列举 | `(1)(2)(3)` | 改为表格或连续叙述 |
| 框图重叠 | 节点错位 | 使用绝对坐标 |

## 参考案例

- **成功案例**: UAV_Delay_Survey_v3 (35页, 90分)
- **对比案例**: AutoSurvey输出 (5页, 65分)

## 贡献

基于北海(Bei Hai)在2026-03-18的UAV_Delay_Survey_v3迭代经验构建。

## 许可

MIT License
