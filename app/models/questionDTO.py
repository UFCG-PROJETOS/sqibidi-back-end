from pydantic import BaseModel

from ..schemas.schemas import typeQuestion


class QuestionPutPostRequestDTO(BaseModel):
    name: str
    code: str
    type_question: typeQuestion
    expected_answer: list[dict]


class QuestionResponseDTO(BaseModel):
    id: int
    name: str
    code: str
    type_question: typeQuestion
    expected_answer: list[dict]


class QuestionResponseDTOWithoutAnswer(BaseModel):
    id: int
    name: str
    code: str
    type_question: typeQuestion
