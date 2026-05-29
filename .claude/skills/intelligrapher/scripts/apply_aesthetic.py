#!/usr/bin/env python3
"""
将审美库配色注入模板。
"""

import json
import sys

def apply_aesthetic(template_path: str, palette_json: str, output_path: str):
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()
    palette = json.loads(palette_json)
    primary = palette.get("primary", [])
    content = content.replace("{{COLOR_PALETTE}}", json.dumps(primary))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Aesthetic applied: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: apply_aesthetic.py <template.py> <palette.json> <output.py>")
        sys.exit(1)
    apply_aesthetic(sys.argv[1], sys.argv[2], sys.argv[3])
