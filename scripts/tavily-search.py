#!/usr/bin/env python3
"""
Tavily 搜索工具 - 实时新闻搜索
"""

import json
import os
import sys
from typing import Dict, List, Optional

# 添加到路径
sys.path.insert(0, os.path.expanduser("~/.openclaw/workspace"))

try:
    from tavily import TavilyClient
except ImportError:
    print("❌ tavily-python 未安装")
    print("运行: pip3 install tavily-python")
    sys.exit(1)


class TavilySearch:
    """Tavily 搜索客户端"""
    
    def __init__(self, config_path: str = None):
        """初始化"""
        if config_path is None:
            config_path = os.path.expanduser("~/.openclaw/workspace/config/search_config.json")
        
        self.config = self._load_config(config_path)
        self.api_key = self.config.get("providers", {}).get("tavily", {}).get("api_key")
        
        if not self.api_key:
            raise ValueError("❌ 未找到 Tavily API Key")
        
        self.client = TavilyClient(api_key=self.api_key)
    
    def _load_config(self, config_path: str) -> Dict:
        """加载配置"""
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"❌ 配置文件不存在: {config_path}")
        
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def search(self, query: str, max_results: int = 10, search_depth: str = "advanced") -> Dict:
        """执行搜索"""
        print(f"🔍 搜索: {query}")
        print(f"  - 最大结果: {max_results}")
        print(f"  - 搜索深度: {search_depth}")
        
        try:
            results = self.client.search(
                query=query,
                max_results=max_results,
                search_depth=search_depth
            )
            
            print(f"✅ 找到 {len(results.get('results', []))} 条结果")
            return results
            
        except Exception as e:
            print(f"❌ 搜索失败: {e}")
            return {"error": str(e), "results": []}
    
    def search_news(self, topic: str, days: int = 7) -> Dict:
        """搜索新闻（带时间过滤）"""
        query = f"{topic} latest news"
        
        # Tavily 支持 include_raw_content 和 days 参数
        try:
            results = self.client.search(
                query=query,
                max_results=10,
                search_depth="advanced",
                include_raw_content=False,
                days=days
            )
            
            return results
            
        except Exception as e:
            print(f"❌ 新闻搜索失败: {e}")
            return {"error": str(e), "results": []}
    
    def format_results(self, results: Dict, max_items: int = 5) -> str:
        """格式化搜索结果"""
        if "error" in results:
            return f"❌ 错误: {results['error']}"
        
        items = results.get("results", [])
        
        if not items:
            return "❌ 未找到结果"
        
        lines = []
        lines.append("=" * 70)
        lines.append(f"📰 搜索结果 ({len(items)} 条)")
        lines.append("=" * 70)
        
        for i, item in enumerate(items[:max_items], 1):
            title = item.get("title", "无标题")
            url = item.get("url", "")
            content = item.get("content", "")[:200] + "..."
            score = item.get("score", 0)
            
            lines.append(f"\n{i}. {title}")
            lines.append(f"   相关度: {score:.2f}")
            lines.append(f"   链接: {url}")
            lines.append(f"   摘要: {content}")
        
        return "\n".join(lines)
    
    def save_results(self, results: Dict, output_file: str):
        """保存结果到文件"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 结果已保存: {output_file}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Tavily 搜索工具")
    parser.add_argument("query", help="搜索关键词")
    parser.add_argument("--max", type=int, default=10, help="最大结果数")
    parser.add_argument("--depth", default="advanced", choices=["basic", "advanced"], help="搜索深度")
    parser.add_argument("--output", help="输出文件路径")
    
    args = parser.parse_args()
    
    # 创建客户端
    searcher = TavilySearch()
    
    # 执行搜索
    results = searcher.search(
        query=args.query,
        max_results=args.max,
        search_depth=args.depth
    )
    
    # 显示结果
    print(searcher.format_results(results))
    
    # 保存结果
    if args.output:
        searcher.save_results(results, args.output)


if __name__ == "__main__":
    main()
