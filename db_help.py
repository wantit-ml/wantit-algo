from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ARRAY, Boolean, BLOB, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone = Column(String)
    role = Column(String)
    about = relationship("About", backref="users")


class About(Base):
    __tablename__ = "about"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    surname = Column(String)
    city = Column(String)
    birthday = Column(DateTime)
    gender = Column(String)
    citizenships = Column(ARRAY(String))
    rank = Column(String)
    salary = Column(Integer)
    currency = Column(String)
    stack = relationship("Stack", backref="about")
    school = Column(String)
    grade = Column(Integer)
    native_language = Column(String)
    foreign_languages = Column(ARRAY(String))
    can_move = Column(String)
    timetable = relationship("Timetable", backref="about")
    metro_station = Column(String)
    github_id = Column(String)
    vk_id = Column(String, Nullable=True)
    telegram_id = Column(String, Nullable=True)
    achievements = relationship("Achievement", backref="about")


class Timetable(Base):
    __tablename__ = "Timetable"
    id = Column(Integer, primary_key=True)
    day = Column(String)
    times = Column(String)  # e.g. times = ["18:00-19:00", "12:00-13:00" etc]
    about_id = Column(Integer, ForeignKey("about.id"))


class Achievement(Base):
    __tablename__ = "achievements"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    title = Column(String)
    level = Column(String)
    role = Column(String)
    file = Column(BLOB)
    description = Column(String)
    about_id = Column(Integer, ForeignKey("about.id"))


class Stack(Base):
    __tablename__ = "stack"
    id = Column(Integer, primary_key=True)
    about_id = Column(Integer, ForeignKey("about.id"))
    technology = Column(String)
    level = Column(Integer)

class Vacancy():
    __tablename__ = "vacancy"
    id = Column(Integer, primary_key=True)
    stack = relationship("Stack", backref="about")
    foreign_languages = Column(ARRAY(String))
