# Seedream AI配图技能

**技能名称**: seedream-image-generation  
**创建时间**: 2026-03-18  
**用途**: 使用Seedream AI生成学术论文配图（框图、架构图、流程图）

---

## 工具介绍

**Seedream** 是字节跳动旗下的AI图像生成模型，支持中文提示词，适合生成学术论文风格的配图。

**当前可用模型**:
- `seedream-5-0-lite` - 轻量级模型，响应快，适合框图/架构图
- `seedream-5-0` - 完整版模型，质量更高，适合复杂场景

---

## 安装与配置

### 1. 安装Seedream CLI工具

```bash
# 通过npm安装（假设已配置）
npm install -g seedream-cli

# 或通过Python pip
pip install seedream
```

### 2. 配置API密钥

```bash
# 设置环境变量
export SEEDREAM_API_KEY="your_api_key"

# 或在配置文件中设置
seedream config set api_key your_api_key
```

---

## 使用方法

### 基础命令

```bash
# 生成单张图片
seedream generate "提示词" --model seedream-5-0-lite

# 指定输出路径
seedream generate "提示词" -o output.jpg

# 设置图片尺寸
seedream generate "提示词" --width 2048 --height 2048
```

### Python API调用

```python
import seedream

client = seedream.Client(api_key="your_api_key")

response = client.generate(
    prompt="专业学术论文框图，控制系统架构...",
    model="seedream-5-0-lite",
    width=2048,
    height=2048
)

# 保存图片
with open("output.jpg", "wb") as f:
    f.write(response.image_data)
```

---

## 学术论文配图最佳实践

### 1. 提示词工程

#### 核心要素

**必须包含的要素**:
1. **风格描述**: "学术论文风格", "技术白皮书", "IEEE期刊配图"
2. **类型说明**: "框图", "架构图", "流程图", "系统图"
3. **配色方案**: "蓝灰配色", "科技蓝", "专业简洁"
4. **背景要求**: "纯白背景", "无水印", "高清"
5. **分辨率**: "2048x2048", "高清", "矢量风格"

#### 提示词模板

**系统架构图**:
```
专业学术论文框图，无人机通信系统架构图，三层架构设计，
顶层地面控制站，中间层5G/6G通信网络，底层UAV无人机系统，
模块间用箭头连接，蓝灰配色，科技风格，纯白背景，
标注清晰，2048x2048高清分辨率，IEEE期刊配图风格
```

**分类树状图**:
```
学术论文方法分类树状图，三层树状结构，根节点在顶部，
子节点分层展开，矩形模块带圆角，模块间用连接线，
不同分支用不同颜色区分，蓝/绿/橙配色，纯白背景，
2048x2048高清，专业科技风格
```

**控制框图**:
```
经典控制理论框图，反馈控制系统，包含控制器C(s)、
被控对象G(s)、反馈回路，信号流用箭头表示，
简洁黑白配色或蓝灰配色，纯白背景，
2048x2048高清，适合Automatica期刊
```

### 2. 常见问题与解决方案

#### 问题1: 图片有灰底/暗底

**症状**: 生成的图片背景不是纯白，而是灰色或暗色

**原因**: Seedream默认生成带渐变或纹理的背景

**解决方案**:
1. 在提示词中明确指定 **"纯白背景"** 或 **"纯白色背景，无渐变"**
2. 使用后期处理去除灰底（Python PIL）:

```python
from PIL import Image
import numpy as np

def remove_gray_background(image_path, output_path, threshold=240):
    """
    去除图片灰底，将接近白色的背景转为纯白色
    
    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        threshold: 阈值，低于此值的像素视为前景
    """
    img = Image.open(image_path).convert('RGB')
    data = np.array(img)
    
    # 创建掩码：亮度高于阈值的像素设为纯白
    gray = np.mean(data, axis=2)
    mask = gray > threshold
    data[mask] = [255, 255, 255]
    
    result = Image.fromarray(data)
    result.save(output_path, quality=95)
    return output_path

# 使用示例
remove_gray_background('input.jpg', 'output_clean.jpg', threshold=235)
```

#### 问题2: 图片嵌入LaTeX后过大

**症状**: 图片在PDF中占据整个页面或过大

**解决方案**:
1. **调整LaTeX中的图片尺寸**:
```latex
% 使用 width 控制宽度，而非 scale
\includegraphics[width=0.85\textwidth]{figure.jpg}

% 或者设置最大高度
\includegraphics[width=0.85\textwidth, height=0.6\textheight, keepaspectratio]{figure.jpg}
```

2. **使用 figure 环境控制位置**:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{figure.jpg}
    \caption{图片标题}
    \label{fig:label}
\end{figure}
```

3. **多图并排**（如果需要）:
```latex
\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{fig1.jpg}
        \caption{子图1}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{fig2.jpg}
        \caption{子图2}
    \end{subfigure}
    \caption{总标题}
