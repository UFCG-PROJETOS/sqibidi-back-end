from pydantic import BaseModel


class AnswerPostDTO(BaseModel):
    question_id: int
    user_id: int


class AnswerResponseDTO(BaseModel):
    success: bool
    score: int
