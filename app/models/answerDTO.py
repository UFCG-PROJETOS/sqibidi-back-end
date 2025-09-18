from pydantic import BaseModel


class AnswerPostDTO(BaseModel):
    question_id: int
    answer: list[dict]


class AnswerResponseDTO(BaseModel):
    success: bool
    score: int
