# AI视频生成工具提示词技巧

## 通用提示词结构

```
[主体] + [动作/运动] + [环境/场景] + [风格/氛围] + [技术参数]
```

示例：
```
A golden retriever [主体] 
running happily through a sunlit meadow [动作]
with wildflowers and distant mountains [环境]
cinematic style, warm golden hour lighting [风格]
4K, high detail, shallow depth of field [技术参数]
```

---

## 主流AI视频工具

### 1. OpenAI Sora

**特点**：
- 支持长提示词（详细描述）
- 物理真实感强
- 复杂场景理解能力好
- 支持视频到视频编辑

**提示词技巧**：
- 详细描述场景和动作
- 强调物理真实感
- 指定镜头运动方式
- 描述光影和氛围

**示例提示词**：
```
A stylish woman walks down a Tokyo street filled with warm glowing neon 
and animated city signage. She wears a black leather jacket, a long red 
dress, and black boots. She walks confidently and casually. The street 
is damp and reflective, creating a colorful mirror of the neon lights. 
Cinematic lighting, shallow depth of field, shot on 35mm film.
```

---

### 2. Runway Gen-2 / Gen-3

**特点**：
- 艺术风格强
- 支持风格迁移
- 图生视频效果好
- Motion Brush 精细控制

**提示词技巧**：
- 强调艺术风格
- 使用风格参考词
- 控制运动幅度（motion scale）
- 配合图片输入效果更好

**示例提示词**：
```
A dreamlike sequence of clouds morphing into faces, surreal artistic style, 
soft pastel colors, gentle floating motion, ethereal atmosphere, 
impressionist painting aesthetic
```

---

### 3. Pika Labs

**特点**：
- 适合动画/卡通风格
- 简洁提示词即可
- 支持图片动画化
- 3D风格效果好

**提示词技巧**：
- 简洁明了
- 强调动画风格
- 描述主要动作
- 指定风格类型

**示例提示词**：
```
Cute cartoon cat playing with a ball of yarn, 3D animation style, 
playful and energetic, bright colors, smooth motion
```

---

### 4. Kling（可灵）

**特点**：
- 中文理解好
- 适合中国元素
- 人物动作自然
- 支持文生视频和图生视频

**提示词技巧**：
- 可用中文描述
- 加入中国元素
- 描述人物表情动作
- 指定场景氛围

**示例提示词**：
```
一位穿着汉服的年轻女子在古色古香的庭院中漫步，春风拂面，
樱花飘落，阳光透过树叶洒下斑驳光影，画面唯美浪漫，
电影质感，4K高清
```

---

### 5. Seedance（火山引擎）

**特点**：
- 商业场景适配
- 中文友好
- 有声视频支持
- 产品展示效果好

**提示词技巧**：
- 商业化描述
- 产品特点突出
- 专业感
- 配合音频更佳

**示例提示词**：
```
Premium skincare product on marble surface, soft studio lighting, 
elegant rotation, professional commercial style, clean background, 
subtle reflections, luxury feel
```

---

## 提示词优化技巧

### 1. 主体描述要具体

❌ 弱：A person walking
✅ 强：A young woman in a red dress walking gracefully through a garden

### 2. 动作描述要生动

❌ 弱：The dog moves
✅ 强：The golden retriever runs joyfully, tail wagging, ears flopping

### 3. 环境描述要有层次

❌ 弱：Outside
✅ 强：A sunlit meadow at golden hour, wildflowers swaying in the breeze, 
distant mountains silhouetted against a warm sky

### 4. 风格描述要明确

| 风格 | 关键词 |
|------|--------|
| 电影感 | cinematic, film look, anamorphic, shallow depth of field |
| 纪录片 | documentary style, handheld, natural lighting |
| 动画 | animated, cartoon, 3D animation, stylized |
| 复古 | vintage, film grain, retro aesthetic, nostalgic |
| 科幻 | futuristic, sci-fi, cyberpunk, neon, holographic |
| 商业 | commercial, product showcase, studio lighting, clean |

### 5. 技术参数建议

| 参数 | 推荐值 |
|------|--------|
| 分辨率 | 4K, 8K, high resolution |
| 镜头 | wide angle, telephoto, macro |
| 景深 | shallow depth of field, bokeh |
| 帧率 | slow motion, 60fps, 120fps |
| 光线 | golden hour, soft lighting, dramatic lighting |

---

## 场景模板

### 人物肖像

```
[人物描述], [服装], [表情/姿态], [场景], [光线], [镜头], [风格]

示例：
A confident young professional woman, wearing a navy blazer, 
smiling warmly, in a modern office with large windows, 
natural soft lighting, medium shot, professional corporate style, 4K
```

### 产品展示

```
[产品], [位置], [光线], [运动], [背景], [氛围], [质量]

示例：
Luxury watch on velvet cushion, rotating slowly, 
soft studio lighting with subtle reflections, 
clean black background, elegant and premium feel, 8K commercial quality
```

### 自然风景

```
[场景], [时间], [天气], [动态元素], [镜头运动], [氛围], [质量]

示例：
Mountain lake at sunrise, clear sky with morning mist, 
gentle ripples on water, camera slowly panning right, 
peaceful and serene, 4K cinematic
```

### 城市街景

```
[地点], [时间], [人流/车流], [建筑], [光线], [风格], [质量]

示例：
Tokyo street at night, busy with pedestrians, 
neon signs and tall buildings, 
rain-slicked streets reflecting colorful lights, 
cyberpunk aesthetic, 4K high detail
```

### 动物/宠物

```
[动物], [动作], [场景], [表情], [光线], [风格], [质量]

示例：
Playful golden retriever chasing a ball in a sunny park, 
happy expression, tail wagging, 
golden hour lighting, cinematic slow motion, 4K
```

---

## 常见问题解决

### 画面模糊

添加关键词：
- sharp focus
- high detail
- crystal clear
- 4K/8K resolution

### 动作不自然

- 简化动作描述
- 添加 "smooth motion", "natural movement"
- 分解为简单动作

### 风格不对

- 明确指定风格关键词
- 添加参考词如 "in the style of..."
- 使用风格对比词

### 光线不好

指定光线类型：
- golden hour lighting
- soft diffused lighting
- dramatic side lighting
- studio lighting
- natural daylight

---

## 高级技巧

### 1. 镜头运动描述

| 运动方式 | 英文描述 |
|----------|----------|
| 推镜头 | dolly in, zoom in, push in |
| 拉镜头 | dolly out, zoom out, pull back |
| 左右摇 | pan left/right |
| 上下摇 | tilt up/down |
| 跟随 | follow shot, tracking shot |
| 环绕 | orbit, circling around |
| 升降 | crane shot, rising/falling |

### 2. 转场效果

| 转场 | 描述 |
|------|------|
| 淡入淡出 | fade in/out |
| 叠化 | dissolve, crossfade |
| 划像 | wipe |
| 缩放 | zoom transition |
| 模糊 | blur transition |

### 3. 情绪氛围

| 情绪 | 关键词 |
|------|--------|
| 欢快 | joyful, cheerful, uplifting, vibrant |
| 悲伤 | melancholic, somber, emotional, touching |
| 紧张 | tense, suspenseful, dramatic, intense |
| 浪漫 | romantic, dreamy, intimate, tender |
| 神秘 | mysterious, enigmatic, atmospheric, eerie |
| 史诗 | epic, grand, majestic, awe-inspiring |
