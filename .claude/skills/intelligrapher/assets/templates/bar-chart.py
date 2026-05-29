#!/usr/bin/env python3
"""
模板：分组柱状图
适用：材料强度对比、分类数据比较
"""

import matplotlib.pyplot as plt
import numpy as np

CONFIG = {
    "figsize": (8, 6), "dpi": 300, "palette": {{COLOR_PALETTE}},
    "font_family": "{{FONT_FAMILY}}", "title_fontsize": {{TITLE_FONTSIZE}},
    "label_fontsize": {{LABEL_FONTSIZE}}, "tick_fontsize": {{TICK_FONTSIZE}},
    "bar_width": {{BAR_WIDTH}}, "xlabel": "{{XLABEL}}", "ylabel": "{{YLABEL}}",
    "title": "{{TITLE}}", "save_path": "{{SAVE_PATH}}",
}

categories = ["Group 1", "Group 2", "Group 3", "Group 4"]
values_a = [23, 45, 56, 78]
values_b = [19, 38, 48, 65]
x = np.arange(len(categories))

plt.rcParams["font.family"] = CONFIG["font_family"]
fig, ax = plt.subplots(figsize=CONFIG["figsize"])
ax.bar(x - CONFIG["bar_width"]/2, values_a, CONFIG["bar_width"], label="A",
       color=CONFIG["palette"][0], edgecolor="black", linewidth=0.5)
ax.bar(x + CONFIG["bar_width"]/2, values_b, CONFIG["bar_width"], label="B",
       color=CONFIG["palette"][1], edgecolor="black", linewidth=0.5)
ax.errorbar(x - CONFIG["bar_width"]/2, values_a, yerr=[2,3,4,5], fmt="none", ecolor="black", capsize=3)
ax.errorbar(x + CONFIG["bar_width"]/2, values_b, yerr=[1.5,2.5,3,4], fmt="none", ecolor="black", capsize=3)
ax.set_xlabel(CONFIG["xlabel"], fontsize=CONFIG["label_fontsize"])
ax.set_ylabel(CONFIG["ylabel"], fontsize=CONFIG["label_fontsize"])
ax.set_title(CONFIG["title"], fontsize=CONFIG["title_fontsize"], fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(categories, fontsize=CONFIG["tick_fontsize"])
ax.legend(fontsize=CONFIG["tick_fontsize"])
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
if CONFIG["save_path"]: plt.savefig(CONFIG["save_path"], dpi=CONFIG["dpi"], bbox_inches="tight")
plt.show()
