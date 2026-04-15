from __future__ import annotations

from src.download import load_market_bundle
from src.markowitz import (
    efficient_frontier,
    maximum_sharpe_portfolio,
    minimum_variance_portfolio,
    simulate_portfolios,
    weights_table,
)


def fetch_markowitz(
    tickers: list[str],
    start_date: str,
    end_date: str,
    rf_annual: float = 0.03,
    n_portfolios: int = 5000,
) -> dict:
    bundle = load_market_bundle(tickers=tickers, start=start_date, end=end_date)
    returns_df = bundle["returns"]

    sim_df = simulate_portfolios(
        returns_df=returns_df,
        rf_annual=rf_annual,
        n_portfolios=n_portfolios,
    )

    if sim_df.empty:
        return {
            "frontier": [],
            "min_variance": {},
            "max_sharpe": {},
            "weights_min_variance": [],
            "weights_max_sharpe": [],
        }

    frontier = efficient_frontier(sim_df)
    min_var = minimum_variance_portfolio(sim_df)
    max_sharpe = maximum_sharpe_portfolio(sim_df)
    min_weights = weights_table(min_var) if not min_var.empty else None
    max_weights = weights_table(max_sharpe) if not max_sharpe.empty else None

    return {
        "frontier": frontier.to_dict(orient="records") if not frontier.empty else [],
        "min_variance": min_var.to_dict() if not min_var.empty else {},
        "max_sharpe": max_sharpe.to_dict() if not max_sharpe.empty else {},
        "weights_min_variance": min_weights.to_dict(orient="records") if min_weights is not None and not min_weights.empty else [],
        "weights_max_sharpe": max_weights.to_dict(orient="records") if max_weights is not None and not max_weights.empty else [],
    }
