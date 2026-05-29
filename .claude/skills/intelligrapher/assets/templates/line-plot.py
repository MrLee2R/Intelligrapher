#!/usr/bin/env python3
"""
模板：多序列折线图
适用：时间序列、滞回骨架线、对比曲线
"""

import matplotlib.pyplot as plt
import numpy as np

# ==================== 参数配置区（由 Skill 替换） ====================
CONFIG = {
    "figsize": (8, 6),
    "dpi": 300,
    "palette": {{COLOR_PALETTE}},
    "font_family": "{{FONT_FAMILY}}",
    "title_fontsize": {{TITLE_FONTSIZE}},
    "label_fontsize": {{LABEL_FONTSIZE}},
    "tick_fontsize": {{TICK_FONTSIZE}},
    "line_width": {{LINE_WIDTH}},
    "marker_size": {{MARKER_SIZE}},
    "xlabel": "{{XLABEL}}",
    "ylabel": "{{YLABEL}}",
    "title": "{{TITLE}}",
    "legend_loc": "{{LEGEND_LOC}}",
    "grid": {{GRID}},
    "save_path": "{{SAVE_PATH}}",
}

# ==================== 数据加载区（用户替换） ====================
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
data_series = [
    {"x": x, "y": y1, "label": "Series A", "linestyle": "-", "marker": "o"},
    {"x": x, "y": y2, "label": "Series B", "linestyle": "--", "marker": "s"},
]

# ==================== 绘图逻辑 ====================
plt.rcParams["font.family"] = CONFIG["font_family"]
plt.rcParams["axes.unicode_minus"] = False
fig, ax = plt.subplots(figsize=CONFIG["figsize"])

for idx, series in enumerate(data_series):
    color = CONFIG["palette"][idx % len(CONFIG["palette"])]
    ax.plot(series["x"], series["y"], color=color,
            linewidth=CONFIG["line_width"], marker=series.get("marker"),
            markersize=CONFIG["marker_size"], markevery=max(1, len(series["x"])//10),
            linestyle=series.get("linestyle", "-"), label=series["label"])

ax.set_xlabel(CONFIG["xlabel"], fontsize=CONFIG["label_fontsize"])
ax.set_ylabel(CONFIG["ylabel"], fontsize=CONFIG["label_fontsize"])
ax.set_title(CONFIG["title"], fontsize=CONFIG["title_fontsize"], fontweight="bold")
if CONFIG["grid"]:
    ax.grid(True, axis="y", color="#d9d9d9", linewidth=0.5, linestyle="--")
ax.legend(fontsize=CONFIG["tick_fontsize"], loc=CONFIG["legend_loc"])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
if CONFIG["save_path"]:
    plt.savefig(CONFIG["save_path"], dpi=CONFIG["dpi"], bbox_inches="tight")
plt.show()
