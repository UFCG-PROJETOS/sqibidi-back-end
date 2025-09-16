from pydantic import BaseModel

from ..schemas.schemas import typeQuestion


class QuestionPutPostRequestDTO(BaseModel):
    name: str
    code: str
    type_question: typeQuestion
    expectedAnswer: str


class QuestionResponseDTO(BaseModel):
    id: int
    name: str
    code: str
    type_question: typeQuestion
