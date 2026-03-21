#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Prompt Generator - Seedance 专用版
为火山引擎 Seedance 生成中文视频提示词
"""

import argparse
import json
from typing import Optional, List, Dict

# 胶片质感模板（中文）
FILM_PRESETS = {
    "portra400": {
        "name": "柯达 Portra 400",
        "description": "35mm柯达Portra 400胶片质感，细腻柔和颗粒，暖调金黄，梦幻氛围",
        "keywords": "Portra 400胶片质感，暖调，柔和颗粒"
    },
    "ektar100": {
        "name": "柯达 Ektar 100",
        "description": "Ektar 100胶片质感，极细颗粒，高饱和度鲜艳色彩",
        "keywords": "Ektar 100，鲜艳色彩，高饱和度"
    },
    "电影级": {
        "name": "电影级数字",
        "description": "Arri Alexa电影级质感，干净锐利，专业画质",
        "keywords": "电影级画质，干净锐利，专业"
    },
    "日系": {
        "name": "日系清新",
        "description": "日系胶片质感，略微偏冷的青色调，清新柔和",
        "keywords": "日系清新，冷调，柔和"
    },
    "复古": {
        "name": "复古怀旧",
        "description": "复古胶片质感，暖黄褪色，明显颗粒感",
        "keywords": "复古怀旧，褪色，胶片颗粒"
    },
    "科技": {
        "name": "科技未来",
        "description": "科技感画质，冷调蓝紫，锐利清晰",
        "keywords": "科技感，冷调，锐利"
    },
    "美食": {
        "name": "美食纪录片",
        "description": "美食纪录片质感，暖调，高饱和度，诱人",
        "keywords": "美食纪录片，暖调，高饱和度"
    },
    "Vlog": {
        "name": "Vlog日常",
        "description": "Vlog日常质感，自然真实，生活化",
        "keywords": "Vlog日常，自然，真实"
    }
}

# 镜头运动（中文）
CAMERA_MOVEMENTS = {
    "固定": "固定镜头，不移动",
    "推进": "镜头缓缓推进，聚焦主体",
    "快速推进": "镜头快速推进，强调冲击",
    "拉远": "镜头缓缓拉远，展现环境",
    "跟随": "镜头跟随主体移动",
    "环绕": "镜头环绕主体旋转",
    "手持": "手持拍摄，轻微晃动",
    "航拍": "无人机航拍视角",
    "俯拍": "俯拍视角",
    "仰拍": "仰拍视角"
}

# 景别（中文）
SHOT_SIZES = {
    "远景": "远景，展现场景全貌",
    "全景": "全景，人物全身及环境",
    "中景": "中景，人物半身",
    "近景": "近景，胸部以上",
    "特写": "特写，面部或局部细节",
    "微距": "微距特写，极近距离"
}

# 光线类型（中文）
LIGHTING_TYPES = {
    "黄金时刻": "黄金时刻，清晨或傍晚的金色阳光，温暖梦幻",
    "蓝调时刻": "蓝调时刻，日落后蓝色天光，宁静忧郁",
    "自然光": "柔和的自然光，真实自然",
    "逆光": "逆光拍摄，轮廓光效果",
    "侧光": "侧光照射，立体感强",
    "影棚光": "专业影棚灯光，柔和均匀",
    "霓虹灯": "多彩霓虹灯光，赛博朋克感",
    "暖光": "暖色光线，温馨氛围",
    "冷光": "冷色光线，冷静氛围"
}

# 风格模板（中文）
STYLE_TEMPLATES = {
    "电影": {
        "keywords": ["电影质感", "浅景深", "戏剧性光线"],
        "film": "portra400"
    },
    "Vlog": {
        "keywords": ["Vlog日常", "自然真实", "手持感"],
        "film": "Vlog"
    },
    "商业": {
        "keywords": ["商业广告", "专业", "干净背景"],
        "film": "电影级"
    },
    "奢华": {
        "keywords": ["奢华感", "高端", "精致"],
        "film": "portra400"
    },
    "科技": {
        "keywords": ["科技感", "未来感", "冷色调"],
        "film": "科技"
    },
    "美食": {
        "keywords": ["美食纪录片", "诱人", "高饱和度"],
        "film": "美食"
    },
    "日系": {
        "keywords": ["日系清新", "治愈", "柔和"],
        "film": "日系"
    },
    "复古": {
        "keywords": ["复古怀旧", "褪色", "胶片感"],
        "film": "复古"
    }
}

def generate_prompt(
    subject: str,
    action: str = "",
    scene: str = "",
    style: str = "电影",
    camera: str = "固定",
    shot_size: str = "",
    lighting: str = "自然光",
    film: str = "",
    quality: str = "4K高清"
) -> str:
    """生成 Seedance 视频提示词（中文）"""
    
    parts = []
    
    # 主体
    parts.append(subject)
    
    # 动作
    if action:
        parts.append(action)
    
    # 场景
    if scene:
        parts.append(scene)
    
    # 景别（可选）
    if shot_size and shot_size in SHOT_SIZES:
        parts.append(SHOT_SIZES[shot_size])
    
    # 镜头运动
    if camera in CAMERA_MOVEMENTS:
        parts.append(CAMERA_MOVEMENTS[camera])
    
    # 光线
    if lighting in LIGHTING_TYPES:
        parts.append(LIGHTING_TYPES[lighting])
    
    # 风格关键词
    if style in STYLE_TEMPLATES:
        parts.extend(STYLE_TEMPLATES[style]["keywords"])
        if not film:
            film = STYLE_TEMPLATES[style]["film"]
    
    # 胶片质感
    if film and film in FILM_PRESETS:
        parts.append(FILM_PRESETS[film]["description"])
    
    # 质量
    parts.append(quality)
    
    return "，".join(parts)

def generate_storyboard(
    title: str,
    duration: int,
    style: str,
    platform: str,
    scenes: List[Dict]
) -> str:
    """生成分镜脚本（中文）"""
    
    output = []
    output.append(f"## 视频标题：{title}")
    output.append(f"时长： {duration}秒 | 风格： {style} | 平台： {platform}")
    output.append("")
    
    # 整体视觉风格
    output.append("### 🎨 整体视觉风格（关键！）")
    if style in STYLE_TEMPLATES:
        film_key = STYLE_TEMPLATES[style].get("film", "portra400")
        if film_key in FILM_PRESETS:
            output.append(f"**胶片质感：** {FILM_PRESETS[film_key]['description']}")
    output.append("**色调基调：** [请根据具体场景填写]")
    output.append("**音乐：** [请根据具体场景填写]")
    output.append("")
    output.append("---")
    output.append("")
    
    # 各分镜
    for i, scene in enumerate(scenes, 1):
        start_time = scene.get("start", 0)
        end_time = scene.get("end", 0)
        phase = scene.get("phase", "")
        theme = scene.get("theme", "")
        
        output.append(f"### 分镜{i}（{start_time}-{end_time}秒）【{phase} - {theme}】")
        output.append("")
        output.append("**画面：**")
        
        shots = scene.get("shots", [])
        for shot in shots:
            shot_size = shot.get("size", "")
            description = shot.get("description", "")
            if shot_size and shot_size in SHOT_SIZES:
                output.append(f"- {shot_size}，{description}")
            else:
                output.append(f"- {description}")
        
        output.append("")
        
        # 胶片质感
        film = scene.get("film", "")
        if film and film in FILM_PRESETS:
            output.append(f"**胶片质感：** {FILM_PRESETS[film]['description']}")
        else:
            output.append("**胶片质感：** [请填写]")
        
        output.append("")
        output.append(f"**配音：** \"{scene.get('voiceover', '')}\"")
        output.append("")
        output.append(f"**音乐/音效：** {scene.get('audio', '')}")
        output.append("")
        output.append("---")
        output.append("")
    
    # 拍摄要点
    output.append("### 📸 拍摄要点：")
    tips = [
        "- [运镜技巧]",
        "- [光线运用]",
        "- [色调统一]",
        "- [音效设计]"
    ]
    output.extend(tips)
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Seedance AI视频提示词生成器（中文版）")
    
    subparsers = parser.add_subparsers(dest="command", help="命令")
    
    # 提示词生成
    prompt_parser = subparsers.add_parser("prompt", help="生成视频提示词")
    prompt_parser.add_argument("--主体", "-s", required=True, dest="subject", help="主体描述")
    prompt_parser.add_argument("--动作", "-a", default="", dest="action", help="动作描述")
    prompt_parser.add_argument("--场景", "-e", default="", dest="scene", help="场景环境")
    prompt_parser.add_argument("--风格", choices=list(STYLE_TEMPLATES.keys()), default="电影", dest="style")
    prompt_parser.add_argument("--镜头", choices=list(CAMERA_MOVEMENTS.keys()), default="固定", dest="camera")
    prompt_parser.add_argument("--景别", choices=list(SHOT_SIZES.keys()), default="", dest="shot_size")
    prompt_parser.add_argument("--光线", choices=list(LIGHTING_TYPES.keys()), default="自然光", dest="lighting")
    prompt_parser.add_argument("--胶片", choices=list(FILM_PRESETS.keys()), default="", dest="film")
    prompt_parser.add_argument("--画质", default="4K高清", dest="quality")
    
    # 分镜脚本
    storyboard_parser = subparsers.add_parser("storyboard", help="生成分镜脚本")
    storyboard_parser.add_argument("--标题", "-t", required=True, dest="title")
    storyboard_parser.add_argument("--时长", "-d", type=int, default=12, dest="duration")
    storyboard_parser.add_argument("--风格", choices=list(STYLE_TEMPLATES.keys()), default="电影", dest="style")
    storyboard_parser.add_argument("--平台", "-p", default="抖音/TikTok", dest="platform")
    
    # 通用选项
    parser.add_argument("--json", action="store_true", help="输出JSON格式")
    parser.add_argument("--列表", choices=["胶片", "镜头", "风格", "光线"], dest="list_type", help="列出可选项")
    
    args = parser.parse_args()
    
    # 列表模式
    if args.list_type:
        if args.list_type == "胶片":
            print("可用胶片风格：")
            for key, value in FILM_PRESETS.items():
                print(f"  {key}: {value['name']}")
        elif args.list_type == "镜头":
            print("可用镜头运动：")
            for key, value in CAMERA_MOVEMENTS.items():
                print(f"  {key}: {value}")
        elif args.list_type == "风格":
            print("可用风格：")
            for key in STYLE_TEMPLATES.keys():
                print(f"  {key}")
        elif args.list_type == "光线":
            print("可用光线类型：")
            for key, value in LIGHTING_TYPES.items():
                print(f"  {key}: {value}")
        return
    
    if args.command == "prompt":
        prompt = generate_prompt(
            subject=args.subject,
            action=args.action,
            scene=args.scene,
            style=args.style,
            camera=args.camera,
            shot_size=args.shot_size,
            lighting=args.lighting,
            film=args.film,
            quality=args.quality
        )
        
        if args.json:
            result = {
                "提示词": prompt,
                "配置": {
                    "主体": args.subject,
                    "动作": args.action,
                    "场景": args.scene,
                    "风格": args.style,
                    "镜头": args.camera,
                    "景别": args.shot_size,
                    "光线": args.lighting,
                    "胶片": args.film,
                    "画质": args.quality
                }
            }
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print("=" * 70)
            print("🎬 Seedance 视频提示词：")
            print("=" * 70)
            print(prompt)
            print("=" * 70)
    
    elif args.command == "storyboard":
        scenes = [
            {
                "start": 0,
                "end": 3,
                "phase": "开场",
                "theme": "引入",
                "shots": [
                    {"size": "中景", "description": "主体出现在画面中"}
                ],
                "voiceover": "开场配音...",
                "audio": "背景音乐开场"
            }
        ]
        
        storyboard = generate_storyboard(
            title=args.title,
            duration=args.duration,
            style=args.style,
            platform=args.platform,
            scenes=scenes
        )
        
        print(storyboard)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
