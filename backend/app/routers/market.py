from __future__ import annotations

from fastapi import APIRouter, Query

from backend.app.services.market_service import fetch_prices, fetch_returns

router = APIRouter()


@router.get("/prices")
def get_prices(
    ticker: str = Query(...),
    start_date: str = Query(...),
    end_date: str = Query(...),
) -> dict:
    return fetch_prices(ticker=ticker, start_date=start_date, end_date=end_date)


@router.get("/returns")
def get_returns(
    ticker: str = Query(...),
    start_date: str = Query(...),
    end_date: str = Query(...),
) -> dict:
    return fetch_returns(ticker=ticker, start_date=start_date, end_date=end_date)
