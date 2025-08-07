from enum import Enum
from typing import Union
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

class QuestionResponseDTO(BaseModel):
    id: int
    name: str
    code: str
    typeQuestion: typeQuestion