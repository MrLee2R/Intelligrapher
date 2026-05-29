# 医学顶刊审美库

## 目标期刊列表
- *The Lancet*
- *New England Journal of Medicine*（NEJM）
- *Nature Medicine*
- *JAMA*
- *BMJ*

## 主色板（Primary）
```json
{
  "primary": ["#004b87", "#b8321a", "#287c37", "#7b3f98", "#d97828"],
  "names": ["Lancet蓝", "警示红", "临床绿", "紫", "橙"]
}
```

## 辅助色板（Secondary）
```json
{
  "secondary": ["#8da9c4", "#e8e8e8", "#f5f5f5"],
  "names": ["淡蓝灰", "分隔灰", "背景灰"]
}
```

## 背景与网格建议
- 背景：`#ffffff`。
- 网格：NEJM 不显示；Lancet 可显示极淡 y 轴网格 `#e8e8e8`。
- 边框：四边框保留（NEJM 极简可隐藏上、右）。

## 字体与字号
- 字体：Helvetica 或 Arial（无衬线优先）。
- 标题：13-14 pt，常规字重。
- 轴标签：11-12 pt；刻度：9-10 pt；图例：9 pt，外置。

## 线型与标记规范
- 线宽：1.0-1.5 pt（医学偏好细线）。
- 标记：4-5 pt，样式循环 `o`, `s`, `^`, `D`。
- 生存曲线删失标记：`+` 或 `|`，大小 4 pt。
