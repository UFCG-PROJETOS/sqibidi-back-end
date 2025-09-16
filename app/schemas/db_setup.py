from typing import Annotated
from fastapi import Depends
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .schemas import Base

bd_url = os.environ.get("DATABASE_URL")

engine = create_engine(
    bd_url
    or "postgresql://sqibidi_dev:sqibidi_pwd_bd@localhost:5432/sqibidi_questions_bd"
)


def get_bd():
    """
    Cria uma conexão com o BD,
     commita as mudanças se nenhum erro ocorrer e fecha a conexão depois.
    """
    bd = Session(engine)
    try:
        yield bd
        bd.commit()
    except:
        bd.rollback()
        raise
    finally:
        bd.close()


Base.metadata.create_all(engine)

db_session = Annotated[Session, Depends(get_bd)]
