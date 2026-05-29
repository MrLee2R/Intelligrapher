#!/usr/bin/env python3
"""
初始化新领域骨架。
"""

import sys
import os

SKILL_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "intelligrapher")
KNOWLEDGE_DIR = os.path.join(SKILL_DIR, "references", "knowledge")
AESTHETIC_DIR = os.path.join(SKILL_DIR, "references", "aesthetic")

K_SKELETON = """# {domain_name} 科研绘图知识库

## 常用图表类型
<!-- 列出本领域最常用的 5-10 种图表 -->

## 坐标轴规范
<!-- 单位、量纲、对数/线性坐标的使用场景 -->

## 标注符号表
<!-- 本领域特有的符号、缩写、图例规范 -->

## 领域特殊要求
<!-- 审稿人常关注的绘图细节、行业惯例 -->
"""

A_SKELETON = """# {domain_name} 顶刊审美库

## 目标期刊列表
<!-- 列出本领域 3-5 个顶刊 -->

## 主色板（Primary）
```json
{{
  "primary": ["#1f4e79", "#c55a11", "#70ad47"],
  "names": ["主色1", "主色2", "主色3"]
}}
```

## 辅助色板（Secondary）
```json
{{
  "secondary": ["#a6a6a6", "#d9d9d9"],
  "names": ["辅助灰1", "辅助灰2"]
}}
```

## 背景与网格建议
<!-- 背景色、网格线颜色、是否显示网格 -->

## 字体与字号
<!-- 建议字体族、标题字号、轴标签字号 -->

## 线型与标记规范
<!-- 线宽、标记大小、标记样式序列 -->
"""

def init_domain(domain_id: str, domain_name: str):
    k_path = os.path.join(KNOWLEDGE_DIR, f"{domain_id}.md")
    with open(k_path, "w", encoding="utf-8") as f:
        f.write(K_SKELETON.format(domain_name=domain_name))
    print(f"Created: {k_path}")
    a_path = os.path.join(AESTHETIC_DIR, f"{domain_id}.md")
    with open(a_path, "w", encoding="utf-8") as f:
        f.write(A_SKELETON.format(domain_name=domain_name))
    print(f"Created: {a_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: init_domain.py <domain_id> <domain_name>"); sys.exit(1)
    init_domain(sys.argv[1], sys.argv[2])
