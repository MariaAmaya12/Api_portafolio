from __future__ import annotations

from fastapi import APIRouter

from backend.app.schemas.portfolio import PortfolioRequest
from backend.app.services.portfolio_service import fetch_markowitz

router = APIRouter()


@router.post("/markowitz")
def post_markowitz(payload: PortfolioRequest) -> dict:
    return fetch_markowitz(
        tickers=payload.tickers,
        start_date=payload.start_date,
        end_date=payload.end_date,
        rf_annual=payload.rf_annual,
        n_portfolios=payload.n_portfolios,
    )
