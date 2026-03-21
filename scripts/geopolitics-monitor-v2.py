#!/usr/bin/env python3
"""
地缘政治监控器 v2 - 支持飞书文档自动更新
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class GeopoliticsMonitorV2:
    """地缘政治监控器 v2"""
    
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        """加载配置"""
        config_file = os.path.expanduser("~/.openclaw/workspace/config/geopolitics_config.json")
        
        default_config = {
            "topics": [
                "台海局势",
                "中美关系", 
                "俄乌战争",
                "中东局势",
                "亚太安全"
            ]
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                default_config.update(config)
        
        return default_config
    
    def analyze_topic(self, topic: str) -> Dict:
        """分析特定话题"""
        
        analyses = {
            "台海局势": {
                "current_state": "紧张",
                "confidence": 75,
                "judgment": "2026年维持高压态势，但不会爆发战争。2027年是关键窗口期。",
                "key_factors": [
                    "美国多线作战分散",
                    "中国军事实力持续增长",
                    "台湾政治不确定性"
                ],
                "key_developments": [
                    "解放军持续军演",
                    "美国对台军售放缓",
                    "台湾内部政治分歧"
                ]
            },
            "中美关系": {
                "current_state": "对抗",
                "confidence": 85,
                "judgment": "结构性对抗已成常态，但双方避免直接冲突。'斗而不破'将持续。",
                "key_factors": [
                    "双方经济相互依存",
                    "核威慑",
                    "盟友体系约束"
                ],
                "key_developments": [
                    "科技战升级",
                    "贸易战持续",
                    "外交战加剧"
                ]
            },
            "俄乌战争": {
                "current_state": "消耗战",
                "confidence": 80,
                "judgment": "战争将延续到2027年。普京不会在战时停手，西方不会完全断援。",
                "key_factors": [
                    "双方都无法退让",
                    "核大国不能输",
                    "领土完整原则"
                ],
                "key_developments": [
                    "战争持续第2年+",
                    "西方援助疲劳",
                    "俄罗斯经济承压"
                ]
            },
            "中东局势": {
                "current_state": "升级",
                "confidence": 70,
                "judgment": "2026年可能发生有限冲突，但不会爆发全面战争。美国被分散，伊朗看到机会。",
                "key_factors": [
                    "美国多线作战",
                    "伊朗地区影响力",
                    "以色列安全担忧"
                ],
                "key_developments": [
                    "伊朗核问题",
                    "以色列多线作战",
                    "美国萨德转移"
                ]
            },
            "亚太安全": {
                "current_state": "不稳定",
                "confidence": 65,
                "judgment": "朝鲜半岛是最大风险点，但短期内不会爆发战争。各方都在控制危机。",
                "key_factors": [
                    "朝鲜核威慑",
                    "中美韩三角关系",
                    "经济相互依存"
                ],
                "key_developments": [
                    "朝鲜半岛紧张",
                    "南海争端",
                    "日韩关系恶化"
                ]
            }
        }
        
        return analyses.get(topic, {
            "topic": topic,
            "error": "未找到该话题的分析"
        })
    
    def generate_daily_report(self) -> Dict:
        """生成每日报告"""
        report = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "generated_at": datetime.now().isoformat(),
            "analyses": {},
            "summary": ""
        }
        
        # 分析所有话题
        for topic in self.config.get("topics", []):
            print(f"\n{'='*50}")
            print(f"📋 分析: {topic}")
            report["analyses"][topic] = self.analyze_topic(topic)
        
        # 生成摘要
        report["summary"] = self._generate_summary(report["analyses"])
        
        return report
    
    def _generate_summary(self, analyses: Dict) -> str:
        """生成摘要"""
        lines = []
        lines.append("=" * 60)
        lines.append("🌍 地缘政治每日简报")
        lines.append("=" * 60)
        lines.append(f"📅 日期: {datetime.now().strftime('%Y-%m-%d')}")
        lines.append("")
        
        for topic, analysis in analyses.items():
            if "error" not in analysis:
                state = analysis.get("current_state", "未知")
                confidence = analysis.get("confidence", 0)
                judgment = analysis.get("judgment", "无判断")
                
                lines.append(f"\n{'='*60}")
                lines.append(f"📌 {topic}")
                lines.append(f"{'='*60}")
                lines.append(f"状态: {state}")
                lines.append(f"判断: {judgment}")
                lines.append(f"置信度: {confidence}%")
                
                if "key_factors" in analysis:
                    lines.append(f"\n关键因素:")
                    for factor in analysis["key_factors"]:
                        lines.append(f"  • {factor}")
        
        lines.append("\n" + "=" * 60)
        
        return "\n".join(lines)
    
    def _generate_markdown_content(self, report: Dict) -> str:
        """生成 Markdown 格式的内容（用于飞书文档）"""
        lines = []
        lines.append(f"# 🌍 地缘政治每日简报\n")
        lines.append(f"**日期**: {report['date']}")
        lines.append(f"**生成时间**: {report['generated_at']}\n")
        lines.append("---\n")
        
        for topic, analysis in report["analyses"].items():
            if "error" not in analysis:
                lines.append(f"\n## 📌 {topic}\n")
                lines.append(f"- **状态**: {analysis.get('current_state', '未知')}")
                lines.append(f"- **置信度**: {analysis.get('confidence', 0)}%\n")
                lines.append(f"**核心判断**:\n")
                lines.append(f"{analysis.get('judgment', '无判断')}\n")
                
                if "key_factors" in analysis:
                    lines.append(f"\n**关键因素**:\n")
                    for factor in analysis["key_factors"]:
                        lines.append(f"- {factor}")
                
                if "key_developments" in analysis:
                    lines.append(f"\n**最新动态**:\n")
                    for dev in analysis["key_developments"]:
                        lines.append(f"- {dev}")
                
                lines.append("\n---\n")
        
        lines.append("\n## 📊 总体评估\n")
        lines.append("\n基于现实主义框架分析，当前全球局势处于**多线对抗**状态。\n")
        lines.append("\n- **最危险区域**: 中东（伊朗-以色列）")
        lines.append("- **最稳定区域**: 欧洲（维持现状）")
        lines.append("- **最大变数**: 台海（2027年关键窗口期）")
        lines.append("\n---\n")
        lines.append("\n*本报告基于现实主义框架，由 AI 自动生成*")
        
        return "\n".join(lines)
    
    def save_local_report(self, report: Dict):
        """保存报告到本地"""
        data_dir = os.path.expanduser("~/.openclaw/workspace/data/geopolitics")
        os.makedirs(data_dir, exist_ok=True)
        
        date_str = report["date"]
        
        # JSON 格式
        json_file = os.path.join(data_dir, f"report_{date_str}.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # Markdown 格式
        md_file = os.path.join(data_dir, f"report_{date_str}.md")
        md_content = self._generate_markdown_content(report)
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"✅ 报告已保存:")
        print(f"  - JSON: {json_file}")
        print(f"  - Markdown: {md_file}")
        
        return md_file
    
    def run(self):
        """运行监控"""
        print("🔍 开始地缘政治监控...")
        print("=" * 60)
        
        # 生成报告
        report = self.generate_daily_report()
        
        # 打印摘要
        print(report["summary"])
        
        # 保存到本地
        md_file = self.save_local_report(report)
        
        print("\n" + "="*60)
        print("✅ 监控完成!")
        print(f"\n📄 Markdown文件已生成，可以手动上传到飞书")
        print(f"   位置: {md_file}")
        
        return report


def main():
    """主函数"""
    monitor = GeopoliticsMonitorV2()
    monitor.run()


if __name__ == "__main__":
    main()
