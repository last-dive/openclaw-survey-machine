# Survey Expander

> 专门用于初稿完成后，页数不足时的合规高质量扩展

## 版本信息

- **版本**: 1.0.0
- **基于**: Survey Expander v1.0 初稿 (2026-03-19)
- **遵循**: survey-writer v2.1.0 原则
- **作者**: 北海 (Bei Hai)

## 快速开始

### 安装

```bash
cd ~/clawd/skills/survey-expander
chmod +x tools/*.py
```

### 使用

**自然语言触发**：
```
请使用 survey-expander 扩展我的综述初稿，目标页数为 35 页。
```

**命令行触发**：
```bash
# 分析初稿
python3 tools/analyze_sections.py \
  --input draft.tex \
  --output expansion_plan.md

# 质量检查
python3 tools/quality_checker.py \
  --input expanded.tex \
  --original draft.tex \
  --output quality_report.md
```

## 核心原则

1. **亲自分析**：由主代理亲自分析扩充位置，撰写扩充内容
2. **维持框架**：不删除当前框架下的子标题，不轻易增加新标题
3. **质量优先**：扩充内容必须与原文逻辑连贯，无矛盾
4. **服务论点**：扩展内容必须服务于核心论点
5. **学术严谨**：避免重复内容，保持论述一致性

## 工作流程

1. **Phase 1**: 分析诊断（10min）- 识别扩展机会点
2. **Phase 2**: 内容扩充（核心）- 基于文献扩充内容
3. **Phase 3**: 图表增强（30min）- 增加高质量图表
4. **Phase 4**: 文献完善（20min）- 补充文献标识信息
5. **Phase 5**: 质量检查（15min）- 确保质量达标

## 目录结构

```
survey-expander/
├── SKILL.md                 # 技能主文档
├── README.md                # 本文件
├── workflows/               # 工作流脚本
├── tools/                   # 工具脚本
│   ├── analyze_sections.py  # 章节分析工具
│   └── quality_checker.py   # 质量检查工具
├── config/                  # 配置文件
│   └── expander.yaml        # 扩展参数配置
└── lessons/                 # 经验教训
```

## 相关技能

- [survey-writer](../survey-writer/) - 综述撰写（v2.1.0）
- [latex-chinese-typesetting](../latex-chinese-typesetting/) - LaTeX 中文排版
- [latex-flowchart](../latex-flowchart/) - TikZ 流程图绘制

## 许可

MIT License
