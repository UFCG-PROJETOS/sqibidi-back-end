from fastapi import APIRouter
from app.models.responseDTO import AnswerPostDTO, AnswerResponseDTO

router = APIRouter(prefix="/answer", tags=["Answers"])


@router.post("/", response_model=AnswerResponseDTO)
def answer(answer: AnswerPostDTO):
    return {"success": True, "score": 100}
