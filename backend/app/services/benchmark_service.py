from __future__ import annotations

import pandas as pd

from src.download import load_market_bundle
from src.preprocess import equal_weight_portfolio
from src.benchmark import benchmark_summary


def fetch_benchmark_summary(
    tickers: list[str],
    start_date: str,
    end_date: str,
    benchmark_ticker: str = "ACWI",
    rf_annual: float = 0.03,
) -> dict:
    bundle_assets = load_market_bundle(tickers=tickers, start=start_date, end=end_date)
    bundle_benchmark = load_market_bundle(tickers=[benchmark_ticker], start=start_date, end=end_date)

    asset_returns = bundle_assets["returns"]
    benchmark_returns = bundle_benchmark["returns"]

    if asset_returns.empty or benchmark_returns.empty:
        return {
            "summary": [],
            "extras": [],
            "cum_portfolio": [],
            "cum_benchmark": [],
        }

    portfolio_returns = equal_weight_portfolio(asset_returns)
    benchmark_series = benchmark_returns.iloc[:, 0]

    summary_df, extras_df, cum_port, cum_bench = benchmark_summary(
        portfolio_returns=portfolio_returns,
        benchmark_returns=benchmark_series,
        rf_annual=rf_annual,
    )

    return {
        "summary": summary_df.to_dict(orient="records"),
        "extras": extras_df.to_dict(orient="records"),
        "cum_portfolio": cum_port.reset_index().rename(columns={0: "value"}).to_dict(orient="records"),
        "cum_benchmark": cum_bench.reset_index().rename(columns={0: "value"}).to_dict(orient="records"),
    }
