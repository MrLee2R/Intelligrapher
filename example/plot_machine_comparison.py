#!/usr/bin/env python3
"""
科研绘图：两台机器工序时间对比
模板来源：Intelligrapher / line-plot.py
审美库：civil-engineering（Engineering Structures 风格）
配色：primary=["#1f4e79", "#c55a11"]
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==================== 参数配置区（由 Intelligrapher 注入） ====================
CONFIG = {
    "figsize": (10, 6.5),
    "dpi": 300,
    "palette": ["#1f4e79", "#c55a11"],
    "font_family": ["Times New Roman", "Arial"],
    "title_fontsize": 14,
    "label_fontsize": 12,
    "tick_fontsize": 10,
    "line_width": 1.5,
    "marker_size": 6,
    "xlabel": "Number of Trials",
    "ylabel": "Average Time (s)",
    "title": "Comparison of Average Completion Time: Machine A vs Machine B",
    "legend_loc": "upper left",
    "grid": True,
    "save_path": "D:\\Claude_code\\grapher\\example\\machine_comparison.png",
}

# ==================== 数据加载区（实际数据） ====================
df = pd.read_excel("D:\\Claude_code\\new\\example.xlsx")

x = df["rounds"].values
y1 = df["time_1"].values          # 机器A平均时间
y2 = df["time_2"].values          # 机器B平均时间
var1 = df["time_1_Dev"].values    # 机器A方差
var2 = df["time_2_Dev"].values    # 机器B方差

# 误差带范围：mean ± sqrt(variance)
std1 = np.sqrt(var1)
std2 = np.sqrt(var2)

data_series = [
    {
        "x": x, "y": y1, "y_lower": y1 - std1, "y_upper": y1 + std1,
        "label": "Machine A", "linestyle": "-", "marker": "o",
        "color": CONFIG["palette"][0]
    },
    {
        "x": x, "y": y2, "y_lower": y2 - std2, "y_upper": y2 + std2,
        "label": "Machine B", "linestyle": "--", "marker": "s",
        "color": CONFIG["palette"][1]
    },
]

# ==================== 绘图逻辑 ====================
plt.rcParams["font.family"] = CONFIG["font_family"]
plt.rcParams["axes.unicode_minus"] = False
fig, ax = plt.subplots(figsize=CONFIG["figsize"])

for series in data_series:
    color = series["color"]

    # 绘制误差阴影带（填充区域）
    ax.fill_between(
        series["x"], series["y_lower"], series["y_upper"],
        color=color, alpha=0.15, label="_nolegend_"
    )

    # 绘制主线
    ax.plot(
        series["x"], series["y"], color=color,
        linewidth=CONFIG["line_width"],
        marker=series["marker"],
        markersize=CONFIG["marker_size"],
        markevery=max(1, len(series["x"]) // 8),
        linestyle=series["linestyle"],
        label=series["label"],
        markerfacecolor="white",
        markeredgecolor=color,
        markeredgewidth=1.2,
    )

# 坐标轴设置
ax.set_xlabel(CONFIG["xlabel"], fontsize=CONFIG["label_fontsize"])
ax.set_ylabel(CONFIG["ylabel"], fontsize=CONFIG["label_fontsize"])
ax.set_title(CONFIG["title"], fontsize=CONFIG["title_fontsize"], fontweight="bold", pad=15)

# 网格线（仅 y 轴，淡灰色虚线）
if CONFIG["grid"]:
    ax.grid(True, axis="y", color="#d9d9d9", linewidth=0.5, linestyle="--", zorder=0)

# 图例
ax.legend(
    fontsize=CONFIG["tick_fontsize"],
    loc=CONFIG["legend_loc"],
    framealpha=0.9,
    edgecolor="#cccccc",
)

# 边框：仅保留左、下边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_linewidth(0.8)
ax.spines["bottom"].set_linewidth(0.8)

# 刻度样式
ax.tick_params(axis="both", labelsize=CONFIG["tick_fontsize"], direction="in", length=4)

# x 轴刻度：每隔 10 个单位显示一个刻度
ax.set_xticks(np.arange(20, 121, 10))

# y 轴范围留边距
y_min = min((y1 - std1).min(), (y2 - std2).min())
y_max = max((y1 + std1).max(), (y2 + std2).max())
ax.set_ylim(y_min - 0.3, y_max + 0.3)

plt.tight_layout()

# 保存
if CONFIG["save_path"]:
    plt.savefig(CONFIG["save_path"], dpi=CONFIG["dpi"], bbox_inches="tight")
    print(f"[OK] Image saved to: {CONFIG['save_path']}")

plt.show()
