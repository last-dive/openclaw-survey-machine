#!/usr/bin/env python3
"""
Survey Evolution - 综述改进工具
基于质量报告自动改进综述

使用方法:
    python3 improver.py --input survey.tex --report quality_report.md --output survey_v2.tex
"""

import re
import argparse
from pathlib import Path


class SurveyImprover:
    """综述改进器"""
    
    def __init__(self, tex_content, report_content):
        self.content = tex_content
        self.report = report_content
        self.changes = []
        
    def fix_isolated_lists(self):
        """修复孤立列举"""
        # 查找 (1)(2)(3) 格式的孤立列举并转换为 itemize
        pattern = r'\n((?:\(\d+\)[^\n]+\n?)+)'
        
        def replace_list(match):
            items = match.group(1).strip().split('\n')
            result = '\n\\begin{itemize}\n'
            for item in items:
                # 提取 (n) 后的内容
                content = re.sub(r'^\(\d+\)\s*', '', item.strip())
                if content:
                    result += f'    \\item {content}\n'
            result += '\\end{itemize}\n'
            self.changes.append(f"修复孤立列举: {items[0][:30]}...")
            return result
            
        self.content = re.sub(pattern, replace_list, self.content)
        return len(self.changes)
        
    def add_cross_references(self):
        """添加交叉引用"""
        # 为图表添加交叉引用
        # 查找 "图 X" 或 "表 X" 并替换为 "图~\\ref{fig:X}"
        
        # 统计已有的引用
        existing_refs = set(re.findall(r'\\label\{([^}]+)\}', self.content))
        
        # 为没有引用的图表添加标签
        figures = re.findall(r'\\begin\{figure\}.*?\\caption\{([^}]+)\}.*?\\end\{figure\}', 
                            self.content, re.DOTALL)
        for i, caption in enumerate(figures, 1):
            label = f'fig:{i}'
            if label not in existing_refs:
                # 在 figure 环境中添加 label
                pattern = f'(\\begin{{figure}}.*?)(\\\\end{{figure}})'
                replacement = rf'\1\\label{{{label}}}\n\2'
                self.content = re.sub(pattern, replacement, self.content, count=1, flags=re.DOTALL)
                self.changes.append(f"添加图表标签: {label}")
                
        return len(self.changes)
        
    def enhance_future_section(self):
        """增强未来方向章节"""
        # 查找未来方向章节
        future_pattern = r'(\\section\{[^}]*(?:展望|未来|结论|Conclusion|Future)[^}]*\}.*?)(?=\\section|\Z)'
        match = re.search(future_pattern, self.content, re.I | re.DOTALL)
        
        if match and len(match.group(1)) < 500:
            # 如果章节较短，添加更多内容
            enhancement = """

未来研究可能从以下几个方向展开：

\\textbf{理论突破}：现有方法在理论保证方面仍有不足。未来的研究需要发展更完善的理论框架，为强化学习在飞行控制中的应用提供收敛性、稳定性和安全性的数学保证。

\\textbf{算法创新}：结合大语言模型、神经辐射场等新兴技术，开发更智能、更高效的控制算法。特别是多模态感知融合和端到端学习将是重要的研究方向。

\\textbf{系统集成}：研究如何在资源受限的机载平台上高效部署深度强化学习模型，包括模型压缩、硬件加速和边缘计算等技术。

\\textbf{安全认证}：建立针对神经网络控制器的验证和认证流程，满足航空领域的严格标准，推动技术的实际应用。

\\textbf{标准化建设}：建立统一的评估基准和数据集，促进研究的可比性和可复现性，加速领域发展。
"""
            self.content = self.content.replace(match.group(1), match.group(1) + enhancement)
            self.changes.append("增强未来方向章节")
            
        return len(self.changes)
        
    def fix_citations(self):
        """修复引用问题"""
        # 查找 ?? 引用并尝试修复
        undefined_refs = re.findall(r'\\cite\{([^}]+)\}[^\n]*?\?\?', self.content)
        
        for ref in undefined_refs:
            # 在参考文献部分添加占位
            bib_pattern = r'(\\begin\{thebibliography\}.*?)(\\\\end\{thebibliography\}|\\bibliography)'
            new_entry = f'\\bibitem{{{ref}}}\nPlaceholder citation for {{{ref}}}. Please add full reference.\n\n'
            
            if re.search(bib_pattern, self.content, re.DOTALL):
                self.content = re.sub(bib_pattern, rf'\1{new_entry}\2', self.content, flags=re.DOTALL)
                self.changes.append(f"添加占位引用: {ref}")
                
        return len(self.changes)
        
    def improve_introduction(self):
        """改进引言"""
        # 检查引言是否有贡献说明
        intro_match = re.search(r'\\section\{[^}]*引言|Introduction[^}]*\}(.*?)(?=\\section|\Z)', 
                                self.content, re.I | re.DOTALL)
        
        if intro_match:
            intro = intro_match.group(1)
            if '贡献' not in intro and 'Contribution' not in intro:
                # 在引言末尾添加贡献说明
                contribution = """

本文的主要贡献包括：
\\begin{enumerate}
    \\item 系统梳理了该领域的研究现状，建立了清晰的分类框架；
    \\item 深入分析了各类方法的优缺点和适用场景；
    \\item 指出了当前面临的关键挑战和未来研究方向。
\\end{enumerate}
"""
                # 在引言最后添加
                new_intro = intro.rstrip() + contribution
                self.content = self.content.replace(intro, new_intro)
                self.changes.append("添加引言贡献说明")
                
        return len(self.changes)
        
    def generate_improvement_log(self):
        """生成改进日志"""
        log = """# 改进日志

## 改进摘要

"""
        if self.changes:
            log += f"本次改进共进行了 {len(self.changes)} 项修改：\n\n"
            for i, change in enumerate(self.changes, 1):
                log += f"{i}. {change}\n"
        else:
            log += "本次未进行自动改进。请根据质量报告手动优化。\n"
            
        log += """
## 手动改进建议

根据质量报告，建议进行以下手动改进：

1. **内容深度**：为每个方法添加更详细的原理说明和优缺点分析
2. **批判性分析**：增加方法之间的对比和批判性讨论
3. **图表优化**：确保所有图表清晰、专业、无重叠
4. **引用完善**：补充缺失的参考文献，确保引用格式规范
5. **排版细节**：检查交叉引用、公式编号、列表格式等

## 下一步

1. 检查自动改进是否正确
2. 根据质量报告进行手动优化
3. 重新运行质量检查
4. 迭代改进直至达到 A+ 水平
"""
        return log


