#!/usr/bin/env python3
"""工作流编排器 - 协调各模块完成综述生成"""

import argparse
import os
import sys
import yaml
import json
from datetime import datetime

def load_config(config_path):
    """加载配置"""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', required=True)
    parser.add_argument('--subtopics', default='')
    parser.add_argument('--pages', type=int, default=50)
    parser.add_argument('--config', default='config/config.yaml')
    parser.add_argument('--work-dir', required=True)
    args = parser.parse_args()
    
    print(f"📝 主题: {args.topic}")
    print(f"📁 工作目录: {args.work_dir}")
    print("")
    
    # 加载配置
    config = load_config(args.config)
    
    # 创建输出结构
    os.makedirs(args.work_dir, exist_ok=True)
    os.makedirs(f"{args.work_dir}/figures", exist_ok=True)
    
    # 保存配置
    with open(f"{args.work_dir}/config_used.json", 'w') as f:
        json.dump({
            'topic': args.topic,
            'subtopics': args.subtopics,
            'pages': args.pages,
            'timestamp': datetime.now().isoformat()
        }, f, indent=2)
    
    print("✅ 工作流初始化完成")
    print(f"请查看工作目录: {args.work_dir}")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
