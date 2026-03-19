# LaTeX 中文排版技能

**技能名称**: latex-chinese-typesetting  
**创建时间**: 2026-03-09  
**用途**: 撰写复杂带公式、中文的 PDF 文档

---

## 安装指南

### 1. 安装 LaTeX 发行版

```bash
# 安装 TeX Live（完整版，包含中文支持）
sudo apt-get update
sudo apt-get install -y texlive-xetex texlive-lang-chinese texlive-fonts-recommended texlive-latex-extra

# 安装中文字体
sudo apt-get install -y fonts-wqy-zenhei fonts-wqy-microhei
```

### 2. 安装 LaTeX 编辑器

**推荐**: TeXstudio（功能强大，支持中文）

```bash
sudo apt-get install -y texstudio
```

**备选**: VS Code + LaTeX Workshop 插件

---

## 中文 LaTeX 文档模板

### 基础模板（article）

```latex
\documentclass[UTF8]{ctexart}

\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{hyperref}

% 页面设置
\geometry{a4paper, margin=2.5cm}

% 标题信息
\title{文档标题}
\author{作者姓名}
\date{\today}

\begin{document}

\maketitle

\section{引言}
这是中文内容。

\section{数学公式}
行内公式：$E = mc^2$

独立公式：
\begin{equation}
    \int_{a}^{b} f(x) \, dx = F(b) - F(a)
\end{equation}

\section{结论}
文档结束。

\end{document}
```

### 高级模板（report）

```latex
\documentclass[UTF8, 12pt]{ctexrep}

% 数学包
\usepackage{amsmath, amssymb, amsthm}
\usepackage{mathtools}

% 页面布局
\usepackage{geometry}
\geometry{a4paper, left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm}

% 图表
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{caption}

% 代码
\usepackage{listings}
\usepackage{xcolor}

% 链接
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue}

% 定理环境
\theoremstyle{definition}
\newtheorem{definition}{定义}[chapter]
\newtheorem{theorem}{定理}[chapter]

% 代码样式
\lstset{
    language=Matlab,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{green!60!black},
    stringstyle=\color{orange},
    numbers=left,
    numberstyle=\tiny\color{gray},
    frame=single
}

\title{\textbf{论文标题}}
\author{作者}
\date{\today}

\begin{document}

\maketitle
\tableofcontents

\chapter{绪论}
\section{研究背景}
中文内容...

\chapter{理论基础}
\section{数学模型}
\begin{equation}
    \frac{d}{dt}\begin{bmatrix} x \\ \dot{x} \end{bmatrix} = 
    \begin{bmatrix} 0 & 1 \\ -\omega^2 & -2\zeta\omega \end{bmatrix}
    \begin{bmatrix} x \\ \dot{x} \end{bmatrix}
\end{equation}

\chapter{结论}
总结...

\end{document}
```

---

## 编译命令

### XeLaTeX（推荐用于中文）

```bash
# 基础编译
xelatex document.tex

# 包含参考文献的完整编译
xelatex document.tex
bibtex document
xelatex document.tex
xelatex document.tex

# 或者使用 latexmk 自动编译
latexmk -xelatex document.tex
```

### LuaLaTeX（备选）

```bash
lualatex document.tex
```

---

## 常用数学符号

### 希腊字母

| 符号 | LaTeX | 符号 | LaTeX |
|------|-------|------|-------|
| α | `\alpha` | β | `\beta` |
| γ | `\gamma` | δ | `\delta` |
| λ | `\lambda` | θ | `\theta` |
| σ | `\sigma` | τ | `\tau` |
| ω | `\omega` | π | `\pi` |

### 上下标和修饰

| 效果 | LaTeX |
|------|-------|
| x² | `x^2` |
| xᵢ | `x_i` |
| ẋ | `\dot{x}` |
| x̄ | `\bar{x}` |
| x̂ | `\hat{x}` |
| x̃ | `\tilde{x}` |

### 分数和根号

| 效果 | LaTeX |
|------|-------|
| ½ | `\frac{1}{2}` |
| √2 | `\sqrt{2}` |
| ³√x | `\sqrt[3]{x}` |

### 积分和求和

