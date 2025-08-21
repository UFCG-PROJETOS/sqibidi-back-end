from pydantic import BaseModel


class AnswerPostDTO(BaseModel):
    questionID: int
    userID: int
    answer: str


class AnswerResponseDTO(BaseModel):
    success: bool
    score: int
