from __future__ import annotations

from fastapi import APIRouter

from backend.app.schemas.risk import RiskRequest
from backend.app.services.risk_service import fetch_var_cvar

router = APIRouter()


@router.post("/var-cvar")
def post_var_cvar(payload: RiskRequest) -> dict:
    return fetch_var_cvar(
        tickers=payload.tickers,
        start_date=payload.start_date,
        end_date=payload.end_date,
        alpha=payload.alpha,
        n_sim=payload.n_sim,
    )
