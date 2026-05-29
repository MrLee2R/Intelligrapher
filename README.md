# Intelligrapher

> 搞科研的都知道，画一张能直接往论文里塞的图，比跑实验还折腾。配色丑了审稿人不乐意，坐标轴单位标错了被打回来重画，更崩溃的是每次都要从零写 matplotlib 代码——时间都花在调 `plt.rcParams` 上了。
>
> 这个项目就是想解决这个痛点。

Intelligrapher 是一套给 Claude Code 用的科研绘图 Skill。它内置了三套东西：知识库（告诉你这个领域图该怎么画）、审美库（顶刊配色直接拿来用）、模板库（不用从零写代码）。三样东西配合，你的需求进去，可运行的 Python 脚本出来。

![example/comparison.png](https://github.com/MrLee2R/Intelligrapher/blob/main/example/comparison.png)

上图就是用 Intelligrapher 生成的实际效果——从数据到成图，一句话的事。深蓝实线是机器 A，砖红虚线是机器 B，阴影带表示方差范围，配色来自 Engineering Structures 的风格库。

\---

## 这玩意到底能干啥

一句话：**你描述需求，它给你代码**。

比如你跟 Claude 说：

```
/intelligrapher 画一张分组柱状图，对比三组材料的抗压强度，
风格用 Geotechnique 的配色，误差棒标上，保存为 PDF
```

Claude 会：

1. 从知识库里查出"材料强度对比"该用什么单位（MPa）、坐标轴怎么标
2. 从审美库里捞出 Geotechnique 风格的色板（蓝、橙、灰那套）
3. 从模板库里取出 `bar-chart.py` 的骨架
4. 把色板和规范填进占位符，吐出一整段可直接运行的 Python 代码

全程你不用碰 matplotlib 文档。

\---

## 这个项目中的三个库是怎么配合的

```
你的一句话需求
        │
        ▼
┌──────────────────────────────────────┐
│ 1. 解析需求 → domain + figure\_type    │
│ 2. 查知识库 → 坐标轴规范、标注符号    │
│ 3. 查审美库 → 色板、字体、线宽        │
│ 4. 取模板   → matplotlib 代码骨架     │
│ 5. 填空     → 注入参数 → 完整脚本     │
└──────────────────────────────────────┘
        │
        ▼
   直接运行的 .py 文件
```

三个库各司其职：

* **知识库**（`references/knowledge/`）：每个领域一份 markdown，告诉你这个圈子里图该怎么画。土木工程默认自带，医学也有一份示例。内容包括常用图表类型、坐标轴规范、领域特殊要求（比如滞回曲线必须闭合、生存曲线要标 n=...）。
* **审美库**（`references/aesthetic/`）：每份对应一个领域的主流顶刊，配色方案从论文里提取的。比如土木工程这套，主色 `#1f4e79` 深蓝、`#c55a11` 砖红，来自 Engineering Structures 的实际用色统计。
* **模板库**（`assets/templates/`）：5 份 `.py` 文件，顶部带 `CONFIG` 字典和 `{{...}}` 占位符。Claude 生成代码时会把占位符替换成具体值。模板本身就能直接跑，自带示例数据。

\---

## 安装

克隆到项目根目录就行：

```bash
cd your-project/
git clone https://github.com/YOUR\_USERNAME/Intelligrapher.git .claude/
```

或者手动把 `.claude/skills/` 下的两个目录复制到你的项目里。重启 Claude Code 对话后生效。

\---

## 使用方式

装上之后，直接跟 Claude 说话就行，不用记命令。

|你想干什么|怎么说|
|-|-|
|画图|`/intelligrapher 帮我画一张...`|
|换领域|`/intelligrapher-updater 切换到医学领域`|
|加新领域|`/intelligrapher-updater 初始化 materials-science 材料科学`|
|换配色|`/intelligrapher-updater 更新 aesthetic 为 Nature 风格`|

两个 Skill 是联动的。Claude 会根据你说的话自动判断该调用主 Skill 还是 Updater，不需要你指定。

\---

## 目前内置了什么

**知识库（领域规范）**

|领域|覆盖内容|状态|
|-|-|-|
|土木工程|滞回曲线、骨架曲线、应力-应变、弯矩图、固结曲线等|默认|
|医学|Kaplan-Meier、ROC、森林图、热图、瀑布图|示例|

**审美库（顶刊配色）**

|领域|参考期刊|主色板|
|-|-|-|
|土木工程|Engineering Structures, J. Struct. Eng., Geotechnique|`#1f4e79`, `#c55a11`, `#70ad47`|
|医学|The Lancet, NEJM, Nature Medicine, JAMA, BMJ|`#004b87`, `#b8321a`, `#287c37`|

**模板库（代码骨架）**

|模板|图表|适用场景|
|-|-|-|
|`line-plot.py`|折线图 + 误差带|时间序列、机器对比、滞回骨架|
|`bar-chart.py`|分组柱状图 + 误差棒|材料强度对比、分类数据|
|`heatmap.py`|热图|相关性矩阵、基因表达|
|`scatter-plot.py`|散点图 + 回归线|相关性分析、预测验证|
|`box-plot.py`|箱线图|统计分布、异常值|

\---

## 🎓 提示词教程：怎么跟 Intelligrapher 说话最有效

很多人用 AI 画图，提示词写得不好，出来的东西总差点意思。这里整理了一套基于 Intelligrapher 内部机制的提示词写法，照着来，一次到位。

### 1\. 基础公式

一个完整的绘图请求，最好包含这 5 个要素：

```
画一张 \[图表类型]，\[数据描述]，\[坐标轴/标签要求]，\[风格要求]，\[输出要求]
```

**✅ 好的示例：**

```
/intelligrapher 画一张折线图，对比两台机器在 20-120 次试验中的平均完成时间，
带误差阴影带，x轴标 Number of Trials，y轴标 Average Time (s)，
Engineering Structures 风格，深蓝和砖红配色，保存为 300 DPI 的 PNG
```

**❌ 不太好的示例：**

```
帮我画个图
```

太模糊了，Claude 不知道你想要什么，只能猜。猜错了你得来回改，浪费 token。

### 2\. 领域指定技巧

Intelligrapher 默认走土木工程的规范。如果你做别的领域，有三种方式切换：

**方式 A：临时覆盖（一句话）**

```
/intelligrapher 用医学领域的规范画一张 Kaplan-Meier 生存曲线...
```

**方式 B：切换默认领域（持久）**

```
/intelligrapher-updater 切换到医学领域
```

之后所有请求默认走医学规范，直到你再次切换。

**方式 C：初始化新领域**

```
/intelligrapher-updater 初始化 materials-science 材料科学
```

会在知识库和审美库下生成骨架文件，你自己填内容。

### 3\. 风格控制技巧

配色方案来自审美库，有几种调用方式：

|你的说法|Intelligrapher 怎么做|
|-|-|
|"Engineering Structures 风格"|读取 `aesthetic/civil-engineering.md`|
|"Lancet 风格"|读取 `aesthetic/medicine.md`|
|"Nature 风格"|如果存在 `aesthetic/nature.md` 就读，否则临时构造|
|"用蓝色和橙色"|临时构造色板，不读审美库|
|"配色要色盲友好"|读取 `guidelines/color-theory.md`，避开红绿组合|

**技巧：** 如果你常投某个期刊，建议直接初始化该期刊的审美库文件，以后直接说期刊名就行。

### 4\. 数据相关技巧

**有数据文件的情况：**

```
/intelligrapher 数据在 D:\\\\data\\\\results.xlsx，第一列是时间，第二列是温度，
画一张折线图...
```

Claude 会读取实际数据，确保代码里的数据路径正确。

**没数据文件、需要示例数据的情况：**

```
/intelligrapher 画一张箱线图，假设有 4 组数据，每组 200 个样本...
```

模板自带随机数据，你可以直接跑起来看效果，再替换成自己的。

**数据格式检查：**

Intelligrapher 内置了 `validate\_data.py`，会根据你选的图表类型检查数据列是否齐全。比如选 `bar-chart` 需要 `category` 和 `value` 列，如果缺少会提示你。

### 5\. 输出格式控制

```
保存为 SVG             ← 矢量图，适合论文插图
保存为 PDF             ← 矢量图，适合 LaTeX
保存为 PNG，300 DPI    ← 位图，适合 PPT
保存为 TIFF，600 DPI   ← 高位图，适合印刷
同时输出 SVG + PNG     ← 两种格式各一份
```

### 6\. 进阶：直接修改模板

如果你发现某个图表类型 Intelligrapher 没有覆盖，可以：

1. 找一个最接近的模板复制一份
2. 改名叫 `your-figure.py`
3. 顶部保留 `CONFIG` 字典和 `{{...}}` 占位符
4. 更新 `templates/README.md`

下次就能直接调用：

```
/intelligrapher 用 your-figure 模板画一张...
```

### 7\. 常见踩坑

|坑|原因|解决|
|-|-|-|
|中文乱码|字体不支持中文|在提示词里加"用 SimHei 字体"或直接说"中文标签"|
|颜色太艳|用了默认 matplotlib 色板|明确说"顶刊配色"或指定审美库|
|图太大/太小|figsize 不合适|说"单栏图宽"或"双栏图宽"，Intelligrapher 会自动换算|
|坐标轴单位不对|知识库没加载|明确指定领域，如"土木工程的规范"|

\---

## 目录结构速览

```
.claude/skills/
├── intelligrapher/
│   ├── skill.md                       # 核心入口
│   ├── .current-domain                # 当前领域标记
│   ├── assets/
│   │   └── templates/                 # 5 份 .py 模板
│   │       ├── line-plot.py
│   │       ├── bar-chart.py
│   │       ├── heatmap.py
│   │       ├── scatter-plot.py
│   │       └── box-plot.py
│   ├── references/
│   │   ├── knowledge/                 # 领域图表规范
│   │   │   ├── civil-engineering.md
│   │   │   └── medicine.md
│   │   ├── aesthetic/                 # 顶刊配色方案
│   │   │   ├── civil-engineering.md
│   │   │   └── medicine.md
│   │   └── guidelines/                # 通用绘图指南
│   │       ├── color-theory.md        # 色盲友好、WCAG 对比度
│   │       ├── journal-styles.md      # Elsevier/Springer/Nature 排版
│   │       └── figure-types.md        # 图表类型决策树
│   └── scripts/
│       ├── apply\_aesthetic.py         # 配色注入
│       └── validate\_data.py           # 数据格式检查
│
└── intelligrapher-updater/
    ├── skill.md                       # 更新器入口
    ├── assets/
    │   └── knowledge-skeleton.md      # 新领域骨架
    ├── references/
    │   ├── update-protocol.md         # 安全更新流程
    │   ├── domain-registry.md         # 领域注册表
    │   └── schema-spec.md             # 格式校验标准
    └── scripts/
        ├── init\_domain.py             # 初始化新领域
        ├── switch\_domain.py           # 切换默认领域
        └── validate\_structure.py      # 结构校验
```

\---

## 扩展：加一个新领域

假设你是计算机视觉方向的，想要一套 CVPR/ICCV 风格的配色和图表规范。

**Step 1 — 初始化骨架：**

```
/intelligrapher-updater 初始化 computer-vision 计算机视觉
```

这会生成两个空文件：`knowledge/computer-vision.md` 和 `aesthetic/computer-vision.md`。

**Step 2 — 填知识库：**

打开 `knowledge/computer-vision.md`，按这四个板块填：

* **常用图表类型**：PR 曲线、mAP 对比表、混淆矩阵、注意力热力图...
* **坐标轴规范**：横轴一般是 epoch / iteration / 阈值，纵轴是 accuracy / mAP / IoU
* **标注符号表**：IoU、mAP@0.5、AP50、F1-score 这些符号怎么写
* **领域特殊要求**：比如 PR 曲线必须标 baseline、对比实验必须标星号显著性

**Step 3 — 填审美库：**

打开 `aesthetic/computer-vision.md`：

* **目标期刊**：CVPR、ICCV、ECCV、TPAMI
* **主色板**：去 CVPR 近几年的论文里吸色，或者用这套默认的：`#1f4e79`, `#c55a11`, `#70ad47`
* **辅助色板**：灰阶，用于背景和网格
* **字体字号**： conferences 通常要求 sans-serif，如 Helvetica 或 Arial
* **线型标记**：线宽 1.5，标记循环 `o`, `s`, `D`

**Step 4 — 校验：**

```bash
python .claude/skills/intelligrapher-updater/scripts/validate\_structure.py \\
    .claude/skills/intelligrapher/references/knowledge/computer-vision.md knowledge
```

通过了就能用了。

\---

## 一些你可能想知道的

**Q：修改 skill 文件后要重启 Claude Code 吗？**

项目级 Skill 是即时生效的。改完 `.claude/skills/` 下的文件，**重启当前对话**就行，不需要重新打包上传。这是比 ZIP 包方式最爽的地方。

**Q：Claude 没自动触发 Intelligrapher 怎么办？**

可能是 `skill.md` 里的 `description` 写得不够像用户请求。你可以去 `intelligrapher/skill.md` 里加一些触发词，比如 "matplotlib 科研图"、"seaborn 可视化"、"顶刊配色"、"论文插图"。

**Q：模板里的占位符都有哪些？**

全部列在这里：

|占位符|类型|说明|
|-|-|-|
|`{{COLOR\_PALETTE}}`|JSON 数组|主色板，如 `\["#1f4e79", "#c55a11"]`|
|`{{FONT\_FAMILY}}`|字符串|字体族|
|`{{TITLE\_FONTSIZE}}`|整数|标题字号|
|`{{LABEL\_FONTSIZE}}`|整数|轴标签字号|
|`{{TICK\_FONTSIZE}}`|整数|刻度字号|
|`{{LINE\_WIDTH}}`|浮点数|线宽|
|`{{MARKER\_SIZE}}`|浮点数|标记大小|
|`{{BAR\_WIDTH}}`|浮点数|柱宽|
|`{{ALPHA}}`|浮点数|透明度|
|`{{XLABEL}}`, `{{YLABEL}}`|字符串|坐标轴标签|
|`{{TITLE}}`|字符串|图标题|
|`{{LEGEND\_LOC}}`|字符串|图例位置|
|`{{SAVE\_PATH}}`|字符串|保存路径|
|`{{GRID}}`|布尔值|是否显示网格|
|`{{ANNOT}}`|布尔值|热图是否标注数值|
|`{{CMAP}}`|字符串|热图 colormap|
|`{{FMT}}`|字符串|热图数值格式|

**Q：怎么调试用？**

生成的代码里加一行 `print(CONFIG)`，就能看到所有占位符的最终值。

\---

## 贡献

欢迎 PR 和 Issue。如果你搞了一个新领域的知识库或者一套新配色，直接提 PR 就行。有几个方向特别缺人：

* **更多领域**：物理、化学、生物、经济学... 只要是发论文需要画图的领域都欢迎
* **更多模板**：森林图、小提琴图、桑基图、三维图...
* **更多顶刊配色**：Nature Methods、Science、Cell 等

提 PR 的时候记得更新 `domain-registry.md`。

\---

## License

MIT。随便用，改也行，商用也行，但出问题别找我（虽然大概率不会出问题）。

\---

<p align="center">
  <i>画好看的图，让审稿人少挑点毛病。</i>
</p>

