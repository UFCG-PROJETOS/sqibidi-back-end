from fastapi import FastAPI

from app.routers.questionsRouter import router as questions_router
from app.routers.answersRouter import router as answers_router

app = FastAPI()
app.include_router(questions_router)
app.include_router(answers_router)
