#!/usr/bin/env python3
"""
Survey Expander - 章节分析工具
自动识别初稿中的扩展机会点
"""

import re
import json
import argparse
from pathlib import Path


def parse_latex_sections(tex_content):
    """解析 LaTeX 文档的章节结构"""
    sections = []
    
    # 匹配章节命令
    section_pattern = r'\\(section|subsection|subsubsection)\{([^}]+)\}'
    
    # 记录当前章节层级
    current_sections = {'section': None, 'subsection': None, 'subsubsection': None}
    
    for match in re.finditer(section_pattern, tex_content):
        level = match.group(1)
        title = match.group(2)
        start_pos = match.end()
        
        # 找到下一个章节或文档结束
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
        
        section_info = {
            'level': level,
            'title': title,
            'chars': char_count,
            'content': content[:500] + '...' if len(content) > 500 else content
        }
        
        sections.append(section_info)
    
    return sections


def find_single_sentence_paragraphs(content):
    """识别单句段落（连续换行）"""
    paragraphs = re.split(r'\n\s*\n', content)
    single_sentences = []
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # 检测是否为单句（没有句号或只有一个句号在末尾）
        sentences = re.split(r'[。\.\?\!]', para)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if len(sentences) == 1 and len(para) < 100:
            single_sentences.append({
                'text': para[:100],
                'chars': len(para)
            })
    
    return single_sentences


def analyze_sections(tex_content):
    """分析章节，识别扩展点"""
    sections = parse_latex_sections(tex_content)
    expansion_points = []
    
    for s in sections:
        # 检测末级标题字数
        if s['level'] == 'subsubsection' and s['chars'] < 500:
            expansion_points.append({
                'type': 'short_section',
                'section': s['title'],
                'level': s['level'],
                'current_chars': s['chars'],
                'target_chars': 500,
                'strategy': 'depth_elaboration'
            })
        
        # 检测单句段落
        single_sentences = find_single_sentence_paragraphs(s['content'])
        if single_sentences:
            expansion_points.append({
                'type': 'single_sentence',
                'section': s['title'],
                'paragraphs': single_sentences,
                'target_chars': 100
            })
    
    return sections, expansion_points


def generate_report(sections, expansion_points):
    """生成分析报告"""
    report = []
    report.append("# 扩展计划")
    report.append("")
    report.append("## 章节分析")
    report.append("")
    report.append("| 章节 | 当前字数 | 状态 | 扩展策略 |")
    report.append("|------|----------|------|----------|")
    
    for s in sections:
        if s['level'] == 'subsubsection':
            status = "✅ 达标" if s['chars'] >= 500 else "⚠️ 过短"
            strategy = "-" if s['chars'] >= 500 else "深度阐述"
            report.append(f"| {s['title'][:30]} | {s['chars']} | {status} | {strategy} |")
    
    report.append("")
    report.append("## 扩展点详情")
    report.append("")
    
    for i, point in enumerate(expansion_points, 1):
        report.append(f"### 扩展点 {i}")
        report.append(f"- **类型**: {point['type']}")
        report.append(f"- **章节**: {point.get('section', 'N/A')}")
        
        if point['type'] == 'short_section':
            report.append(f"- **当前字数**: {point['current_chars']}")
            report.append(f"- **目标字数**: {point['target_chars']}")
            report.append(f"- **扩展策略**: {point['strategy']}")
        elif point['type'] == 'single_sentence':
            report.append(f"- **单句段落数**: {len(point['paragraphs'])}")
            report.append(f"- **目标字数**: {point['target_chars']}")
        
        report.append("")
    
    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description='分析 LaTeX 综述初稿，识别扩展点')
    parser.add_argument('--input', '-i', required=True, help='输入 LaTeX 文件路径')
    parser.add_argument('--output', '-o', default='expansion_plan.md', help='输出报告路径')
    parser.add_argument('--json', '-j', help='JSON 格式输出路径（可选）')
    
    args = parser.parse_args()
    
    # 读取输入文件
    tex_path = Path(args.input)
    if not tex_path.exists():
        print(f"错误：文件不存在 {args.input}")
        return 1
    
    tex_content = tex_path.read_text(encoding='utf-8')
    
    # 分析章节
    sections, expansion_points = analyze_sections(tex_content)
    
    # 生成报告
    report = generate_report(sections, expansion_points)
    
    # 保存报告
    output_path = Path(args.output)
    output_path.write_text(report, encoding='utf-8')
    print(f"分析报告已保存至: {output_path}")
    
    # 可选：保存 JSON
    if args.json:
        json_data = {
            'sections': sections,
            'expansion_points': expansion_points
        }
        json_path = Path(args.json)
        json_path.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"JSON 数据已保存至: {json_path}")
    
    # 打印摘要
    print(f"\n分析摘要:")
    print(f"- 总章节数: {len(sections)}")
    print(f"- 扩展点数量: {len(expansion_points)}")
    short_sections = [p for p in expansion_points if p['type'] == 'short_section']
    print(f"- 过短章节: {len(short_sections)}")
    
    return 0


if __name__ == '__main__':
    exit(main())
