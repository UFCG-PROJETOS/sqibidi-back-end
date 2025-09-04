from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey
from enum import Enum as PyEnum


class Base(DeclarativeBase):
    pass


class typeQuestion(PyEnum):
    SELECT = "SELECT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    CREATE = "CREATE"
    VIEW = "VIEW"


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    code: Mapped[str]
    type_question: Mapped[typeQuestion] = mapped_column(
        Enum(
            typeQuestion,
            name="type_question_enum",
            create_type=True,
            native_enum=True,
        )
    )
    expected_answer: Mapped[str]


class DailyQuestion(Base):
    __tablename__ = "daily_question"
    id: Mapped[int] = mapped_column(ForeignKey(Question.id), primary_key=True)
