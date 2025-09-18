from fastapi import APIRouter, HTTPException

from ..schemas.schemas import Question
from ..models.answerDTO import AnswerPostDTO, AnswerResponseDTO
from ..schemas.db_setup import db_session


router = APIRouter(prefix="/answer", tags=["Answers"])


@router.post("/", response_model=AnswerResponseDTO)
async def answer(db: db_session, answer: AnswerPostDTO):
    question = db.get(Question, answer.question_id)
    if not question:
        raise HTTPException(400, "Question doesn't exist")

    if answer.answer == question.expected_answer:
        return {"success": True, "score": 100}
    else:
        return {"success": False, "score": 0}