| 效果 | LaTeX |
|------|-------|
| ∫ | `\int` |
| ∫ₐᵇ | `\int_{a}^{b}` |
| ∑ | `\sum` |
| ∑ᵢ₌₁ⁿ | `\sum_{i=1}^{n}` |
| ∏ | `\prod` |

### 矩阵

```latex
\begin{bmatrix}
    a & b \\
    c & d
\end{bmatrix}
```

### 分段函数

```latex
f(x) = \begin{cases}
    x^2 & x \geq 0 \\
    -x^2 & x < 0
\end{cases}
```

---

## 实用技巧

### 1. 自动编号公式

```latex
\begin{equation}
    E = mc^2
    \label{eq:emc2}
\end{equation}

如公式 \ref{eq:emc2} 所示...
```

### 2. 对齐多行公式

```latex
\begin{align}
    a &= b + c \\
      &= d + e + f \\
      &= g
\end{align}
```

### 3. 插入图片

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figure.png}
    \caption{图片标题}
    \label{fig:example}
\end{figure}
```

### 4. 插入表格

```latex
\begin{table}[htbp]
    \centering
    \caption{表格标题}
    \begin{tabular}{lcc}
        \toprule
        项目 & 数值1 & 数值2 \\
        \midrule
        A & 1.0 & 2.0 \\
        B & 3.0 & 4.0 \\
        \bottomrule
    \end{tabular}
\end{table}
```

### 5. 代码高亮

```latex
\begin{lstlisting}[language=Matlab]
function y = fibonacci(n)
    if n <= 1
        y = n;
    else
        y = fibonacci(n-1) + fibonacci(n-2);
    end
end
\end{lstlisting}
```

---

## 常见问题

### Q1: 中文显示为方块

**解决**: 确保使用 XeLaTeX 编译，并安装中文字体

```bash
sudo apt-get install fonts-wqy-zenhei fonts-wqy-microhei
```

### Q2: 数学公式中的中文

**解决**: 使用 `\text{}` 命令

```latex
$\text{其中} x \in \mathbb{R}$
```

### Q3: 行内公式和中文间距

**解决**: 使用 `\mbox{}` 或调整 ctex 设置

```latex
\ctexset{space=auto}
```

### Q4: 引号显示不正确（只有左引号或右引号）

**问题**: 在LaTeX中直接使用键盘上的直引号 `"` 或 `'` 会导致引号显示不正确。

**解决**: 使用LaTeX专用的引号命令：

| 引号类型 | 左引号 | 右引号 | 示例 |
|---------|--------|--------|------|
| 双引号 | `` (两个反引号) | '' (两个单引号) | ``这是双引号'' |
| 单引号 | ` (一个反引号) | ' (一个单引号) | `这是单引号' |

**错误示例**:
```latex
"AI智能体"          % 错误！显示为两个右引号
'副驾驶'             % 错误！显示为两个右单引号
```

**正确示例**:
```latex
``AI智能体''         % 正确！显示为一对弯引号
`副驾驶'             % 正确！显示为一对弯单引号
```

**批量替换技巧**:
```bash
# 将直双引号替换为LaTeX格式（需要手动检查）
sed -i 's/"\([^"]*\)"/``\1''/g' document.tex

# 检查是否还有遗漏的直引号
grep -n '"' document.tex
```

### Q5: 参考文献中的长URL被截断

**问题**: 在PDF中，参考文献中的长URL（如`https://www.example.com/very/long/path/to/article`）在页面边缘被截断，无法完整显示。

**原因**: LaTeX默认的`\url{}`命令只允许在特定字符（如`.`、`/`）处换行，对于很长的URL或没有这些字符的URL，会导致超出页面边界被截断。

**解决**: 使用`xurl`宏包，它允许URL在任意字符位置自动换行。

**解决方案**:
```latex
% 在导言区添加
\usepackage{xurl}  % 允许URL在任意位置换行

% 使用方式不变
\url{https://www.example.com/very/long/path/to/article}
```

