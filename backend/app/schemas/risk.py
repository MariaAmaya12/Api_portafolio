from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Literal


class RiskRequest(BaseModel):
    tickers: list[str] = Field(..., min_length=1)
    start_date: str
    end_date: str
    alpha: float = Field(0.95, gt=0.0, lt=1.0)
    n_sim: int = Field(10000, ge=1000)


class RiskResponse(BaseModel):
    portfolio_summary: list[dict]
    kupiec: dict


class GarchRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str


class GarchResponse(BaseModel):
    comparison: list[dict]
    forecast: list[dict]
    diagnostics: list[dict]
    best_model_name: str | None = None
    summary_text: str
