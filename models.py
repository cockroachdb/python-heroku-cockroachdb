from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import INT

Base = declarative_base()

class Score(Base):
    __tablename__ = 'scores'
    id = Column(UUID, primary_key=True)
    avatar = Column(INT)
    playername = Column(String)
    points = Column(INT)