**完整示例**:
```latex
\documentclass{ctexart}
\usepackage{hyperref}
\usepackage{xurl}  % 必须放在hyperref之后

\begin{document}

% 参考文献
\begin{thebibliography}{99}
\bibitem{example} Author. ``Title.'' \url{https://www.example.com/very/long/path/that/will/be/broken/correctly}
\end{thebibliography}

\end{document}
```

**注意事项**:
- `xurl`宏包必须放在`hyperref`之后加载
- 与`breakurl`宏包功能类似，但`xurl`更现代、兼容性更好
- 对于XeLaTeX编译，`xurl`是首选方案

---

## 报告写作最佳实践（2026-03-16更新）

### 从LLM Survey范文中学到的经验

#### 1. 标题层级控制

**原则**: 控制标题层级在3-4层以内，避免过度细分

**推荐结构**:
```
I.   一级标题（Chapter）
    A. 二级标题（Section）
        1) 三级标题（Subsection）- 尽量少用
```

**反例**（避免）:
```
1. 产品概述
    1.1 核心功能
        1.1.1 功能点A
            1.1.1.1 子功能点1
            1.1.1.2 子功能点2
```

#### 2. 叙述 vs 列举的平衡

**原则**: 能用自然语言叙述的，不要用分点列举

**反例**（避免过度列举）:
```latex
该产品具有以下特点：
\begin{itemize}
    \item 特点1：xxx
    \item 特点2：xxx
    \item 特点3：xxx
    \item 特点4：xxx
\end{itemize}
```

**正例**（使用自然语言叙述）:
```latex
该产品在设计上注重用户体验，通过简洁的界面和直观的操作流程，
使用户能够快速上手。其核心优势在于高效的处理能力和灵活的
配置选项，能够满足不同场景下的使用需求。
```

**例外情况**（可以使用列举）:
- 数据对比（如产品参数表）
- 步骤说明（如安装步骤）
- 分类清单（如功能模块列表）
- 每个小点后都有清晰解释或总结

#### 3. 段落组织技巧

**一个段落一个主题**:
```latex
% 好的例子
LLMs have drawn a lot of attention due to their strong performance 
on a wide range of natural language tasks. Their ability of 
general-purpose language understanding and generation is acquired 
by training billions of model's parameters on massive amounts of 
text data, as predicted by scaling laws.

% 不好的例子（多个主题混杂）
LLMs性能很好。它们可以用于NLP任务。训练需要大量数据。
GPT-4是一个例子。还有很多其他模型。
```

**段落之间的逻辑连接**:
```latex
% 使用过渡句
... This opens the door to computing semantic similarity of any 
two inputs regardless their forms.

% 下一段承接
Building upon this capability, recent work has focused on 
extending these models to handle more complex tasks...
```

#### 4. 图表使用原则

**原则**: 图表服务于叙述，不是装饰

**推荐做法**:
- 复杂概念用图说明（如架构图、流程图）
- 数据对比用表格
- 每个图表都要有清晰的标题和说明
- 正文中引用图表（如"如图1所示"）

#### 5. 写作风格建议

**学术风格**（如LLM Survey）:
- 客观、严谨、简洁
- 使用被动语态（如"is developed"而非"we develop"）
- 避免口语化表达
- 专业术语首次出现时解释

**商业报告风格**:
- 清晰、直接、有说服力
- 可以使用主动语态
- 适当使用项目符号（但不要过度）
- 强调关键发现和洞察

#### 6. 常见错误检查清单

- [ ] 标题层级是否过深（>3层）
- [ ] 是否存在连续多个只有列举的段落
- [ ] 每个段落是否有明确的主题句
- [ ] 段落之间是否有逻辑过渡
- [ ] 图表是否都有引用和说明
- [ ] 专业术语是否都有解释
- [ ] 是否存在过长的列举（>5项）

---

## 工作流示例

### 撰写技术报告

1. 创建 `.tex` 文件
2. 使用 TeXstudio 编辑
3. 按 F5 或 F6 编译（自动选择 XeLaTeX）
4. 查看 PDF 输出
5. 迭代修改

### 命令行工作流

```bash
# 创建项目目录
mkdir ~/latex_project && cd ~/latex_project

# 创建主文件
cat > main.tex << 'EOF'
\documentclass[UTF8]{ctexart}
\usepackage{amsmath}
\begin{document}
你好，LaTeX！
\end{document}
EOF

# 编译
xelatex main.tex

# 查看
xdg-open main.pdf
```

