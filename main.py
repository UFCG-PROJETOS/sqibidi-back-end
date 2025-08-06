from fastapi import FastAPI

from .app.routers.questoes import questoes_router

app = FastAPI()
app.include_router(questoes_router)
