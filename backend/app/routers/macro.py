from __future__ import annotations

from fastapi import APIRouter

from backend.app.services.macro_service import fetch_macro_snapshot

router = APIRouter()


@router.get("/snapshot")
def get_snapshot() -> dict:
    return fetch_macro_snapshot()
