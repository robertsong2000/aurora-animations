#!/usr/bin/env python3
"""
Tavily 实时搜索脚本
使用 Tavily API 搜索实时新闻
"""

import json
import os
import sys
from typing import Dict, List, Optional
import urllib.request
import urllib.error

class TavilySearch:
    """Tavily 搜索客户端"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or self._load_api_key()
        self.base_url = "https://api.tavily.com"
    
    def _load_api_key(self) -> str:
        """从配置文件加载 API Key"""
        config_file = os.path.expanduser("~/.openclaw/workspace/config/search_config.json")
        
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get("providers", {}).get("tavily", {}).get("api_key", "")
        
        raise ValueError("Tavily API Key 未配置")
    
    def search(
        self,
        query: str,
        max_results: int = 10,
        search_depth: str = "advanced",
        include_domains: Optional[List[str]] = None,
        exclude_domains: Optional[List[str]] = None,
        include_answer: bool = True,
        include_raw_content: bool = False,
        include_images: bool = False,
    ) -> Dict:
        """
        执行搜索
        
        Args:
            query: 搜索关键词
            max_results: 最大结果数（默认10）
            search_depth: 搜索深度（basic/advanced）
            include_domains: 包含的域名列表
            exclude_domains: 排除的域名列表
            include_answer: 是否包含 AI 生成的答案
            include_raw_content: 是否包含原始内容
            include_images: 是否包含图片
        
        Returns:
            搜索结果字典
        """
        
        url = f"{self.base_url}/search"
        
        payload = {
            "api_key": self.api_key,
            "query": query,
            "max_results": max_results,
            "search_depth": search_depth,
            "include_answer": include_answer,
            "include_raw_content": include_raw_content,
            "include_images": include_images,
        }
        
        if include_domains:
            payload["include_domains"] = include_domains
        if exclude_domains:
            payload["exclude_domains"] = exclude_domains
        
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            print(f"❌ HTTP Error {e.code}: {error_body}", file=sys.stderr)
            return {"error": f"HTTP {e.code}", "details": error_body}
        except urllib.error.URLError as e:
            print(f"❌ URL Error: {e.reason}", file=sys.stderr)
            return {"error": str(e.reason)}
        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            return {"error": str(e)}
    
    def format_results(self, results: Dict) -> str:
        """格式化搜索结果为可读文本"""
        if "error" in results:
            return f"❌ 搜索失败: {results['error']}"
        
        lines = []
        
        # AI 生成的答案（如果有）
        if "answer" in results and results["answer"]:
            lines.append("=" * 60)
            lines.append("💡 AI 摘要")
            lines.append("=" * 60)
            lines.append(results["answer"])
            lines.append("")
        
        # 搜索结果
        if "results" in results:
            lines.append("=" * 60)
            lines.append(f"📰 搜索结果 ({len(results['results'])} 条)")
            lines.append("=" * 60)
            
            for i, item in enumerate(results["results"], 1):
                lines.append(f"\n{i}. {item.get('title', '无标题')}")
                lines.append(f"   链接: {item.get('url', '')}")
                lines.append(f"   来源: {item.get('source', '未知')}")
                
                if "content" in item:
                    content = item["content"]
                    if len(content) > 200:
                        content = content[:200] + "..."
                    lines.append(f"   摘要: {content}")
                
                if "published_date" in item:
                    lines.append(f"   时间: {item['published_date']}")
                
                lines.append("")
        
        return "\n".join(lines)


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python3 tavily-search.py <搜索关键词> [--max 10] [--depth basic|advanced]")
        print("示例: python3 tavily-search.py '国际新闻 地缘政治' --max 10 --depth advanced")
        sys.exit(1)
    
    # 解析参数
    query = sys.argv[1]
    max_results = 10
    search_depth = "advanced"
    
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--max" and i + 1 < len(sys.argv):
            max_results = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--depth" and i + 1 < len(sys.argv):
            search_depth = sys.argv[i + 1]
            i += 2
        else:
            i += 1
    
    # 执行搜索
    print(f"🔍 正在搜索: {query}")
    print(f"📊 最大结果: {max_results}, 深度: {search_depth}")
    print("")
    
    client = TavilySearch()
    results = client.search(
        query=query,
        max_results=max_results,
        search_depth=search_depth,
        include_answer=True
    )
    
    # 格式化输出
    print(client.format_results(results))
    
    # 保存 JSON 结果
    output_file = os.path.expanduser("~/.openclaw/workspace/data/tavily_last_search.json")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n📄 完整结果已保存: {output_file}")


if __name__ == "__main__":
    main()
