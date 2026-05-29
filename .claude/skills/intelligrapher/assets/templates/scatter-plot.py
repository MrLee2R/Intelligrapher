#!/usr/bin/env python3
"""
模板：散点图 + 回归线
适用：相关性分析、预测值 vs 真实值
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

CONFIG = {
    "figsize": (7, 7), "dpi": 300, "palette": {{COLOR_PALETTE}},
    "font_family": "{{FONT_FAMILY}}", "title_fontsize": {{TITLE_FONTSIZE}},
    "label_fontsize": {{LABEL_FONTSIZE}}, "tick_fontsize": {{TICK_FONTSIZE}},
    "marker_size": {{MARKER_SIZE}}, "alpha": {{ALPHA}},
    "xlabel": "{{XLABEL}}", "ylabel": "{{YLABEL}}", "title": "{{TITLE}}",
    "save_path": "{{SAVE_PATH}}",
}

np.random.seed(42)
x = np.random.randn(50)
y = 2*x + np.random.randn(50)*0.5

plt.rcParams["font.family"] = CONFIG["font_family"]
fig, ax = plt.subplots(figsize=CONFIG["figsize"])
ax.scatter(x, y, c=CONFIG["palette"][0], s=CONFIG["marker_size"], alpha=CONFIG["alpha"],
           edgecolors="black", linewidth=0.5, label="Data")
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
x_line = np.array([x.min(), x.max()])
y_line = slope*x_line + intercept
ax.plot(x_line, y_line, color=CONFIG["palette"][1], linewidth=2, linestyle="--",
        label=f"Fit: $R^2={r_value**2:.3f}$")
ax.axline((0,0), slope=1, color="gray", linewidth=0.8, linestyle=":", label="1:1")
ax.set_xlabel(CONFIG["xlabel"], fontsize=CONFIG["label_fontsize"])
ax.set_ylabel(CONFIG["ylabel"], fontsize=CONFIG["label_fontsize"])
ax.set_title(CONFIG["title"], fontsize=CONFIG["title_fontsize"], fontweight="bold")
ax.legend(fontsize=CONFIG["tick_fontsize"])
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
if CONFIG["save_path"]: plt.savefig(CONFIG["save_path"], dpi=CONFIG["dpi"], bbox_inches="tight")
plt.show()
