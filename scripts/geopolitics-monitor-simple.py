#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
地缘政治监控系统（简化版）- 仅检查记忆并读取搜索结果
"""

import json
import os
import subprocess
from datetime import datetime
from os.path import exists

def check_memory_system():
    """检查记忆系统压缩风险"""
    try:
        result = subprocess.run(
            ['~/.openclaw/workspace/skills/memory-manager/detect.sh'],
            capture_output=True
        )
        output = result.stdout.decode()
        print(f"✅ 讘忆系统状态: {output.strip()}")
        return True
    except Exception as e:
        print(f"❌ 检查记忆系统失败: {e}")
        return False

def load_last_search():
    """读取最后一次搜索结果"""
    cache_path = os.path.expanduser('~/.openclaw/workspace/data/tavily_last_search.json')
    
    if exists(cache_path):
        with open(cache_path, 'r') as f:
            data = json.load(f)
            print(f"✅ 加载搜索结果: {data.get('query')}")
            print(f"📊 结果数: {len(data.get('results', []))}")
            return data
    else:
        print("❌ 未找到搜索结果缓存")
        return None

def main():
    """主函数"""
    print("=" * 50)
    print("🌍 地缘政治监控系统")
    print("=" * 50)
    
    # 检查记忆系统
    check_memory_system()
    
    # 读取搜索结果
    search_data = load_last_search()
    
    if search_data:
        print("\n✅ 搜索结果已加载")
        print(f"查询: {search_data.get('query')}")
        print(f"结果数: {len(search_data.get('results', []))}")
    else:
        print("\n⚠️ 未找到搜索结果， 请先运行 tavily-search.py")
    
    print("\n" + "=" * 50)
    print("监控完成")
    print("=" * 50)

if __name__ == '__main__':
    main()
