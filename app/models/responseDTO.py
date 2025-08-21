from pydantic import BaseModel


class AnswerPostDTO(BaseModel):
    questionID: int
    userID: int


class AnswerResponseDTO(BaseModel):
    success: bool
    score: int
