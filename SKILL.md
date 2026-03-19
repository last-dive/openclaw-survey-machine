# 综述永动机 (Survey Machine) v1.0

**名称**: openclaw-survey-machine  
**版本**: 1.0.0  
**作者**: 综述永动机  
**描述**: 一键生成高质量学术综述的完整工作流

---

## 快速开始

### 自然语言触发

```
帮我写一篇关于[主题]的综述
```

### 命令行使用

```bash
cd ~/clawd/skills/survey-machine
./survey-machine.sh "无人机通信时延"
```

---

## 系统架构

```
survey-machine/
├── core/                      # 核心模块
│   ├── survey-writer/        # 内容撰写
│   ├── survey-expander/      # 内容扩展
│   └── survey-evolution/     # 质量进化
├── tools/                     # 工具模块
│   ├── latex-typesetting/    # LaTeX排版
│   ├── diagram-generation/   # 框图生成
│   ├── seedream-poster/      # AI海报
│   └── serpapi-search/       # 文献检索
├── config/                    # 配置文件
├── examples/                  # 使用示例
└── utils/                     # 工具函数
```

---

## 工作流程

1. **需求解析** - 理解用户主题和子主题
2. **文献调研** - SerpAPI检索100+文献
3. **框架构建** - 生成7章标准结构
4. **内容撰写** - survey-writer生成深度内容
5. **可视化** - TikZ框图 + Seedream海报
6. **质量进化** - survey-evolution检查优化
7. **成品交付** - 编译PDF，质量报告

---

## 配置

编辑 `config/config.yaml`:

```yaml
apis:
  serpapi:
    key: "YOUR_KEY"
  seedream:
    key: "YOUR_KEY"

defaults:
  pages: 50
  papers: 100
  target_score: 95
```

---

## 安装

```bash
./install.sh
./verify.sh
```

---

*综述永动机 - 让学术写作不再是负担*
