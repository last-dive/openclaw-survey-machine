# 失败案例库
# 基于UAV_Delay_Survey_v3迭代经验

## 案例1: 文档截断

**级别**: 🔴 严重
**频率**: 高
**影响**: 内容丢失，无法使用

### 现象
生成的PDF只有5页，明显不完整。

### 根因
```latex
% 第151行
\section{引言}
...
\end{document}  % ← 错误的结束命令

% 第152-1094行 (被忽略)
\section{基础理论}
...
\section{方法A}
...
\end{document}  % ← 正确的结束命令
```

### 规避策略
1. 生成后检查页数 (应>30页)
2. 搜索`\end{document}`确认唯一性
3. 检查章节计数

### 自动检测
```python
def check_truncation(tex_content):
    end_count = tex_content.count('\\end{document}')
    if end_count != 1:
        return False, f"发现{end_count}个\\end{{document}}"
    return True, "OK"
```

---

## 案例2: 引用系统错误

**级别**: 🔴 严重
**频率**: 高
**影响**: 学术不规范，无法投稿

### 现象
正文中出现`[??]`，或引用无链接。

### 根因

**错误做法1**: 手动编号
```latex
Smith预估器[1]是经典方法。  % 手动编号

\begin{enumerate}
\item Smith, O. J. (1957). ...  % enumerate环境
\end{enumerate}
```

**错误做法2**: 使用enumerate
```latex
\begin{enumerate}
\item Smith, O. J. (1957). ...
\item Krstic, M. (2009). ...
\end{enumerate}
```

**正确做法**:
```latex
Smith预估器~\cite{smith1957}是经典方法。

\begin{thebibliography}{99}
\bibitem{smith1957} Smith, O. J. (1957). ...
\bibitem{krstic2009} Krstic, M. (2009). ...
\end{thebibliography}
```

### 规避策略
1. 强制使用`thebibliography`环境
2. 每条文献必须有`\bibitem{标签}`
3. 正文使用`\cite{标签}`引用
4. 编译后搜索`[??]`确认无遗漏

---

## 案例3: 孤立列举

**级别**: 🟡 中等
**频率**: 高
**影响**: 可读性差，显得不专业

### 现象
```latex
(1) 影响飞行稳定性
(2) 降低控制精度
(3) 增加能量消耗
(4) 限制通信距离
```

### 根因
生成时逐句处理，未合并为段落。

### 修复方案

**方案1**: 改为表格 (推荐)
```latex
\begin{table}[htbp]
\centering
\caption{通信时延对无人机系统的主要影响}
\begin{tabular}{@{}ll@{}}
\toprule
\textbf{影响方面} & \textbf{具体表现} \\
\midrule
飞行稳定性 & 时延导致控制指令滞后，影响姿态稳定 \\
控制精度 & 跟踪误差增大，难以精确控制 \\
能量消耗 & 为补偿时延需增加控制量，增加能耗 \\
通信距离 & 时延随距离增加，限制作业范围 \\
\bottomrule
\end{tabular}
\end{table}
```

**方案2**: 改为连续叙述
```latex
通信时延对无人机系统的影响主要体现在四个方面：
首先，时延导致控制指令滞后，影响飞行稳定性；
其次，跟踪误差增大，降低控制精度；
此外，为补偿时延需增加控制量，导致能量消耗增加；
最后，时延随通信距离增加，限制了作业范围。
```

---

## 案例4: 交叉引用换行

**级别**: 🟡 中等
**频率**: 中
**影响**: 排版不美观

### 现象
```
如表
1所示，该方法...
```

### 根因
缺少`~`防止换行。

### 修复
```latex
% 错误
如表\ref{tab:comparison}所示...

% 正确
如表~\ref{tab:comparison}所示...
```

---

## 案例5: TikZ框图重叠

**级别**: 🟡 中等
**频率**: 中
**影响**: 图表不清晰

### 现象
框图节点重叠，连接线错位。

### 根因
使用`matrix`布局，节点数量不一致时错位。

### 修复
使用绝对坐标:
```latex
% 错误 (matrix布局)
\matrix[row sep=1cm, column sep=2cm] {
    \node (a) {A}; & \node (b) {B}; \\
    \node (c) {C}; \\
};

% 正确 (绝对坐标)
\node[block] (a) at (0,0) {A};
\node[block] (b) at (3,0) {B};
\node[block] (c) at (0,-2.5) {C};
```

---

## 案例6: 单句itemize

**级别**: 🟢 轻微
**频率**: 高
**影响**: 内容松散

### 现象
```latex
\begin{itemize}
\item 这是一个要点。
\end{itemize}

\begin{itemize}
\item 这是另一个要点。
\end{itemize}
```

### 修复
合并为段落或改为表格。

---

## 预防检查清单

```markdown
□ 文档结构
  □ 搜索`\end{document}`，确认只有1个
  □ 检查章节数量 (应≥7)
  □ 确认页数>30页

□ 引用系统
  □ 使用`thebibliography`环境
  □ 每条文献有`\bibitem{标签}`
  □ 正文使用`\cite{标签}`
  □ 搜索`[??]`，确认无遗漏

□ 排版格式
  □ 无孤立列举(1)(2)(3)
  □ 交叉引用使用`~\ref{}`
  □ 无单句itemize

□ 图表
  □ TikZ使用绝对坐标
  □ 框图无重叠
  □ 图表数量≥5

□ 编译
  □ 无错误
  □ 无警告
```
