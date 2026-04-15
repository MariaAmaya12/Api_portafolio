from __future__ import annotations

import pandas as pd

from src.download import download_single_ticker
from src.preprocess import log_returns
from src.garch_models import fit_garch_models


def fetch_garch_fit(ticker: str, start_date: str, end_date: str) -> dict:
    df = download_single_ticker(ticker=ticker, start=start_date, end=end_date)
    if df.empty:
        return {
            "comparison": [],
            "forecast": [],
            "diagnostics": [],
            "best_model_name": None,
            "summary_text": "No fue posible descargar datos para el activo.",
        }

    price_col = "Adj Close" if "Adj Close" in df.columns else "Close"
    series = pd.to_numeric(df[price_col], errors="coerce").dropna()
    returns = log_returns(series)

    results = fit_garch_models(returns)

    return {
        "comparison": results["comparison"].to_dict(orient="records") if not results["comparison"].empty else [],
        "forecast": results["forecast"].to_dict(orient="records") if not results["forecast"].empty else [],
        "diagnostics": results["diagnostics"].to_dict(orient="records") if not results["diagnostics"].empty else [],
        "best_model_name": results.get("best_model_name"),
        "summary_text": results.get("summary_text", ""),
    }
