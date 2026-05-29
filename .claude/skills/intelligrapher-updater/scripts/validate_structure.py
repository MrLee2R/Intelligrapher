#!/usr/bin/env python3
"""
校验知识库和审美库结构。
"""

import sys
import os
import re
import json

REQ_K = ["## 常用图表类型", "## 坐标轴规范", "## 标注符号表", "## 领域特殊要求"]
REQ_A = ["## 目标期刊列表", "## 主色板（Primary）", "## 辅助色板（Secondary）",
         "## 背景与网格建议", "## 字体与字号", "## 线型与标记规范"]

def validate(file_path: str, ftype: str) -> dict:
    report = {"file": file_path, "valid": True, "errors": [], "warnings": []}
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if ftype == "knowledge":
        for h in REQ_K:
            if h not in content:
                report["errors"].append(f"Missing heading: {h}"); report["valid"] = False
    elif ftype == "aesthetic":
        for h in REQ_A:
            if h not in content:
                report["errors"].append(f"Missing heading: {h}"); report["valid"] = False
        for block in re.findall(r"```json\n(.*?)\n```", content, re.DOTALL):
            try:
                data = json.loads(block)
                for key in ["primary", "secondary"]:
                    if key in data:
                        for c in data[key]:
                            if not re.match(r"^#[0-9A-Fa-f]{6}$", c):
                                report["warnings"].append(f"Invalid HEX: {c}")
            except json.JSONDecodeError as e:
                report["errors"].append(f"JSON error: {e}"); report["valid"] = False
    return report

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: validate_structure.py <file> <knowledge|aesthetic>"); sys.exit(1)
    res = validate(sys.argv[1], sys.argv[2])
    print(json.dumps(res, indent=2, ensure_ascii=False))
    sys.exit(0 if res["valid"] else 1)
