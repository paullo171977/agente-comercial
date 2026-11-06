from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import pages

app = FastAPI(
    title="Agente Comercial IA",
    description="Sistema de prospecção e qualificação de leads",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pages.router)
