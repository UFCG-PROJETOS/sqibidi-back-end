from pydantic import BaseModel, ConfigDict

from ..schemas.schemas import typeQuestion


class QuestionPutPostRequestDTO(BaseModel):
    name: str
    code: str
    type_question: typeQuestion
    expected_answer: list[dict]
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Questão pra reprovar quem tá pagando BD",
                "code": "INSERT ...",
                "type_question": "SELECT",
                "expected_answer": [
                    {"id": 1, "idade": 10, "nome": "Fulano"},
                    {"id": 2, "idade": 20, "nome": "Cicrano"},
                ],
            }
        }
    )


class QuestionResponseDTO(BaseModel):
    id: int
    name: str
    code: str
    type_question: typeQuestion
    expected_answer: list[dict]
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Questão pra reprovar quem tá pagando BD",
                "code": "INSERT ...",
                "type_question": "SELECT",
                "expected_answer": [
                    {"id": 1, "idade": 10, "nome": "Fulano"},
                    {"id": 2, "idade": 20, "nome": "Cicrano"},
                ],
            }
        }
    )


class QuestionResponseDTOWithoutAnswer(BaseModel):
    id: int
    name: str
    code: str
    type_question: typeQuestion
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Questão pra reprovar quem tá pagando BD",
                "code": "INSERT ...",
                "type_question": "SELECT",
            }
        }
    )
