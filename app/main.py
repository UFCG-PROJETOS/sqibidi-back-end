from fastapi import FastAPI

from .routers.questionsRouter import router as questions_router
from .routers.answersRouter import router as answers_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(questions_router)
app.include_router(answers_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