def main():
    parser = argparse.ArgumentParser(description='Survey Evolution - 综述改进工具')
    parser.add_argument('--input', '-i', required=True, help='输入的 .tex 文件路径')
    parser.add_argument('--report', '-r', required=True, help='质量报告路径')
    parser.add_argument('--output', '-o', required=True, help='输出文件路径')
    
    args = parser.parse_args()
    
    # 读取文件
    with open(args.input, 'r', encoding='utf-8') as f:
        tex_content = f.read()
        
    with open(args.report, 'r', encoding='utf-8') as f:
        report_content = f.read()
        
    # 创建改进器
    improver = SurveyImprover(tex_content, report_content)
    
    # 执行改进
    print("🔧 正在自动改进综述...")
    
    # 根据报告中的问题选择改进策略
    if '孤立列举' in report_content:
        improver.fix_isolated_lists()
        
    if '??' in report_content and '未定义引用' in report_content:
        improver.fix_citations()
        
    if '交叉引用' in report_content and '较少' in report_content:
        improver.add_cross_references()
        
    if '未来方向' in report_content and ('不够具体' in report_content or '缺少' in report_content):
        improver.enhance_future_section()
        
    if '贡献' in report_content and '缺少' in report_content:
        improver.improve_introduction()
        
    # 保存改进后的文件
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(improver.content)
        
    # 保存改进日志
    log_path = args.output.replace('.tex', '_improvement_log.md')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(improver.generate_improvement_log())
        
    print(f"✅ 改进完成！")
    print(f"📝 改进后的文件: {args.output}")
    print(f"📋 改进日志: {log_path}")
    
    if improver.changes:
        print(f"\n📊 共进行了 {len(improver.changes)} 项自动改进")
        for change in improver.changes:
            print(f"  - {change}")
    else:
        print(f"\n⚠️ 未进行自动改进，请根据质量报告手动优化")


if __name__ == '__main__':
    main()
