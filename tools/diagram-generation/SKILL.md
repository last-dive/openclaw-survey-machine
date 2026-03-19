# 框图生成工具

## 功能
- TikZ 框图自动生成
- 方法分类框架图
- 系统架构图
- 技术路线图

## 使用
```python
from diagram_generator import TikZGenerator

gen = TikZGenerator()
gen.create_framework_diagram(categories=["方法A", "方法B", "方法C"])
```
