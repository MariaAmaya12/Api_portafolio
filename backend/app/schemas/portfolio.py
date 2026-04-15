from __future__ import annotations

from pydantic import BaseModel, Field


class PortfolioRequest(BaseModel):
    tickers: list[str] = Field(..., min_length=2)
    start_date: str
    end_date: str
    rf_annual: float = 0.03
    n_portfolios: int = Field(5000, ge=1000)


class PortfolioResponse(BaseModel):
    frontier: list[dict]
    min_variance: dict
    max_sharpe: dict
    weights_min_variance: list[dict]
    weights_max_sharpe: list[dict]