\end{figure}
```

#### 问题3: 概念表达不准确

**症状**: AI生成的框图与预期概念不符（如时滞现象表现不好）

**原因**: 提示词中概念描述不够具体或存在歧义

**解决方案**:
1. **使用更具体的技术术语**:
   - ❌ "时间延迟效果"
   - ✅ "信号传输时滞，输入信号与输出信号之间的时间差Δt"

2. **提供视觉参考描述**:
```
时滞现象示意图：左侧输入信号r(t)，经过延迟环节e^(-τs)，
右侧输出信号y(t) = r(t-τ)，信号波形相同但右移τ时间，
用双向箭头标注时间差τ，数学公式标注
```

3. **分步生成复杂图**:
   - 先生成基础框架
   - 再添加细节元素
   - 最后合成

#### 问题4: 文字模糊或乱码

**症状**: 生成的图片中文字模糊、无法识别或乱码

**原因**: AI生成图片中的文字渲染不稳定

**解决方案**:
1. **减少文字量**: 让AI生成图形框架，文字用LaTeX/TikZ后期添加
2. **使用编号系统**: AI生成带编号的模块，文字说明在LaTeX中添加
3. **提高分辨率**: 使用2048x2048或更高分辨率

---

## 完整工作流示例

### 场景: 生成控制系统框图并嵌入LaTeX

#### Step 1: 生成图片

```bash
# 生成系统架构图
seedream generate \
  "专业学术论文框图，无人机通信时延管理系统架构，三层架构，
   顶层地面控制站GCS带天线图标，中间层5G通信网络带信号塔，
   底层多架无人机UAV，模块间用箭头连接，数据流向清晰，
   蓝灰配色，科技风格，纯白背景，2048x2048高清" \
  --model seedream-5-0-lite \
  --width 2048 \
  --height 2048 \
  -o fig_arch_raw.jpg
```

#### Step 2: 后处理（去除灰底）

```python
# clean_image.py
from PIL import Image
import numpy as np

def clean_background(input_path, output_path):
    img = Image.open(input_path).convert('RGB')
    data = np.array(img)
    
    # 将接近白色的背景转为纯白
    gray = np.mean(data, axis=2)
    mask = gray > 235
    data[mask] = [255, 255, 255]
    
    Image.fromarray(data).save(output_path, quality=95)

if __name__ == "__main__":
    clean_background('fig_arch_raw.jpg', 'fig_arch.jpg')
```

```bash
python clean_image.py
```

#### Step 3: 嵌入LaTeX

```latex
\documentclass[UTF8]{ctexart}
\usepackage{graphicx}
\usepackage{caption}

\begin{document}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.85\textwidth]{fig_arch.jpg}
    \caption{无人机通信时延管理系统架构}
    \label{fig:architecture}
\end{figure}

如图~\ref{fig:architecture}所示，系统采用三层架构设计...

\end{document}
```

#### Step 4: 编译

```bash
xelatex document.tex
xelatex document.tex  # 编译两次确保引用正确
```

---

## 批量生成脚本

```bash
#!/bin/bash
# generate_figures.sh - 批量生成论文配图

MODEL="seedream-5-0-lite"
SIZE="2048"

# 定义提示词数组
declare -A prompts
declare -A outputs

prompts[arch]="专业学术论文框图，无人机通信系统架构，三层架构，蓝灰配色，纯白背景，2048x2048"
prompts[delay]="学术论文时滞辨识方法分类图，树状结构，三大分支，蓝绿橙配色，纯白背景，2048x2048"
prompts[smith]="经典控制理论框图，Smith预估器结构，反馈回路，简洁配色，纯白背景，2048x2048"
prompts[comp]="控制方法分类体系图，四大类方法，多色区分，层次清晰，纯白背景，2048x2048"

outputs[arch]="fig_arch"
outputs[delay]="fig_delay"
outputs[smith]="fig_smith"
outputs[comp]="fig_comp"

# 生成图片
for key in "${!prompts[@]}"; do
    echo "Generating ${outputs[$key]}..."
    seedream generate "${prompts[$key]}" \
        --model $MODEL \
        --width $SIZE \
        --height $SIZE \
        -o "${outputs[$key]}_raw.jpg"
    
    # 后处理
    python clean_image.py "${outputs[$key]}_raw.jpg" "${outputs[$key]}.jpg"
done

echo "All figures generated!"
```

---

## 质量检查清单

生成图片后，检查以下项目：

- [ ] **背景**: 是否为纯白？（RGB: 255,255,255）
- [ ] **清晰度**: 文字和线条是否清晰？
- [ ] **配色**: 是否符合学术风格？（避免过于鲜艳）
- [ ] **概念**: 是否准确表达预期概念？
- [ ] **分辨率**: 是否达到2048x2048或更高？
- [ ] **水印**: 是否包含AI生成水印？（需要去除）
- [ ] **嵌入效果**: 在LaTeX中预览，尺寸是否合适？

---

## 经验教训（2026-03-18）

### Seedream生成学术配图的优缺点

**优点**:
- 中文提示词理解准确
- 生成速度快（lite模型）
- 学术风格把握较好
- 2048x2048分辨率足够清晰

**缺点**:
- 默认有灰底，需要后处理
- 复杂概念（如时滞现象）表现不稳定
- 文字渲染可能模糊
- 需要精确的提示词工程

### 最佳实践总结

1. **提示词必须包含**: 风格 + 类型 + 配色 + 背景 + 分辨率
2. **后处理必备**: 去除灰底，调整对比度
3. **LaTeX嵌入**: 使用 `width=0.85\textwidth` 控制尺寸
4. **概念验证**: 生成后人工检查概念准确性
5. **备用方案**: 复杂图用TikZ手绘，简单图用Seedream生成

### 与TikZ的对比

| 特性 | Seedream AI | TikZ手绘 |
|------|-------------|----------|
| 生成速度 | 快（秒级） | 慢（需编写代码） |
| 视觉质量 | 高（拟真） | 中（矢量） |
| 概念准确性 | 依赖提示词 | 完全可控 |
| 修改灵活性 | 低（需重新生成） | 高（改代码即可） |
| 学习成本 | 低 | 高 |
| 适用场景 | 简单框图、架构图 | 复杂公式、精确控制 |

**建议**: 简单架构图用Seedream快速生成，复杂控制框图用TikZ精确绘制。

---

## 参考资源

- Seedream官方文档: https://seedream.volces.com
- LaTeX图片插入指南: `texdoc graphicx`
- TikZ绘图教程: `texdoc tikz`

---

*技能创建: 北海 🚀*  
*版本: 1.0*  
*最后更新: 2026-03-18*
