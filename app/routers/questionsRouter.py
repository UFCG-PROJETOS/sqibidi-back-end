from fastapi import APIRouter, HTTPException

from app.models.questionDTO import (
    QuestionPutPostRequestDTO,
    QuestionResponseDTO,
    QuestionResponseDTOWithoutAnswer,
)

from ..schemas.db_setup import db_session
from ..schemas.schemas import Question, DailyQuestion

from sqlalchemy import select


router = APIRouter(prefix="/question", tags=["Questions"])


@router.post("/", response_model=QuestionResponseDTO)
def create_question(questionDTO: QuestionPutPostRequestDTO, db: db_session):
    new = Question(
        name=questionDTO.name,
        code=questionDTO.code,
        type_question=questionDTO.type_question,
        expected_answer=questionDTO.expected_answer,
    )
    db.add(new)
    try:
        db.flush()
    except Exception as e:
        raise HTTPException(400, e)
    return new


@router.put("/{id}/", response_model=QuestionResponseDTO)
def update_question(id: int, questionDTO: QuestionPutPostRequestDTO):
    return {
        "id": 123,
        "name": questionDTO.name,
        "code": questionDTO.code,
        "type_question": questionDTO.type_question,
    }


@router.delete("/{id}/")
def remove_question(id: int, db: db_session):
    db.delete(db.get(Question, id))


@router.get("/", response_model=list[QuestionResponseDTO])
def list_questions(db: db_session):
    return db.scalars(select(Question)).all()


@router.get("/day_question/", response_model=QuestionResponseDTOWithoutAnswer)
def get_question_day(db: db_session):
    question = db.scalars(select(DailyQuestion)).first()
    if not question:
        raise HTTPException(404, "No daily question found")
    question = db.get(Question, question.id)
    if not question:
        raise HTTPException(
            404, "Daily question was set to a question that doesn't exist"
        )

    return question


@router.post("/day_question/", response_model=QuestionResponseDTO)
def set_question_day(id: int, db: db_session):
    question = db.get(Question, id)
    if not question:
        raise HTTPException(404, "Question id doesn't exist")

    daily = db.scalars(select(DailyQuestion)).first()
    if daily:
        daily.id = id
    else:
        db.add(DailyQuestion(id=id))

    return question
