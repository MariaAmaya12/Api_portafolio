from __future__ import annotations

from fastapi import FastAPI

from backend.app.routers import benchmark, garch, health, macro, market, portfolio, risk
from backend.app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend FastAPI para el proyecto de teoría del riesgo.",
)

app.include_router(health.router, tags=["Health"])
app.include_router(market.router, prefix="/market", tags=["Market"])
app.include_router(macro.router, prefix="/macro", tags=["Macro"])
app.include_router(benchmark.router, prefix="/benchmark", tags=["Benchmark"])
app.include_router(risk.router, prefix="/risk", tags=["Risk"])
app.include_router(garch.router, prefix="/garch", tags=["GARCH"])
app.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])
