from fastapi import FastAPI

from app.routers.questions_routes import router as questions_router

app = FastAPI()
app.include_router(questions_router)
