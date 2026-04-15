from __future__ import annotations

from src.api.macro import macro_snapshot


def fetch_macro_snapshot() -> dict:
    return macro_snapshot()
