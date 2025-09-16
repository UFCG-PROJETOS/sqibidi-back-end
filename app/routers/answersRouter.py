from fastapi import APIRouter, File, Form, UploadFile, HTTPException, status

from ..schemas.schemas import Question
from ..models.answerDTO import AnswerPostDTO, AnswerResponseDTO
from ..schemas.db_setup import db_session

import io
import polars as pl

router = APIRouter(prefix="/answer", tags=["Answers"])


@router.post("/", response_model=AnswerResponseDTO)
async def answer(
    db: db_session,
    question_id: int = Form(...),
    user_id: int = Form(...),
    file: UploadFile = File(...),
):
    question = db.get(Question, question_id)
    if not question:
        raise HTTPException(400, "Question doesn't exist")

    answer = AnswerPostDTO(question_id=question_id, user_id=user_id)

    if not file.filename.endswith(".csv"):  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="File must be a CSV."
        )

    contents = await file.read()
    try:
        answer_csv = pl.read_csv(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error reading file: {e}"
        )
    correct_answer = pl.from_dict(
        {"name": ["leo", "keven", "ramon"], "age": [18, 20, 22]}
    )
    if correct_answer.equals(answer_csv):
        return {"success": True, "score": 100}
    else:
        return {"success": False, "score": 0}