---

## 参考资源

- **ctex 宏包文档**: `texdoc ctex`
- **LaTeX 数学符号**: `texdoc symbols-a4`
- **在线教程**: https://www.overleaf.com/learn

---

## 经验教训 (2026-03-16)

### 引号问题排查记录

**问题描述**: 在生成《AI智能体市场调研与宣发策略分析报告》PDF时，发现文档中的引号显示不正确——所有引号都显示为右引号（"），而不是成对的左右引号。

**根本原因**: 
- LaTeX中直接使用键盘输入的直引号 `"` 和 `'` 会被解释为特殊字符
- 直双引号 `"` 在LaTeX中等价于两个右双引号
- 直单引号 `'` 在LaTeX中等价于右单引号

**解决方案**:
1. 双引号: 使用 `` ``内容'' `` 格式（两个反引号 + 内容 + 两个单引号）
2. 单引号: 使用 `` `内容' `` 格式（一个反引号 + 内容 + 一个单引号）

**检查方法**:
```bash
# 查找所有直双引号
grep -n '"' document.tex

# 查找所有直单引号（排除转义符和已有格式）
grep -n "'" document.tex | grep -v "\\'" | grep -v "'.*'"
```

### 长URL截断问题排查记录

**问题描述**: 在生成《AI智能体市场调研与宣发策略分析报告》PDF时，发现参考文献中的长URL（如`https://www.indiatoday.in/jobs/story/...`）在页面边缘被截断，无法完整显示。

**根本原因**: 
- LaTeX默认的`\url{}`命令只允许在特定字符（如`.`、`/`）处换行
- 对于很长的URL或没有这些字符的URL，会导致超出页面边界被截断

**解决方案**:
添加`xurl`宏包，它允许URL在任意字符位置自动换行：
```latex
\usepackage{xurl}  % 必须放在hyperref之后
```

**注意事项**:
- `xurl`宏包必须放在`hyperref`之后加载
- 与`breakurl`宏包功能类似，但`xurl`更现代、兼容性更好
- 对于XeLaTeX编译，`xurl`是首选方案

### 报告写作结构问题

**问题描述**: 初版报告存在标题层级过深、过度使用分点列举的问题，不符合人类阅读偏好。

**根本原因**:
- 过度追求结构清晰，导致碎片化
- 缺乏叙述性内容，信息密度低
- 没有区分"需要列举"和"可以叙述"的场景

**解决方案**（从LLM Survey范文学习）:
1. **控制标题层级**: 最多3层（Chapter > Section > Subsection）
2. **叙述为主，列举为辅**: 能用自然语言说明的，不要用 bullet points
3. **段落完整性**: 每个段落一个主题，有主题句和支撑句
4. **逻辑连贯**: 段落之间使用过渡句连接
5. **图表服务叙述**: 图表不是装饰，而是复杂概念的可视化

**检查清单**:
- [ ] 标题层级是否过深（>3层）
- [ ] 是否存在连续多个只有列举的段落
- [ ] 每个段落是否有明确的主题句
- [ ] 段落之间是否有逻辑过渡
- [ ] 图表是否都有引用和说明

---

## 调研报告内容审核机制（2026-03-16）

### 背景

在《AI智能体市场调研与宣发策略分析报告》的撰写过程中，出现了严重的调研错误：
- **Manus AI**被错误分类为"低技术·低认知"，实际上Meta以20亿美元收购，已成为主流企业级产品
- **OpenClaw**被错误分类为"高技术·低认知"，实际上已达到25万GitHub星标，成为现象级产品

这些错误暴露了调研流程中的系统性问题，需要建立严格的内容审核机制。

### 四层内容审核机制

#### 第一层：信息收集审核

**目标**: 确保信息源的可靠性和时效性

**检查项**:
- [ ] **多源验证**: 关键事实至少3个独立来源确认
- [ ] **时效性检查**: 确认信息发布时间，优先使用近3个月数据
- [ ] **来源可信度排序**: 学术论文 > 官方博客 > 权威媒体 > 社交媒体
- [ ] **数据更新**: 检查是否有更新的数据推翻旧结论

