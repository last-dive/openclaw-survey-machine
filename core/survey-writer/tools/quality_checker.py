#!/usr/bin/env python3
"""
Survey Quality Checker
基于UAV_Delay_Survey_v3成功经验的质量检查工具
"""

import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

class SurveyQualityChecker:
    """综述质量检查器"""
    
    def __init__(self, tex_file: str):
        self.tex_file = Path(tex_file)
        self.content = self.tex_file.read_text(encoding='utf-8')
        self.issues = []
        self.scores = {}
        
    def check_structure(self) -> Tuple[int, List[str]]:
        """检查文档结构完整性"""
        issues = []
        score = 20
        
        # 检查是否被截断
        end_document_count = self.content.count('\\end{document}')
        if end_document_count > 1:
            issues.append(f"❌ 发现{end_document_count}个\\end{{document}}，文档可能被截断")
            score -= 10
        elif end_document_count == 0:
            issues.append("❌ 缺少\\end{document}")
            score -= 10
            
        # 检查章节完整性
        chapters = re.findall(r'\\section\{([^}]+)\}', self.content)
        if len(chapters) < 7:
            issues.append(f"⚠️ 只有{len(chapters)}章，标准综述应有7章")
            score -= 5
        else:
            issues.append(f"✅ 章节完整 ({len(chapters)}章)")
            
        # 检查目录
        if '\\tableofcontents' not in self.content:
            issues.append("⚠️ 缺少目录")
            score -= 2
            
        return max(0, score), issues
    
    def check_citations(self) -> Tuple[int, List[str]]:
        """检查引用系统"""
        issues = []
        score = 20
        
        # 检查是否有??引用失败
        undefined_cites = re.findall(r'\[\?\?\]', self.content)
        if undefined_cites:
            issues.append(f"❌ 发现{len(undefined_cites)}处引用失败[??]")
            score -= 10
        else:
            issues.append("✅ 无引用失败")
            
        # 检查是否使用thebibliography
        if '\\begin{thebibliography}' in self.content:
            issues.append("✅ 使用标准thebibliography环境")
        elif '\\begin{enumerate}' in self.content and 'bibitem' not in self.content:
            issues.append("❌ 使用enumerate做参考文献，应改为thebibliography")
            score -= 10
        else:
            issues.append("⚠️ 未找到标准参考文献环境")
            score -= 5
            
        # 检查cite使用
        cite_count = len(re.findall(r'\\cite\{([^}]+)\}', self.content))
        if cite_count < 20:
            issues.append(f"⚠️ 引用数量较少 ({cite_count}处)")
            score -= 3
        else:
            issues.append(f"✅ 引用数量充足 ({cite_count}处)")
            
        return max(0, score), issues
    
    def check_formatting(self) -> Tuple[int, List[str]]:
        """检查排版格式"""
        issues = []
        score = 15
        
        # 检查孤立列举 (1)(2)(3)(4)
        isolated_lists = re.findall(r'\n\s*\(\d\)[^\n]{0,50}\n', self.content)
        if isolated_lists:
            issues.append(f"⚠️ 发现{len(isolated_lists)}处孤立列举，建议改为表格或连续叙述")
            score -= 5
        else:
            issues.append("✅ 无孤立列举")
            
        # 检查交叉引用格式
        bad_refs = re.findall(r'[^~]\\ref\{', self.content)
        if bad_refs:
            issues.append(f"⚠️ 发现{len(bad_refs)}处交叉引用缺少~，建议改为`表~\\ref{{}}`格式")
            score -= 3
        else:
            issues.append("✅ 交叉引用格式正确")
            
        # 检查单句itemize
        short_items = re.findall(r'\\item\s*[^\\]{0,100}\\n\\end\{itemize\}', self.content)
        if short_items:
            issues.append(f"⚠️ 发现{len(short_items)}处简短itemize，建议合并为段落")
            score -= 3
            
        return max(0, score), issues
    
    def check_figures(self) -> Tuple[int, List[str]]:
        """检查图表"""
        issues = []
        score = 15
        
        # 统计图表数量
        figures = re.findall(r'\\begin\{figure\}', self.content)
        tables = re.findall(r'\\begin\{table\}', self.content)
        
        total = len(figures) + len(tables)
        
        if total < 5:
            issues.append(f"⚠️ 图表数量较少 ({total}个)，建议5-10个")
            score -= 5
        elif total > 15:
            issues.append(f"⚠️ 图表数量过多 ({total}个)")
            score -= 2
        else:
            issues.append(f"✅ 图表数量合适 ({total}个)")
            
        issues.append(f"  - 图: {len(figures)}个")
        issues.append(f"  - 表: {len(tables)}个")
        
        # 检查TikZ图
        tikz_figures = re.findall(r'\\begin\{tikzpicture\}', self.content)
        if tikz_figures:
            issues.append(f"✅ 包含{len(tikz_figures)}个TikZ图")
        
        return max(0, score), issues
    
    def check_content(self) -> Tuple[int, List[str]]:
        """检查内容质量"""
        issues = []
        score = 15
        
        # 检查批判性分析
        critical_patterns = ['局限性', '缺点', '不足', '挑战', '问题']
        critical_count = sum(self.content.count(p) for p in critical_patterns)
        
        if critical_count < 10:
            issues.append(f"⚠️ 批判性分析较少 ({critical_count}处)，建议>10处")
            score -= 5
        else:
            issues.append(f"✅ 批判性分析充足 ({critical_count}处)")
            
        # 检查数学公式
        equations = re.findall(r'\\begin\{equation\}', self.content)
        if len(equations) < 10:
            issues.append(f"⚠️ 公式数量较少 ({len(equations)}个)")
            score -= 3
        else:
            issues.append(f"✅ 公式数量充足 ({len(equations)}个)")
            
        # 检查未来方向
        if '未来' in self.content and ('展望' in self.content or '趋势' in self.content):
            issues.append("✅ 包含未来方向讨论")
        else:
            issues.append("⚠️ 未来方向讨论不充分")
            score -= 3
            
        return max(0, score), issues
    
    def check_compilation(self) -> Tuple[int, List[str]]:
        """检查编译状态"""
        issues = []
        score = 15
        
        # 检查常见编译错误
        errors = []
        
        # 未闭合环境
        envs = re.findall(r'\\begin\{([^}]+)\}', self.content)
        end_envs = re.findall(r'\\end\{([^}]+)\}', self.content)
        
        for env in set(envs):
            if envs.count(env) != end_envs.count(env):
                errors.append(f"环境{env}未正确闭合")
                
        # 数学模式错误
        if '$' in self.content:
            dollar_count = self.content.count('$')
            if dollar_count % 2 != 0:
                errors.append("数学模式$符号不匹配")
                
        if errors:
            for e in errors[:3]:
                issues.append(f"❌ {e}")
            score -= 10
        else:
            issues.append("✅ 无明显编译错误")
            
        return max(0, score), issues
    
    def run_all_checks(self) -> Dict:
        """运行所有检查"""
        print(f"\n{'='*60}")
        print(f"综述质量检查报告")
        print(f"{'='*60}")
        print(f"文件: {self.tex_file}")
        print(f"{'='*60}\n")
        
        checks = [
            ("结构完整性", self.check_structure),
            ("引用系统", self.check_citations),
            ("排版格式", self.check_formatting),
            ("图表质量", self.check_figures),
            ("内容深度", self.check_content),
            ("编译状态", self.check_compilation),
        ]
        
        total_score = 0
        max_score = 0
        
        for name, check_func in checks:
            score, issues = check_func()
            self.scores[name] = score
            
            max_s = {'结构完整性': 20, '引用系统': 20, '排版格式': 15, 
                     '图表质量': 15, '内容深度': 15, '编译状态': 15}[name]
            max_score += max_s
            total_score += score
            
            print(f"\n【{name}】 {score}/{max_s}分")
            print("-" * 40)
            for issue in issues:
                print(f"  {issue}")
                
        # 总分
        print(f"\n{'='*60}")
        print(f"总分: {total_score}/{max_score} ({total_score/max_score*100:.1f}%)")
        print(f"{'='*60}")
        
        # 评级
        percentage = total_score / max_score * 100
        if percentage >= 90:
            grade = "A+ (优秀，可投稿顶刊)"
        elif percentage >= 80:
            grade = "A (良好，可投稿核心期刊)"
        elif percentage >= 70:
            grade = "B+ (中等，需进一步完善)"
        elif percentage >= 60:
            grade = "B (及格，需大幅修改)"
        else:
            grade = "C (不合格，需重写)"
            
        print(f"评级: {grade}")
        print(f"{'='*60}\n")
        
        return {
            'total_score': total_score,
            'max_score': max_score,
            'percentage': percentage,
            'grade': grade,
            'details': self.scores
        }

def main():
    parser = argparse.ArgumentParser(description='综述质量检查工具')
    parser.add_argument('tex_file', help='LaTeX文件路径')
    parser.add_argument('-o', '--output', help='输出报告文件')
    args = parser.parse_args()
    
    checker = SurveyQualityChecker(args.tex_file)
    result = checker.run_all_checks()
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"综述质量检查报告\n")
            f.write(f"="*60 + "\n")
            f.write(f"文件: {args.tex_file}\n")
            f.write(f"总分: {result['total_score']}/{result['max_score']}\n")
            f.write(f"评级: {result['grade']}\n")
            f.write(f"="*60 + "\n\n")
            f.write("详细评分:\n")
            for name, score in result['details'].items():
                f.write(f"  {name}: {score}分\n")
        print(f"报告已保存到: {args.output}")

if __name__ == '__main__':
    main()
