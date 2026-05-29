#!/usr/bin/env python3
"""
模板：箱线图
适用：多组分布对比、异常值识别
"""

import matplotlib.pyplot as plt
import numpy as np

CONFIG = {
    "figsize": (8, 6), "dpi": 300, "palette": {{COLOR_PALETTE}},
    "font_family": "{{FONT_FAMILY}}", "title_fontsize": {{TITLE_FONTSIZE}},
    "label_fontsize": {{LABEL_FONTSIZE}}, "tick_fontsize": {{TICK_FONTSIZE}},
    "xlabel": "{{XLABEL}}", "ylabel": "{{YLABEL}}", "title": "{{TITLE}}",
    "save_path": "{{SAVE_PATH}}",
}

np.random.seed(42)
data_groups = [np.random.normal(100, 10, 200), np.random.normal(110, 15, 200),
               np.random.normal(95, 8, 200), np.random.normal(120, 20, 200)]
labels = ["Control", "Treatment A", "Treatment B", "Treatment C"]

plt.rcParams["font.family"] = CONFIG["font_family"]
fig, ax = plt.subplots(figsize=CONFIG["figsize"])
bp = ax.boxplot(data_groups, labels=labels, patch_artist=True, widths=0.6,
                showmeans=True, meanline=True,
                meanprops={"color":"black","linestyle":"-","linewidth":1.5},
                medianprops={"color":"white","linewidth":2},
                whiskerprops={"color":"black","linewidth":1},
                capprops={"color":"black","linewidth":1},
                flierprops={"marker":"o","markerfacecolor":"none","markersize":4,"alpha":0.5})
for patch, color in zip(bp["boxes"], CONFIG["palette"]):
    patch.set_facecolor(color); patch.set_edgecolor("black"); patch.set_linewidth(0.8)
ax.set_xlabel(CONFIG["xlabel"], fontsize=CONFIG["label_fontsize"])
ax.set_ylabel(CONFIG["ylabel"], fontsize=CONFIG["label_fontsize"])
ax.set_title(CONFIG["title"], fontsize=CONFIG["title_fontsize"], fontweight="bold")
ax.set_xticklabels(labels, fontsize=CONFIG["tick_fontsize"])
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
if CONFIG["save_path"]: plt.savefig(CONFIG["save_path"], dpi=CONFIG["dpi"], bbox_inches="tight")
plt.show()