**工具**:
```bash
# 检查信息时效性
grep -n "202[0-9]" document.md  # 查找日期引用
# 交叉验证关键数据
diff <(cat source1.txt) <(cat source2.txt)
```

#### 第二层：数据分析审核

**目标**: 确保分析框架与实际数据匹配

**检查项**:
- [ ] **量化指标**: 技术成熟度、市场认知度需有客观衡量标准
- [ ] **交叉验证**: 不同来源的数据是否一致（误差<10%）
- [ ] **趋势判断**: 避免静态分析，关注动态变化（时间序列）
- [ ] **边界明确**: 结论的适用范围是否清晰（时间、地域、场景）

**常见错误**:
- 用发布时的状态判断产品，忽视动态演进
- 强行套用分析框架（如矩阵模型），忽视实际表现
- 静态分类，未考虑产品发展阶段变化

#### 第三层：结论推导审核

**目标**: 确保结论与数据支撑逻辑一致

**检查项**:
- [ ] **逻辑一致性**: 结论是否与数据支撑匹配
- [ ] **反例检查**: 是否存在与结论矛盾的案例
- [ ] **因果推断**: 相关性不等于因果性
- [ ] **样本偏差**: 是否过度依赖特定群体数据

**反例挑战法**:
对每个关键结论，主动寻找反例：
- "Manus是低认知产品" → 反例：Meta 20亿美元收购
- "OpenClaw是低认知产品" → 反例：25万GitHub星标

#### 第四层：质量检查清单

**发布前最终检查**:

**数据准确性**:
- [ ] 关键数据是否有引用（时间、金额、数量）
- [ ] 敏感数据是否核实（如"20亿美元"需多源确认）
- [ ] 百分比数据是否标明基数（如"72%企业"需说明样本量）

**逻辑一致性**:
- [ ] 图表与文字是否一致
- [ ] 前后文数据是否矛盾
- [ ] 分类标准是否统一

**时效性**:
- [ ] 关键数据是否为最新（6个月内）
- [ ] 快速变化领域（如AI）是否标注数据截止日期
- [ ] 历史数据是否过时（需更新或删除）

### 调研工作流优化

```
┌─────────────────────────────────────────────────────────────┐
│                    高质量调研工作流 v2.0                      │
└─────────────────────────────────────────────────────────────┘

阶段一：需求定义（10%时间）
├── 明确研究问题（Research Questions）
├── 界定研究范围与边界
├── 制定信息收集清单
└── 设定数据截止日期

阶段二：深度调研（40%时间）
├── 学术文献检索（arXiv、Google Scholar）
├── 官方技术文档（白皮书、GitHub）
├── 行业报告（Gartner、CB Insights）
├── 新闻与媒体（TechCrunch、VentureBeat）
└── 【审核点】多源验证关键数据

阶段三：分析整合（30%时间）
├── 建立分类体系
├── 提取关键数据
├── 识别模式与趋势
├── 【审核点】反例挑战关键结论
└── 制作图表与可视化

阶段四：撰写审核（20%时间）
├── 初稿撰写
├── 【审核点】四层内容审核
├── 图表优化
├── 引用核实
└── 终稿定稿
```

### 关键教训

#### 1. 避免静态思维

**错误**: 用发布时的状态判断产品，忽视动态演进  
**案例**: Manus从"饥饿营销"（2025.3）到"20亿美元收购"（2025.12）仅9个月  
**改进**: 建立产品时间线，标注关键里程碑，定期更新

#### 2. 避免框架僵化

**错误**: 强行套用分析框架，忽视实际表现  
**案例**: 强行将Manus/OpenClaw放入"低认知"象限，与GitHub星标、收购数据矛盾  
**改进**: 框架服务于分析，而非限制分析；数据与框架冲突时，优先相信数据

#### 3. 避免数据滞后

**错误**: 使用过时数据支撑当前结论  
**案例**: 使用2025年初的GitHub星标数据，忽视2026年3月已达25万星标  
**改进**: 设定数据截止日期，快速变化领域每周更新

#### 4. 避免主观臆断

