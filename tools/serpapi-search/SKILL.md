# SerpAPI 文献检索工具

## 功能
- Google Scholar 学术检索
- arXiv 论文检索
- IEEE Xplore 检索
- 智能去重和质量筛选

## 配置
在 config/config.yaml 中设置 SerpAPI key

## 使用
```python
from serpapi_search import ScholarSearcher

searcher = ScholarSearcher(api_key="your_key")
papers = searcher.search("无人机通信时延", num_results=100)
```
