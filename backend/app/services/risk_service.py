from __future__ import annotations

import numpy as np

from src.download import load_market_bundle
from src.preprocess import equal_weight_portfolio, equal_weight_vector
from src.risk_metrics import (
    historical_var_cvar,
    kupiec_test,
    monte_carlo_var_cvar,
    parametric_var_cvar,
    risk_comparison_table,
)


def fetch_var_cvar(
    tickers: list[str],
    start_date: str,
    end_date: str,
    alpha: float = 0.95,
    n_sim: int = 10000,
) -> dict:
    bundle = load_market_bundle(tickers=tickers, start=start_date, end=end_date)
    returns_df = bundle["returns"]

    if returns_df.empty:
        return {"portfolio_summary": [], "kupiec": {}}

    portfolio_returns = equal_weight_portfolio(returns_df)
    weights = equal_weight_vector(returns_df.shape[1])

    comparison = risk_comparison_table(
        portfolio_returns=portfolio_returns,
        asset_returns_df=returns_df,
        weights=weights,
        alpha=alpha,
        n_sim=n_sim,
    )

    hist = historical_var_cvar(portfolio_returns, alpha=alpha)
    kupiec = {}
    if hist:
        kupiec = kupiec_test(portfolio_returns, var=hist["VaR_diario"], alpha=alpha)

    return {
        "portfolio_summary": comparison.to_dict(orient="records"),
        "kupiec": kupiec,
    }
