#!/usr/bin/env python3
"""
Survey Expander - 质量检查工具
检查扩展后的论文质量
"""

import re
import argparse
from pathlib import Path


def count_pages(tex_content):
    """估算页数（基于字数）"""
    # 移除 LaTeX 命令
    clean_text = re.sub(r'\\[a-zA-Z]+(\[.*?\])?(\{.*?\})?', '', tex_content)
    # 中文字符计数
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', clean_text))
    # 英文单词计数
    english_words = len(re.findall(r'[a-zA-Z]+', clean_text))
    
    # 估算：中文约 800 字/页，英文约 400 词/页
    estimated_pages = (chinese_chars / 800) + (english_words / 400)
    return estimated_pages, chinese_chars, english_words


def check_sections(tex_content):
    """检查章节字数"""
    section_pattern = r'\\(section|subsection|subsubsection)\{([^}]+)\}'
    issues = []
    
    for match in re.finditer(section_pattern, tex_content):
        level = match.group(1)
        title = match.group(2)
        start_pos = match.end()
        
        # 找到下一个章节
        next_match = None
        for next_m in re.finditer(section_pattern, tex_content[start_pos:]):
            next_match = next_m
            break
        
        if next_match:
            end_pos = start_pos + next_match.start()
        else:
            end_pos = len(tex_content)
        
        content = tex_content[start_pos:end_pos]
        char_count = len(content.strip())
        
        if level == 'subsubsection' and char_count < 500:
            issues.append({
                'type': 'short_section',
                'section': title,
                'chars': char_count,
                'message': f'末级标题 "{title}" 字数不足（{char_count} < 500）'
            })
    
    return issues


def check_citations(tex_content):
    """检查引用"""
    issues = []
    
    # 检查未定义引用
    undefined_cites = re.findall(r'cite\{([^}]+)\}', tex_content)
    
    # 检查 [??]
    undefined_refs = re.findall(r'\[\?\?\]', tex_content)
    if undefined_refs:
        issues.append({
            'type': 'undefined_ref',
            'count': len(undefined_refs),
            'message': f'发现 {len(undefined_refs)} 处未定义引用 [??]'
        })
    
    return issues


def check_figures(tex_content):
    """检查图表"""
    issues = []
    
    # 统计图表数量
    figures = len(re.findall(r'\\begin\{figure\}', tex_content))
    tables = len(re.findall(r'\\begin\{table\}', tex_content))
    
    # 估算图表页数（假设每个图表占 0.5 页）
    figure_pages = (figures + tables) * 0.5
    
    # 估算总页数
    total_pages, _, _ = count_pages(tex_content)
    
    # 检查图表占比
    if total_pages > 0:
        figure_ratio = figure_pages / total_pages
        if figure_ratio > 0.3:
            issues.append({
                'type': 'figure_ratio',
                'ratio': figure_ratio,
                'message': f'图表占比过高（{figure_ratio:.1%} > 30%）'
            })
    
    return issues, figures, tables


def check_consistency(original_content, expanded_content):
    """检查与原文的一致性"""
    issues = []
    
    # 检查原文框架是否保留
    original_sections = set(re.findall(r'\\(section|subsection|subsubsection)\{([^}]+)\}', original_content))
    expanded_sections = set(re.findall(r'\\(section|subsection|subsubsection)\{([^}]+)\}', expanded_content))
    
    removed_sections = original_sections - expanded_sections
    if removed_sections:
        issues.append({
            'type': 'removed_sections',
            'sections': removed_sections,
            'message': f'发现 {len(removed_sections)} 个章节被删除'
        })
    
    return issues


def generate_report(expanded_path, original_path=None):
    """生成质量报告"""
    expanded_content = Path(expanded_path).read_text(encoding='utf-8')
    original_content = None
    if original_path:
        original_content = Path(original_path).read_text(encoding='utf-8')
    
    report = []
    report.append("# 质量检查报告")
    report.append("")
    
    # 页数统计
    pages, chinese, english = count_pages(expanded_content)
    report.append("## 页数统计")
    report.append(f"- 估算页数: {pages:.1f} 页")
    report.append(f"- 中文字符: {chinese}")
    report.append(f"- 英文单词: {english}")
    report.append("")
    
    # 章节检查
    section_issues = check_sections(expanded_content)
    report.append("## 章节检查")
    if section_issues:
        report.append(f"⚠️ 发现 {len(section_issues)} 个问题:")
        for issue in section_issues:
            report.append(f"- {issue['message']}")
    else:
        report.append("✅ 所有末级标题字数达标")
    report.append("")
    
    # 引用检查
    citation_issues = check_citations(expanded_content)
    report.append("## 引用检查")
    if citation_issues:
        report.append(f"⚠️ 发现 {len(citation_issues)} 个问题:")
        for issue in citation_issues:
            report.append(f"- {issue['message']}")
    else:
        report.append("✅ 引用格式正确")
    report.append("")
    
    # 图表检查
    figure_issues, figures, tables = check_figures(expanded_content)
    report.append("## 图表检查")
    report.append(f"- 图片数量: {figures}")
    report.append(f"- 表格数量: {tables}")
    if figure_issues:
        for issue in figure_issues:
            report.append(f"⚠️ {issue['message']}")
    else:
        report.append("✅ 图表占比合理")
    report.append("")
    
    # 一致性检查
    if original_content:
        consistency_issues = check_consistency(original_content, expanded_content)
        report.append("## 一致性检查")
        if consistency_issues:
            report.append(f"⚠️ 发现 {len(consistency_issues)} 个问题:")
            for issue in consistency_issues:
                report.append(f"- {issue['message']}")
        else:
            report.append("✅ 原文框架完整保留")
        report.append("")
    
    # 总结
    total_issues = len(section_issues) + len(citation_issues) + len(figure_issues)
    if original_content:
        total_issues += len(consistency_issues)
    
    report.append("## 总结")
    if total_issues == 0:
        report.append("✅ 所有检查项通过")
    else:
        report.append(f"⚠️ 共发现 {total_issues} 个问题，请修复后重新检查")
    
    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description='检查扩展后的论文质量')
    parser.add_argument('--input', '-i', required=True, help='扩展后的 LaTeX 文件路径')
    parser.add_argument('--original', '-o', help='原始 LaTeX 文件路径（可选）')
    parser.add_argument('--output', '-O', default='quality_report.md', help='输出报告路径')
    
    args = parser.parse_args()
    
    # 生成报告
    report = generate_report(args.input, args.original)
    
    # 保存报告
    output_path = Path(args.output)
    output_path.write_text(report, encoding='utf-8')
    print(f"质量报告已保存至: {output_path}")
    
    return 0


if __name__ == '__main__':
    exit(main())
