from __future__ import annotations

from fastapi import APIRouter

from backend.app.schemas.risk import GarchRequest
from backend.app.services.garch_service import fetch_garch_fit

router = APIRouter()


@router.post("/fit")
def post_garch(payload: GarchRequest) -> dict:
    return fetch_garch_fit(
        ticker=payload.ticker,
        start_date=payload.start_date,
        end_date=payload.end_date,
    )