**错误**: 对"技术成熟度"和"市场认知度"缺乏客观标准  
**案例**: 主观判断"低认知"，未使用GitHub星标、媒体曝光、收购金额等量化指标  
**改进**: 建立量化评估体系，如：
- 市场认知度 = GitHub Stars × 0.3 + 媒体曝光 × 0.4 + 企业采用 × 0.3
- 技术成熟度 = 功能完整度 × 0.4 + 性能基准 × 0.3 + 企业部署案例 × 0.3

### 质量检查工具

**自动化检查脚本**:
```bash
#!/bin/bash
# 调研报告质量检查脚本

echo "=== 数据时效性检查 ==="
grep -n "202[0-9]" report.md | head -20

echo "=== 关键数据引用检查 ==="
grep -n "亿美元\|万\|百分比" report.md | head -20

echo "=== 未引用声明检查 ==="
grep -n "显然\|明显\|众所周知" report.md

echo "=== 图表引用检查 ==="
grep -n "如图\|见表" report.md
```

**人工审核表**:
| 审核项 | 审核人 | 状态 | 备注 |
|--------|--------|------|------|
| 多源验证 | | | |
| 时效性检查 | | | |
| 逻辑一致性 | | | |
| 反例挑战 | | | |
| 图表准确性 | | | |

### 文档合并与交叉引用问题

**问题描述**: 在合并多个LaTeX文件片段时，文档在第1章后意外结束，后续所有章节被截断，导致PDF只有5页而非完整的34页。

**根本原因**:
1. 文件合并时，第1章末尾遗留了错误的 `\end{document}` 命令
2. 参考文献末尾的 `\end{document}` 位置不当，导致内容截断

**解决方案**:
1. 删除中间错误的 `\end{document}`，只在文档真正末尾保留一个
2. 确保参考文献完整，不被截断
3. 重新编译3次以确保交叉引用正确

**检查方法**:
```bash
# 检查文档中是否有多个 \end{document}
grep -n "end{document}" document.tex

# 应该只在最后一行出现一次
```

### 交叉引用失效问题

**问题描述**: 编译后的PDF中，交叉引用显示为"??"或页码不正确。

**根本原因**:
LaTeX的交叉引用需要多次编译才能解析：
- 第1次编译：收集引用标签信息，写入.aux文件
- 第2次编译：读取.aux文件，解析引用
- 第3次编译：确保所有引用稳定

**解决方案**:
```bash
# 完整编译流程
xelatex document.tex
xelatex document.tex  # 第2次，解析引用
xelatex document.tex  # 第3次，确保稳定

# 或使用 latexmk 自动处理
latexmk -xelatex document.tex
```

**预防措施**:
- 每次修改结构后（添加章节、公式、图表），至少编译2次
- 使用 `\label{}` 后立即检查对应的 `\ref{}` 是否正确
- 定期清理辅助文件（.aux, .log, .toc）后重新编译

### 参考文献交叉引用失效问题

**问题描述**: 使用 `\cite{label}` 命令时，编译报错 "Citation `label' on page X undefined"，PDF中显示为"[?]"或"[0]"。

**根本原因**:
文档使用了手动的 `enumerate` 环境来编写参考文献列表，而不是标准的 `thebibliography` 环境。`\cite` 命令需要与 `\bibitem` 命令配合使用。

**错误示例**:
```latex
% 错误！使用 enumerate 环境无法与 \cite 配合
\begin{enumerate}[label={[\arabic*]}]
    \item Smith, O. J. M. A controller to overcome dead time...
\end{enumerate}

% 正文中使用
Smith预估器由Smith~\cite{smith1959controller}于1959年提出。
% 结果：[?] 或编译报错
```

**正确示例**:
```latex
% 正确！使用 thebibliography 环境
\begin{thebibliography}{99}

\bibitem{smith1959controller}
Smith, O. J. M. A controller to overcome dead time. \textit{ISA Journal}, 1959, 6(2): 28-33.

\bibitem{richard2003time}
Richard, J. P. Time-delay systems: an overview... \textit{Automatica}, 2003, 39(10): 1667-1694.

\end{thebibliography}

% 正文中使用
Smith预估器由Smith~\cite{smith1959controller}于1959年提出。
% 结果：[1]
```

