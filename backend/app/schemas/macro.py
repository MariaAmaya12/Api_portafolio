from __future__ import annotations

from pydantic import BaseModel


class MacroSnapshotResponse(BaseModel):
    risk_free_rate_pct: float | None = None
    inflation_yoy: float | None = None
    cop_per_usd: float | None = None
    usdcop_market: float | None = None
    source: str | None = None
    last_updated: str | None = None
