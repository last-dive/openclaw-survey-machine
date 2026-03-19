# Survey Evolution Skill v1.0.0

> **综述写作的最后一公里** —— 通过多维度质量检查、迭代改进和版本管理，将综述初稿打磨至 A+ 可投稿水平。

## 简介

Survey Evolution 是 survey-writer v2.1.0 和 survey-expander v1.0.0 的配套技能，专注于综述论文的质量检查、迭代改进和版本管理。

## 核心功能

- **8 维度质量检查**：结构完整性、引言质量、分类框架、内容深度、引用系统、图表质量、排版规范、未来方向
- **自动评分系统**：100 分制，A+/A/B+/B/C 五级评级
- **自动改进工具**：根据质量报告自动修复常见问题
- **版本管理**：支持 v1 → v2 → v3 → ... → A+ 的迭代流程

## 快速开始

### 1. 质量检查

```bash
python3 ~/clawd/skills/survey-evolution/tools/quality_checker.py \
  --input survey.tex \
  --output quality_report.md
```

### 2. 自动改进

```bash
python3 ~/clawd/skills/survey-evolution/tools/improver.py \
  --input survey.tex \
  --report quality_report.md \
  --output survey_v2.tex
```

### 3. 迭代改进

重复执行质量检查和自动改进，直到达到 A+ 水平（90+ 分）。

## 8 维度评估体系

| 维度 | 分值 | 检查重点 |
|------|------|----------|
| 结构完整性 | 15 | 章节齐全，无截断 |
| 引言质量 | 10 | 背景、问题、贡献、组织 |
| 分类框架 | 15 | 原创性、清晰度、覆盖度 |
| 内容深度 | 15 | 原理、优缺点、批判性分析 |
| 引用系统 | 15 | 格式规范、文献真实、分布合理 |
| 图表质量 | 10 | 数量充足、清晰无重叠 |
| 排版规范 | 10 | 格式统一、交叉引用正确 |
| 未来方向 | 10 | 具体性、洞察力、可操作性 |

## 评级标准

| 等级 | 分数 | 说明 | 行动 |
|------|------|------|------|
| A+ | 90-100 | 可投稿顶刊 | 完成 |
| A | 80-89 | 可投稿核心期刊 | 微调后投稿 |
| B+ | 70-79 | 需进一步完善 | 针对性改进 |
| B | 60-69 | 需大幅修改 | 结构性调整 |
| C | <60 | 不合格 | 重写 |

## 与 Survey Writer/Expander 的衔接

```
Survey Writer → Survey Expander → Survey Evolution
     ↓              ↓                ↓
   初稿 v1        扩展 v1         检查 + 改进
                                     ↓
                              v2, v3, ... → A+
```

## 文件结构

```
survey-evolution/
├── SKILL.md                    # 主技能文档
├── README.md                   # 本文件
├── config/
│   └── quality_standards.yaml  # 质量标准配置
├── tools/
│   ├── quality_checker.py      # 质量检查工具
│   └── improver.py             # 自动改进工具
└── outputs/                    # 输出目录
    ├── survey_v1/
    ├── survey_v2/
    └── survey_final/
```

## 使用示例

### 示例 1：检查现有综述

```bash
# 检查综述质量
python3 tools/quality_checker.py \
  --input RL_Aircraft_Control_Survey_expanded.tex \
  --output report.md

# 查看报告
cat report.md
```

### 示例 2：迭代改进

```bash
# 第一轮改进
python3 tools/quality_checker.py -i survey.tex -o report_v1.md
python3 tools/improver.py -i survey.tex -r report_v1.md -o survey_v2.tex

# 第二轮改进
python3 tools/quality_checker.py -i survey_v2.tex -o report_v2.md
python3 tools/improver.py -i survey_v2.tex -r report_v2.md -o survey_v3.tex

# 直到达到 A+
```

## 核心原则

1. **先诊断，后改进**：先全面检查，再针对性修改
2. **版本管理**：每次重大改进都是一次版本迭代
3. **A+ 目标**：以可投稿顶刊为标准
4. **学术诚信**：0 编造、0 空洞、0 孤立

## 常见问题

### Q: 综述真的不需要实验章节吗？

A: 大多数综述（Survey/Review）不需要原创性实验。评估重点是文献梳理、分类框架和批判性分析。

### Q: 什么时候可以停止迭代？

A: 当总分 >= 90 且所有维度 >= 70 时，可以认为达到 A+ 水平。

### Q: 如果某个维度始终无法提升怎么办？

A: 分析原因：
- 结构性问题 → 重写该章节
- 内容不足 → 补充更多文献
- 格式问题 → 使用工具自动修复

## 更新日志

### v1.0.0 (2026-03-19)

- 初始版本
- 8 维度质量检查体系
- 自动改进工具
- 版本管理规范

## 许可

MIT License

## 相关技能

- [survey-writer v2.1.0](../survey-writer/) - 综述初稿撰写
- [survey-expander v1.0.0](../survey-expander/) - 综述内容扩展
