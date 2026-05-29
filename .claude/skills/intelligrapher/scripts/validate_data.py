#!/usr/bin/env python3
"""
数据格式预检。
"""

import sys
import json

def validate(data_description: dict, template_name: str) -> dict:
    report = {"valid": True, "warnings": [], "errors": []}
    required_map = {
        "line-plot": ["x","y"], "bar-chart": ["category","value"],
        "heatmap": ["matrix"], "scatter-plot": ["x","y"], "box-plot": ["groups"]
    }
    required = required_map.get(template_name, [])
    user_cols = data_description.get("columns", [])
    for col in required:
        if col not in user_cols:
            report["errors"].append(f"Missing required column: '{col}' for '{template_name}'")
            report["valid"] = False
    if data_description.get("missing", 0) > data_description.get("rows", 1) * 0.05:
        report["warnings"].append("Missing value ratio > 5%.")
    return report

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: validate_data.py '<json_description>' <template_name>"); sys.exit(1)
    desc = json.loads(sys.argv[1])
    print(json.dumps(validate(desc, sys.argv[2]), indent=2, ensure_ascii=False))
