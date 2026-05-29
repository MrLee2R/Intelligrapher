#!/usr/bin/env python3
"""
模板：热图
适用：相关性矩阵、基因表达、敏感性分析
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

CONFIG = {
    "figsize": (8, 7), "dpi": 300, "cmap": "{{CMAP}}", "font_family": "{{FONT_FAMILY}}",
    "title_fontsize": {{TITLE_FONTSIZE}}, "tick_fontsize": {{TICK_FONTSIZE}},
    "title": "{{TITLE}}", "xlabel": "{{XLABEL}}", "ylabel": "{{YLABEL}}",
    "annot": {{ANNOT}}, "fmt": "{{FMT}}", "save_path": "{{SAVE_PATH}}",
}

np.random.seed(42)
data = np.random.randn(10, 10)
data = (data + data.T) / 2
np.fill_diagonal(data, 1.0)
labels = [f"Var{i+1}" for i in range(10)]

plt.rcParams["font.family"] = CONFIG["font_family"]
fig, ax = plt.subplots(figsize=CONFIG["figsize"])
sns.heatmap(data, cmap=CONFIG["cmap"], annot=CONFIG["annot"], fmt=CONFIG["fmt"],
            linewidths=0.5, linecolor="white", square=True,
            xticklabels=labels, yticklabels=labels,
            cbar_kws={"shrink": 0.8, "label": "Correlation"}, ax=ax)
ax.set_title(CONFIG["title"], fontsize=CONFIG["title_fontsize"], fontweight="bold", pad=20)
ax.set_xlabel(CONFIG["xlabel"], fontsize=CONFIG["tick_fontsize"])
ax.set_ylabel(CONFIG["ylabel"], fontsize=CONFIG["tick_fontsize"])
plt.tight_layout()
if CONFIG["save_path"]: plt.savefig(CONFIG["save_path"], dpi=CONFIG["dpi"], bbox_inches="tight")
plt.show()
