#!/usr/bin/env python3
"""
切换默认领域。
"""

import sys
import os

MARKER = os.path.join(os.path.dirname(__file__), "..", "..", "intelligrapher", ".current-domain")

def switch(domain_id: str):
    with open(MARKER, "w", encoding="utf-8") as f:
        f.write(domain_id)
    print(f"Default domain switched to: {domain_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: switch_domain.py <domain_id>"); sys.exit(1)
    switch(sys.argv[1])
