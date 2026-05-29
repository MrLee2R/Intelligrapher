# 模板库索引

## 占位符说明
所有 `.py` 模板顶部包含 `CONFIG` 字典，使用双花括号 `{{...}}` 作为占位符，由 Intelligrapher 在生成代码时替换为具体值。

## 模板清单
| 文件名 | 图表类型 | 适用场景 |
|--------|----------|----------|
| `line-plot.py` | 折线图 | 时间序列、滞回骨架线 |
| `bar-chart.py` | 分组柱状图 | 材料对比、分类数据 |
| `heatmap.py` | 热图 | 相关性、基因表达 |
| `scatter-plot.py` | 散点图+回归 | 相关性、预测验证 |
| `box-plot.py` | 箱线图 | 统计分布、异常值 |

## 占位符列表
- `{{COLOR_PALETTE}}`, `{{FONT_FAMILY}}`, `{{TITLE_FONTSIZE}}`, `{{LABEL_FONTSIZE}}`, `{{TICK_FONTSIZE}}`
- `{{LINE_WIDTH}}`, `{{MARKER_SIZE}}`, `{{BAR_WIDTH}}`, `{{ALPHA}}`
- `{{XLABEL}}`, `{{YLABEL}}`, `{{TITLE}}`, `{{LEGEND_LOC}}`, `{{SAVE_PATH}}`
- `{{GRID}}`, `{{ANNOT}}`, `{{CMAP}}`, `{{FMT}}`
