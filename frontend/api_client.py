from __future__ import annotations

import os
from typing import Any

import httpx

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


def _handle_response(response: httpx.Response) -> Any:
    response.raise_for_status()
    return response.json()


def get_health() -> dict:
    response = httpx.get(f"{BASE_URL}/health", timeout=30.0)
    return _handle_response(response)


def get_market_prices(ticker: str, start_date: str, end_date: str) -> dict:
    response = httpx.get(
        f"{BASE_URL}/market/prices",
        params={"ticker": ticker, "start_date": start_date, "end_date": end_date},
        timeout=60.0,
    )
    return _handle_response(response)


def get_market_returns(ticker: str, start_date: str, end_date: str) -> dict:
    response = httpx.get(
        f"{BASE_URL}/market/returns",
        params={"ticker": ticker, "start_date": start_date, "end_date": end_date},
        timeout=60.0,
    )
    return _handle_response(response)


def get_macro_snapshot() -> dict:
    response = httpx.get(f"{BASE_URL}/macro/snapshot", timeout=30.0)
    return _handle_response(response)


def get_benchmark_summary(
    tickers: list[str],
    start_date: str,
    end_date: str,
    benchmark_ticker: str = "ACWI",
    rf_annual: float = 0.03,
) -> dict:
    response = httpx.get(
        f"{BASE_URL}/benchmark/summary",
        params={
            "tickers": tickers,
            "start_date": start_date,
            "end_date": end_date,
            "benchmark_ticker": benchmark_ticker,
            "rf_annual": rf_annual,
        },
        timeout=90.0,
    )
    return _handle_response(response)


def post_var_cvar(payload: dict) -> dict:
    response = httpx.post(f"{BASE_URL}/risk/var-cvar", json=payload, timeout=90.0)
    return _handle_response(response)


def post_garch(payload: dict) -> dict:
    response = httpx.post(f"{BASE_URL}/garch/fit", json=payload, timeout=120.0)
    return _handle_response(response)


def post_markowitz(payload: dict) -> dict:
    response = httpx.post(f"{BASE_URL}/portfolio/markowitz", json=payload, timeout=120.0)
    return _handle_response(response)
