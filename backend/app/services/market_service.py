from __future__ import annotations

import pandas as pd

from src.api.market import get_prices
from src.preprocess import simple_returns


def fetch_prices(ticker: str, start_date: str, end_date: str) -> dict:
    df = get_prices(ticker=ticker, start=start_date, end=end_date)
    out = df.reset_index()
    out.columns = [str(c) for c in out.columns]
    return {
        "ticker": ticker,
        "rows": out.to_dict(orient="records"),
    }


def fetch_returns(ticker: str, start_date: str, end_date: str) -> dict:
    df = get_prices(ticker=ticker, start=start_date, end=end_date)

    price_col = "Adj Close" if "Adj Close" in df.columns else "Close"
    returns = simple_returns(pd.to_numeric(df[price_col], errors="coerce").dropna())
    out = returns.reset_index()
    out.columns = ["Date", "return"]
    return {
        "ticker": ticker,
        "rows": out.to_dict(orient="records"),
    }
