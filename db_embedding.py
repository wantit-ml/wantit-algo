from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Vector(Base):
    __tablename__ = "vector"
    id = Column(Integer, primary_key=True)
    word = Column(String)
    coords = Column(String)


engine = create_engine("sqlite:///vectors.db")

Base.metadata.bind = engine
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
vectors_db = DBSession()
