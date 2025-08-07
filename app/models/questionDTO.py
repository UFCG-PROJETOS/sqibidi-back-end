from enum import Enum
from pydantic import BaseModel


class typeQuestion(str, Enum):
    SELECT = "SELECT"
    UPDATE = "UPDATE"
    DELELE = "DELETE"
    CRETE = "CREATE"
    VIEW = "VIEW"


class QuestionPutPostRequestDTO(BaseModel):
    name: str
    code: str
    typeQuestion: typeQuestion
    expectedAnswer: str


class QuestionResponseDTO(BaseModel):
    id: int
    name: str
    code: str
    typeQuestion: typeQuestion