**完整示例**:
```latex
\documentclass{ctexart}
\usepackage{hyperref}

\begin{document}

Smith预估器是处理时滞系统的经典方法~\cite{smith1959controller}。

\begin{thebibliography}{99}

\bibitem{smith1959controller}
Smith, O. J. M. A controller to overcome dead time. \textit{ISA Journal}, 1959, 6(2): 28-33.

\end{thebibliography}

\end{document}
```

**检查方法**:
```bash
# 检查是否有 \bibitem 定义
grep -n "bibitem" document.aux

# 应该显示类似：
# \bibcite{smith1959controller}{1}

# 如果没有，说明引用未定义
```

**编译流程**:
```bash
# 修改参考文献后需要编译2次
xelatex document.tex
xelatex document.tex
```

**最佳实践**:
- 使用 `thebibliography` 环境而非 `enumerate` 环境
- 每个 `\bibitem` 必须有一个唯一的标签（如 `smith1959controller`）
- 标签命名规范：`作者姓氏年份关键词`，如 `gu2003stability`
- 使用 `~\cite{}` 在引用前加非断行空格，防止引用编号孤立在行首

### 综述文档排版最佳实践（2026-03-18）

#### 1. 避免孤立列举形式

**反例**（避免连续分行但只有孤立一句的列举）:
```latex
% 不好的例子 - 碎片化严重，阅读体验差
\textbf{（1）特点A}：描述A。

\textbf{（2）特点B}：描述B。

\textbf{（3）特点C}：描述C。
```

**正例**（优先使用表格）:
```latex
\begin{table}[htbp]
\centering
\caption{方法对比}\label{tab:comparison}
\begin{tabular}{@{}p{3cm}p{4cm}p{5cm}@{}}
\toprule
\textbf{方法} & \textbf{优点} & \textbf{适用场景} \\
\midrule
方法A & 计算效率高 & 实时性要求高的场景 \\
方法B & 精度高 & 精度要求高的场景 \\
方法C & 鲁棒性强 & 噪声环境 \\
\bottomrule
\end{tabular}
\end{table}
```

**正例**（使用连续分行+解释性文字）:
```latex
该方法具有以下特点：首先，计算效率高，能够在毫秒级完成计算；
其次，对噪声具有较好的鲁棒性，在低信噪比条件下仍能保持稳定性能；
最后，实现简单，不需要复杂的参数调优，适合工程部署。
```

#### 2. 叙述 vs 列举的决策树

```
是否需要列举？
├── 是数据对比？→ 使用表格
├── 是步骤说明？→ 使用有序列表（enumerate）
├── 是分类清单？→ 使用无序列表（itemize）
├── 每个点都有详细解释？→ 可以使用列表
└── 否 → 使用自然语言叙述
```

#### 3. 章节结构优化

**原则**: 控制标题层级在3层以内

**推荐结构**:
```
第1章 引言
  1.1 研究背景
  1.2 问题定义
第2章 核心技术
  2.1 技术A
    2.1.1 基本原理  % 最深层级
    2.1.2 实现方法
  2.2 技术B
第3章 结论
```

**避免**:
```
第2章 技术
  2.1 子技术
    2.1.1 子子技术
      2.1.1.1 子子子技术  % 层级过深！
```

#### 4. AI生成图片嵌入规范（2026-03-18）

**Seedream AI配图最佳实践**:

生成后处理（去除灰底）:
```python
from PIL import Image
import numpy as np

def clean_ai_background(input_path, output_path, threshold=235):
    """去除AI生成图片的灰底，转为纯白背景"""
    img = Image.open(input_path).convert('RGB')
    data = np.array(img)
    gray = np.mean(data, axis=2)
    mask = gray > threshold
    data[mask] = [255, 255, 255]
    Image.fromarray(data).save(output_path, quality=95)
```

LaTeX嵌入尺寸控制:
```latex
% 避免图片过大，控制宽度在85%以内
\includegraphics[width=0.85\textwidth]{figure.jpg}

% 或者设置最大高度
\includegraphics[width=0.85\textwidth, height=0.6\textheight, keepaspectratio]{figure.jpg}
```

