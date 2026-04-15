from __future__ import annotations

from fastapi import APIRouter, Query

from backend.app.services.benchmark_service import fetch_benchmark_summary

router = APIRouter()


@router.get("/summary")
def get_summary(
    tickers: list[str] = Query(...),
    start_date: str = Query(...),
    end_date: str = Query(...),
    benchmark_ticker: str = Query("ACWI"),
    rf_annual: float = Query(0.03),
) -> dict:
    return fetch_benchmark_summary(
        tickers=tickers,
        start_date=start_date,
        end_date=end_date,
        benchmark_ticker=benchmark_ticker,
        rf_annual=rf_annual,
    )
