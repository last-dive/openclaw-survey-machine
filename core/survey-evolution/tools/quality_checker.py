#!/usr/bin/env python3
"""
Survey Evolution - 综述质量检查工具
基于 survey-writer v2.1.0 和 survey-expander v1.0.0

使用方法:
    python3 quality_checker.py --input survey.tex --output report.md
"""

import re
import argparse
from datetime import datetime
from pathlib import Path


class SurveyQualityChecker:
    """综述质量检查器"""
    
    def __init__(self, tex_content):
        self.content = tex_content
        self.issues = []
        self.scores = {}
        
    def check_structure_integrity(self):
        """检查结构完整性 (15分)"""
        score = 15
        details = []
        
        # 检查是否有引言
        if not re.search(r'\\section\{[^}]*引言|Introduction', self.content, re.I):
            score -= 5
            details.append("❌ 缺少引言章节 (-5)")
        else:
            details.append("✅ 引言章节存在")
            
        # 检查是否有展望/结论
        if not re.search(r'\\section\{[^}]*展望|未来|结论|Conclusion|Future', self.content, re.I):
            score -= 3
            details.append("❌ 缺少展望/结论章节 (-3)")
        else:
            details.append("✅ 展望/结论章节存在")
            
        # 检查章节数量
        sections = re.findall(r'\\section\{([^}]+)\}', self.content)
        if len(sections) < 5:
            score -= 3
            details.append(f"⚠️ 章节数量较少 ({len(sections)} 章) (-3)")
        else:
            details.append(f"✅ 章节数量充足 ({len(sections)} 章)")
            
        # 检查文档是否完整
        if '\\end{document}' not in self.content:
            score -= 5
            details.append("❌ 文档不完整，缺少 \\end{document} (-5)")
        else:
            details.append("✅ 文档结构完整")
            
        self.scores['structure'] = {'score': max(0, score), 'max': 15, 'details': details}
        return max(0, score)
        
    def check_introduction_quality(self):
        """检查引言质量 (10分)"""
        score = 10
        details = []
        
        # 提取引言部分 - 匹配 "引言" 或 "Introduction" 章节
        intro_match = re.search(r'\\section\{[^}]*(?:引言|Introduction)[^}]*\}(.*?)(?=\\section\{|\\end\{document\}|\Z)', 
                                self.content, re.I | re.DOTALL)
        if not intro_match:
            self.scores['introduction'] = {'score': 0, 'max': 10, 
                                           'details': ["❌ 未找到引言章节"]}
            return 0
            
        intro = intro_match.group(1) or ""
        # 限制检查长度，避免匹配到后续章节
        intro = intro[:5000]  # 只检查前5000字符
        
        # 检查研究背景
        if re.search(r'背景|发展|随着|Background', intro):
            details.append("✅ 包含研究背景")
        else:
            score -= 2
            details.append("⚠️ 研究背景不够清晰 (-2)")
            
        # 检查问题定义
        if re.search(r'问题|挑战|难点|Problem|Challenge', intro):
            details.append("✅ 包含问题定义")
        else:
            score -= 2
            details.append("⚠️ 问题定义不够明确 (-2)")
            
        # 检查贡献说明
        if re.search(r'贡献|Contribution|本文', intro):
            details.append("✅ 包含贡献说明")
        else:
            score -= 2
            details.append("⚠️ 缺少贡献说明 (-2)")
            
        # 检查组织结构
        if re.search(r'结构|组织|Structure|Overview', intro):
            details.append("✅ 包含组织结构")
        else:
            score -= 1
            details.append("⚠️ 缺少组织结构说明 (-1)")
            
        self.scores['introduction'] = {'score': max(0, score), 'max': 10, 'details': details}
        return max(0, score)
        
    def check_classification_framework(self):
        """检查分类框架 (15分)"""
        score = 15
        details = []
        
        # 检查章节层次结构
        sections = re.findall(r'\\section\{([^}]+)\}', self.content)
        subsections = re.findall(r'\\subsection\{([^}]+)\}', self.content)
        
        if len(subsections) >= len(sections) * 2:
            details.append(f"✅ 层次结构良好 ({len(sections)} 章, {len(subsections)} 节)")
        else:
            score -= 3
            details.append(f"⚠️ 层次结构较浅 ({len(sections)} 章, {len(subsections)} 节) (-3)")
            
        # 检查是否有方法分类
        method_sections = [s for s in sections if any(kw in s.lower() for kw in 
                          ['方法', 'method', '技术', 'technique', '算法', 'algorithm'])]
        if len(method_sections) >= 2:
            details.append(f"✅ 方法分类清晰 ({len(method_sections)} 个方法章节)")
        else:
            score -= 3
            details.append("⚠️ 方法分类不够清晰 (-3)")
            
        # 检查是否有对比表格
        tables = len(re.findall(r'\\begin\{table\}', self.content))
        if tables >= 2:
            details.append(f"✅ 包含 {tables} 个表格")
        else:
            score -= 2
            details.append(f"⚠️ 表格数量较少 ({tables} 个) (-2)")
            
        self.scores['framework'] = {'score': max(0, score), 'max': 15, 'details': details}
        return max(0, score)
        
    def check_content_depth(self):
        """检查内容深度 (15分)"""
        score = 15
        details = []
        
        # 检查批判性分析
        critical_patterns = ['优点', '缺点', '优势', '局限', '不足', '挑战', 
                           '然而', '但是', '相比之下', '优于', '劣于',
                           'advantage', 'disadvantage', 'limitation', 'challenge',
                           'however', 'but', 'compared', 'better', 'worse']
        critical_count = sum(len(re.findall(p, self.content, re.I)) for p in critical_patterns)
        
        if critical_count >= 10:
            details.append(f"✅ 批判性分析充足 ({critical_count} 处)")
        else:
            score -= 5
            details.append(f"⚠️ 批判性分析不足 ({critical_count} 处, 建议 >10) (-5)")
            
        # 检查公式数量
        equations = len(re.findall(r'\\begin\{equation\}|\\\[', self.content))
        if equations >= 5:
            details.append(f"✅ 公式数量充足 ({equations} 个)")
        else:
            score -= 2
            details.append(f"⚠️ 公式数量较少 ({equations} 个) (-2)")
            
        # 检查段落长度
        short_sections = re.findall(r'\\subsubsection\{([^}]+)\}[^\\]*?(?=\\subsubsection|\\subsection|\\section|\Z)', 
                                    self.content, re.DOTALL)
        short_count = sum(1 for s in short_sections if len(s) < 300)
        if short_count > 0:
            score -= short_count
            details.append(f"⚠️ 有 {short_count} 个过短的小节 (-{short_count})")
        else:
            details.append("✅ 各小节内容充实")
            
        self.scores['depth'] = {'score': max(0, score), 'max': 15, 'details': details}
        return max(0, score)
        
    def check_citation_system(self):
        """检查引用系统 (15分)"""
        score = 15
        details = []
        
        # 检查是否有参考文献
        if '\\begin{thebibliography}' in self.content or '\\bibliography' in self.content:
            details.append("✅ 参考文献格式正确")
        else:
            score -= 5
            details.append("❌ 缺少参考文献 (-5)")
            
        # 检查是否有 ?? 引用
        undefined_citations = len(re.findall(r'\?\?', self.content))
        if undefined_citations == 0:
            details.append("✅ 无未定义引用")
        else:
            score -= min(10, undefined_citations * 5)
            details.append(f"❌ 有 {undefined_citations} 处未定义引用 (-{min(10, undefined_citations * 5)})")
            
        # 统计引用数量
        citations = len(re.findall(r'\\cite\{[^}]+\}', self.content))
        bibitems = len(re.findall(r'\\bibitem\{[^}]+\}', self.content))
        total_refs = max(citations, bibitems)
        
        # 检查正文交叉引用比例（关键标准：≥50%文献需在正文中有明确交叉引用）
        # 只计算唯一的\cite{}引用（去重）
        unique_cited_refs = set(re.findall(r'\\cite\{([^}]+)\}', self.content))
        
        # 计算实际的交叉引用比例
        cross_ref_ratio = len(unique_cited_refs) / total_refs * 100 if total_refs > 0 else 0
        
        if total_refs >= 30:
            details.append(f"✅ 引用数量充足 ({total_refs} 处)")
        else:
            score -= 2
            details.append(f"⚠️ 引用数量偏少 ({total_refs} 处) (-2)")
        
        # 严格的交叉引用检查（新标准）
        if cross_ref_ratio >= 50:
            details.append(f"✅ 正文交叉引用比例达标 ({cross_ref_ratio:.1f}% ≥ 50%)")
        else:
            score -= 5
            details.append(f"❌ 正文交叉引用比例不足 ({cross_ref_ratio:.1f}% < 50%) (-5)")
            details.append(f"   建议：确保至少50%的参考文献在正文中有明确的\\cite引用")
            
        self.scores['citation'] = {'score': max(0, score), 'max': 15, 'details': details}
        return max(0, score)
        
    def check_figure_quality(self):
        """检查图表质量 (10分)"""
        score = 10
        details = []
        
        # 检查图片数量
        figures = len(re.findall(r'\\begin\{figure\}', self.content))
        if figures >= 3:
            details.append(f"✅ 图片数量充足 ({figures} 张)")
        else:
            score -= 3
            details.append(f"⚠️ 图片数量较少 ({figures} 张) (-3)")
            
        # 检查表格数量
        tables = len(re.findall(r'\\begin\{table\}', self.content))
        if tables >= 3:
            details.append(f"✅ 表格数量充足 ({tables} 个)")
        else:
            score -= 2
            details.append(f"⚠️ 表格数量较少 ({tables} 个) (-2)")
            
        # 检查是否有 TikZ 图
        tikz_count = len(re.findall(r'\\begin\{tikzpicture\}', self.content))
        if tikz_count >= 2:
            details.append(f"✅ 包含 {tikz_count} 个 TikZ 矢量图")
        elif tikz_count == 1:
            details.append("✅ 包含 TikZ 矢量图")
        else:
            score -= 1
            details.append("⚠️ 建议添加 TikZ 矢量图 (-1)")
        
        # 检查框图质量（检查TikZ代码质量）
        tikz_issues = []
        
        # 检查是否有minimum width/height设置（质量指标）
        has_min_width = 'minimum width=' in self.content
        has_min_height = 'minimum height=' in self.content
        
        if has_min_width and has_min_height:
            details.append("✅ TikZ节点设置了最小尺寸，质量良好")
        elif has_min_width or has_min_height:
            details.append("⚠️ TikZ节点部分设置了最小尺寸")
        else:
            tikz_issues.append("TikZ节点未设置minimum width/height")
        
        # 检查node distance是否合理
        if 'node distance=' in self.content:
            distance_matches = re.findall(r'node distance=([\d.]+)cm', self.content)
            small_distances = [d for d in distance_matches if float(d) < 0.5]
            if small_distances:
                tikz_issues.append(f"Node间距较小({min(small_distances)}cm)，建议≥0.5cm")
        
        # 扣分逻辑：只有存在实际问题时才扣分
        if len(tikz_issues) >= 2:
            score -= 3
            details.append(f"⚠️ TikZ图有可改进之处 (-3):")
            for issue in tikz_issues:
                details.append(f"   - {issue}")
        elif len(tikz_issues) == 1:
            score -= 1
            details.append(f"⚠️ {tikz_issues[0]} (-1)")
            
        self.scores['figures'] = {'score': max(0, score), 'max': 10, 'details': details}
        return max(0, score)
        
    def check_formatting(self):
        """检查排版规范 (10分)"""
        score = 10
        details = []
        
        # 检查孤立列举
        isolated_lists = len(re.findall(r'\n\(\d+\)[^\\]', self.content))
        if isolated_lists == 0:
            details.append("✅ 无孤立列举")
        else:
            score -= min(5, isolated_lists * 2)
            details.append(f"⚠️ 有 {isolated_lists} 处孤立列举 (-{min(5, isolated_lists * 2)})")
            
        # 检查交叉引用格式
        correct_refs = len(re.findall(r'(?:图|表|章节|公式|算法)?~?\\ref\{[^}]+\}', self.content))
        if correct_refs >= 10:
            details.append(f"✅ 交叉引用规范 ({correct_refs} 处)")
        else:
            score -= 1
            details.append(f"⚠️ 交叉引用较少 ({correct_refs} 处) (-1)")
            
        # 检查是否有编译警告相关的问题
        if '\\begin{itemize}' in self.content and '\\end{itemize}' in self.content:
            details.append("✅ 列表环境使用正确")
        
        self.scores['formatting'] = {'score': max(0, score), 'max': 10, 'details': details}
        return max(0, score)
        
    def check_future_directions(self):
        """检查未来方向 (10分)"""
        score = 10
        details = []
        
        # 查找展望/未来方向章节
        future_match = re.search(r'\\section\{[^}]*(?:展望|未来|挑战|结论|Conclusion|Future|Challenge)[^}]*\}(.*?)(?=\\section|\Z)', 
                                 self.content, re.I | re.DOTALL)
        if not future_match:
            self.scores['future'] = {'score': 0, 'max': 10, 
                                     'details': ["❌ 未找到展望/结论章节"]}
            return 0
            
        future = future_match.group(1)
        
        # 检查是否有具体方向
        direction_patterns = ['方向', '趋势', '未来', '下一步', '研究', '发展',
                            'direction', 'trend', 'future', 'next', 'research']
        direction_count = sum(len(re.findall(p, future, re.I)) for p in direction_patterns)
        
        if direction_count >= 5:
            details.append(f"✅ 未来方向具体 ({direction_count} 处)")
        else:
            score -= 3
            details.append(f"⚠️ 未来方向不够具体 ({direction_count} 处) (-3)")
            
        # 检查是否有挑战分析
        if re.search(r'挑战|问题|难点|Challenge|Problem|Difficulty', future, re.I):
            details.append("✅ 包含挑战分析")
        else:
            score -= 2
            details.append("⚠️ 缺少挑战分析 (-2)")
            
        self.scores['future'] = {'score': max(0, score), 'max': 10, 'details': details}
        return max(0, score)
        
    def generate_report(self):
        """生成质量报告"""
        total_score = sum(self.scores[s]['score'] for s in self.scores)
        max_score = sum(self.scores[s]['max'] for s in self.scores)
        
        # 确定等级
        percentage = (total_score / max_score) * 100 if max_score > 0 else 0
        if percentage >= 90:
            grade = "A+"
            grade_emoji = "🌟"
        elif percentage >= 80:
            grade = "A"
            grade_emoji = "✅"
        elif percentage >= 70:
            grade = "B+"
            grade_emoji = "⚠️"
        elif percentage >= 60:
            grade = "B"
            grade_emoji = "⚠️"
        else:
            grade = "C"
            grade_emoji = "❌"
            
        report = f"""# 综述质量检查报告

## 基本信息
- 检查日期：{datetime.now().strftime('%Y-%m-%d %H:%M')}
- 检查工具：Survey Evolution v1.0.0
- 总分：{total_score}/{max_score} ({percentage:.1f}%)
- 等级：{grade_emoji} {grade}

## 总体评分

| 维度 | 分值 | 得分 | 状态 |
|------|------|------|------|
| 结构完整性 | 15 | {self.scores['structure']['score']}/15 | {'✅' if self.scores['structure']['score'] >= 12 else '⚠️' if self.scores['structure']['score'] >= 9 else '❌'} |
| 引言质量 | 10 | {self.scores['introduction']['score']}/10 | {'✅' if self.scores['introduction']['score'] >= 8 else '⚠️' if self.scores['introduction']['score'] >= 6 else '❌'} |
| 分类框架 | 15 | {self.scores['framework']['score']}/15 | {'✅' if self.scores['framework']['score'] >= 12 else '⚠️' if self.scores['framework']['score'] >= 9 else '❌'} |
| 内容深度 | 15 | {self.scores['depth']['score']}/15 | {'✅' if self.scores['depth']['score'] >= 12 else '⚠️' if self.scores['depth']['score'] >= 9 else '❌'} |
| 引用系统 | 15 | {self.scores['citation']['score']}/15 | {'✅' if self.scores['citation']['score'] >= 12 else '⚠️' if self.scores['citation']['score'] >= 9 else '❌'} |
| 图表质量 | 10 | {self.scores['figures']['score']}/10 | {'✅' if self.scores['figures']['score'] >= 8 else '⚠️' if self.scores['figures']['score'] >= 6 else '❌'} |
| 排版规范 | 10 | {self.scores['formatting']['score']}/10 | {'✅' if self.scores['formatting']['score'] >= 8 else '⚠️' if self.scores['formatting']['score'] >= 6 else '❌'} |
| 未来方向 | 10 | {self.scores['future']['score']}/10 | {'✅' if self.scores['future']['score'] >= 8 else '⚠️' if self.scores['future']['score'] >= 6 else '❌'} |
| **总分** | **100** | **{total_score}/100** | **{grade}** |

## 详细检查项

### 1. 结构完整性 ({self.scores['structure']['score']}/15)
"""
        for detail in self.scores['structure']['details']:
            report += f"- {detail}\n"
            
        report += f"""
### 2. 引言质量 ({self.scores['introduction']['score']}/10)
"""
        for detail in self.scores['introduction']['details']:
            report += f"- {detail}\n"
            
        report += f"""
### 3. 分类框架 ({self.scores['framework']['score']}/15)
"""
        for detail in self.scores['framework']['details']:
            report += f"- {detail}\n"
            
        report += f"""
### 4. 内容深度 ({self.scores['depth']['score']}/15)
"""
        for detail in self.scores['depth']['details']:
            report += f"- {detail}\n"
            
        report += f"""
### 5. 引用系统 ({self.scores['citation']['score']}/15)
"""
        for detail in self.scores['citation']['details']:
            report += f"- {detail}\n"
            
        report += f"""
### 6. 图表质量 ({self.scores['figures']['score']}/10)
"""
        for detail in self.scores['figures']['details']:
            report += f"- {detail}\n"
            
        report += f"""
### 7. 排版规范 ({self.scores['formatting']['score']}/10)
"""
        for detail in self.scores['formatting']['details']:
            report += f"- {detail}\n"
            
        report += f"""
### 8. 未来方向 ({self.scores['future']['score']}/10)
"""
        for detail in self.scores['future']['details']:
            report += f"- {detail}\n"
            
        # 改进建议
        report += """
## 改进建议

"""
        if percentage >= 90:
            report += "🎉 **恭喜！综述已达到 A+ 水平，可以投稿顶刊。**\n\n"
            report += "可选优化：\n"
            report += "- 进一步优化图表美观度\n"
            report += "- 检查是否有最新的相关文献可以补充\n"
        elif percentage >= 80:
            report += "✅ **综述达到 A 水平，经过微调后可以投稿。**\n\n"
            report += "建议改进：\n"
            # 找出得分最低的维度
            min_dim = min(self.scores.items(), key=lambda x: x[1]['score']/x[1]['max'])
            report += f"- 重点提升：{min_dim[0]} (当前 {min_dim[1]['score']}/{min_dim[1]['max']})\n"
        else:
            report += "⚠️ **综述需要进一步改进。**\n\n"
            report += "优先级改进：\n"
            # 找出得分最低的3个维度
            sorted_dims = sorted(self.scores.items(), key=lambda x: x[1]['score']/x[1]['max'])
            for i, (name, data) in enumerate(sorted_dims[:3]):
                report += f"{i+1}. {name}: {data['score']}/{data['max']}\n"
                
        report += """
## 下一步行动

"""
        if percentage >= 90:
            report += "- [ ] 最终校对：检查拼写和格式\n"
            report += "- [ ] 编译 PDF 验证效果\n"
            report += "- [ ] 准备投稿材料\n"
        elif percentage >= 70:
            report += "- [ ] 根据建议修复问题\n"
            report += "- [ ] 重新运行质量检查\n"
            report += "- [ ] 迭代改进直至达到 A+\n"
        else:
            report += "- [ ] 结构性调整：补充缺失章节\n"
            report += "- [ ] 内容扩充：增加深度分析\n"
            report += "- [ ] 重新运行质量检查\n"
            
        return report, grade


def main():
    parser = argparse.ArgumentParser(description='Survey Evolution - 综述质量检查工具')
    parser.add_argument('--input', '-i', required=True, help='输入的 .tex 文件路径')
    parser.add_argument('--output', '-o', default='quality_report.md', help='输出报告路径')
    
    args = parser.parse_args()
    
    # 读取输入文件
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 创建检查器
    checker = SurveyQualityChecker(content)
    
    # 执行所有检查
    print("🔍 正在检查综述质量...")
    checker.check_structure_integrity()
    checker.check_introduction_quality()
    checker.check_classification_framework()
    checker.check_content_depth()
    checker.check_citation_system()
    checker.check_figure_quality()
    checker.check_formatting()
    checker.check_future_directions()
    
    # 生成报告
    report, grade = checker.generate_report()
    
    # 保存报告
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(report)
        
    print(f"✅ 质量检查完成！")
    print(f"📊 等级: {grade}")
    print(f"📝 报告已保存至: {args.output}")


if __name__ == '__main__':
    main()
