"""Compatibility shim: expose has_cycle and find_cycle as hw03.main

The real implementations live in the top-level `main.py` in this repo
so we import and re-export them here to satisfy tests that do
`from hw03.main import has_cycle, find_cycle`.
"""

from main import has_cycle, find_cycle

__all__ = ["has_cycle", "find_cycle"]
