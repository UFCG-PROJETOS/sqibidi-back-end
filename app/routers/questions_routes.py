from fastapi import APIRouter

from app.models.questionDTO import QuestionPutPostRequestDTO, QuestionResponseDTO, typeQuestion

router = APIRouter(
    prefix="/question",
    tags=["Items"]
)

@router.post("/", response_model=QuestionResponseDTO)
def create_question(questionDTO: QuestionPutPostRequestDTO):
    return {
            "id": 123,
            "name": questionDTO.name,
            "code": questionDTO.code,
            "typeQuestion": questionDTO.typeQuestion
        }

@router.put("/{id}", response_model=QuestionResponseDTO)
def update_question(id: int, questionDTO: QuestionPutPostRequestDTO):
    return {
            "id": 123,
            "name": questionDTO.name,
            "code": questionDTO.code,
            "typeQuestion": questionDTO.typeQuestion
        }

@router.delete("/{id}")
def remove_question(id: int):
    return None

@router.get("/", response_model=list[QuestionResponseDTO])
def list_questions():
    return [
        {
            "id": 123,
            "name": "teste",
            "code": "teste",
            "typeQuestion": typeQuestion.SELECT
        }
    ]

@router.get("/day_question", response_model=QuestionResponseDTO)
def get_question_day():
    return  {
            "id": 123,
            "name": "teste",
            "code": "teste",
            "typeQuestion": typeQuestion.SELECT
        }