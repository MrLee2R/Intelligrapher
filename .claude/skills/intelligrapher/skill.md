---
name: intelligrapher
description: 科研绘图智能助手。当用户需要科研绘图、数据可视化、配色建议、期刊风格调整、生成 matplotlib 或 seaborn 绘图代码、或询问某专业领域图表规范时触发。支持多领域与顶刊审美，输出可直接运行的 Python 脚本。
dependencies: matplotlib, seaborn, numpy, pandas, scipy
user-invocable: true
---

# Intelligrapher

## Overview
本 Skill 通过「知识库 + 审美库 + 模板库」三库协同，将用户的科研绘图需求转化为可直接运行的 Python 代码。

## 三库机制
1. **知识库（Knowledge）**：`${SKILL_DIR}/references/knowledge/{domain}.md`，包含领域图表规范。默认 domain 为 `civil-engineering`。
2. **审美库（Aesthetic）**：`${SKILL_DIR}/references/aesthetic/{journal}.md`，包含顶刊配色、字体、线型规范。
3. **模板库（Template）**：`${SKILL_DIR}/assets/templates/{figure_type}.py`，包含参数化 Python 模板。

## 工作流程
1. **需求解析**：从用户输入提取 `$domain`（默认 civil-engineering）、`$journal`（默认 default）、`$figure_type`、`$data_description`。
2. **领域匹配**：读取 `references/knowledge/${domain}.md`，获取坐标轴规范、标注符号、领域特殊要求。
3. **审美选择**：读取 `references/aesthetic/${journal}.md`，获取主色板、辅助色板、字体、线宽。
4. **模板调用**：从 `assets/templates/${figure_type}.py` 加载基础代码框架。
5. **代码生成**：将审美库色板、知识库规范注入模板占位符，输出完整 Python 脚本。

## 占位符规范（模板内使用双花括号）
- `{{COLOR_PALETTE}}`：JSON 数组，如 ["#1f4e79", "#c55a11"]
- `{{FONT_FAMILY}}`：字体族字符串
- `{{TITLE_FONTSIZE}}`, `{{LABEL_FONTSIZE}}`, `{{TICK_FONTSIZE}}`：整数
- `{{LINE_WIDTH}}`, `{{MARKER_SIZE}}`, `{{BAR_WIDTH}}`, `{{ALPHA}}`：浮点数
- `{{XLABEL}}`, `{{YLABEL}}`, `{{TITLE}}`, `{{LEGEND_LOC}}`, `{{SAVE_PATH}}`：字符串
- `{{GRID}}`, `{{ANNOT}}`：布尔值（True/False）
- `{{CMAP}}`, `{{FMT}}`：字符串

## 约束
- 所有生成代码必须基于 matplotlib / seaborn，确保可复现。
- 配色必须严格引用审美库中的 HEX 值，禁止随意编造。
- 若 `$domain` 对应的知识库文件不存在，提示用户："该领域知识库未初始化，请使用 /intelligrapher-updater 并执行 init 操作。"