常见问题:
- **灰底问题**: AI生成图片常有灰色背景，需后处理转为纯白
- **尺寸过大**: 使用 `width=0.85\textwidth` 而非 `scale=1.0`
- **概念不准确**: 复杂概念（如时滞现象）建议用TikZ手绘

完整工作流:
1. 用Seedream生成图片（2048x2048，指定"纯白背景"）
2. Python后处理去除灰底
3. LaTeX中控制嵌入尺寸（width=0.85\textwidth）
4. 编译并检查效果

详细指南: `~/clawd/skills/seedream-image-generation/SKILL.md`

#### 5. 综述文档专用排版规范

**数学公式**:
- 重要公式使用 `\begin{equation}` 编号
- 多行对齐使用 `\begin{align}`
- 行内公式使用 `$...$`

**图表**:
- 每个图表必须有 `\caption` 和 `\label`
- 正文中必须引用（如"如表~\ref{tab:comparison}所示"）
- 表格使用 `booktabs` 宏包的 `\toprule`, `\midrule`, `\bottomrule`

**引用格式**:
- 章节引用：第~\ref{sec:introduction}~节
- 公式引用：式~\eqref{eq:emc2}
- 图表引用：图~\ref{fig:example}，表~\ref{tab:comparison}
- 注意：在引用前加波浪号 `~` 防止换行

**参考文献**:
- 使用 `thebibliography` 环境或 BibTeX/BibLaTeX
- 每条引用必须包含：作者、标题、期刊/会议、年份
- URL使用 `\url{}` 命令，并加载 `xurl` 宏包

### 6. AI生成图片背景问题（2026-03-19更新）

**问题描述**: 使用Seedream等AI生图工具生成的图片默认带有灰色背景，直接嵌入LaTeX文档会显得突兀，与纯白页面不协调。

**根本原因**:
- AI生图模型默认生成带纹理/渐变背景的图片
- 灰色背景（RGB约200-220）在白色页面上形成明显边界
- 未在prompt中明确指定"纯白背景"

**解决方案**:

**方案1：Prompt优化（推荐）**
```
生成图片时明确指定：
- "纯白背景" / "white background"
- "透明背景" / "transparent background"
- "无背景" / "no background"
- "纯色背景" / "solid white background"
```

**方案2：后处理（已生成图片）**
```python
from PIL import Image
import numpy as np

def remove_gray_background(input_path, output_path, threshold=240):
    """
    去除AI生成图片的灰底，转为纯白背景
    threshold: 灰度阈值，高于此值的像素转为纯白
    """
    img = Image.open(input_path).convert('RGB')
    data = np.array(img)
    # 计算灰度值
    gray = np.mean(data, axis=2)
    # 将浅灰色区域转为纯白
    mask = gray > threshold
    data[mask] = [255, 255, 255]
    Image.fromarray(data).save(output_path, quality=95)
    print(f"已处理: {output_path}")

# 使用示例
remove_gray_background('ai_generated.png', 'cleaned.png', threshold=240)
```

**方案3：LaTeX层面处理（临时方案）**
```latex
% 使用tikz在图片周围添加白色边框
\begin{tikzpicture}
    \fill[white] (-0.5,-0.5) rectangle (10.5,7.5);
    \node at (5,3.5) {\includegraphics[width=10cm]{figure.png}};
\end{tikzpicture}
```

**最佳实践**:
1. **生成阶段**: 在prompt中明确指定"纯白背景，无纹理"
2. **检查阶段**: 生成后立即检查背景是否为纯白色（RGB 255,255,255）
3. **后处理阶段**: 使用Python脚本批量去除灰底
4. **嵌入阶段**: LaTeX中控制图片尺寸，避免过大

**检查清单**:
- [ ] Prompt中是否包含"纯白背景"指令
- [ ] 生成图片背景是否为纯白色
- [ ] 是否需要后处理去除灰底
- [ ] LaTeX中图片尺寸是否合适（建议width=0.85\textwidth）

---

*技能创建: 北海 🚀*  
*版本: 1.6*  
*最后更新: 2026-03-19*
