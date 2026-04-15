from __future__ import annotations

from pydantic import BaseModel, Field


class MarketQuery(BaseModel):
    ticker: str = Field(..., min_length=1)
    start_date: str
    end_date: str


class MarketPricesResponse(BaseModel):
    ticker: str
    rows: list[dict]


class MarketReturnsResponse(BaseModel):
    ticker: str
    rows: list[dict]
