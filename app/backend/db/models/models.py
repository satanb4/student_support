# title: models.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-23 19:44:50
# Description: This file contains the Database models for the MyPath application.

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

from pathlib import Path
from app.backend.db.database import DbHandler

Base = declarative_base()


# -- These models are tentative -- #
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    user_type = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    course_code = Column(String, unique=True, index=True)
    course_description = Column(String)
    course_units = Column(Integer)
    course_duration = Column(Integer)
    enrolled_students = Column(Integer)
    course_instructor = Column(String)
    course_status = Column(String)
    course_start_date = Column(String)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    student_email = Column(String)
    student_course = Column(String)
    student_status = Column(String)
    student_start_date = Column(String)
    student_end_date = Column(String)
    user = Column(ForeignKey("users.id"))


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    staff_name = Column(String)
    staff_email = Column(String)
    staff_course = Column(String)
    advisor = Column(Boolean, default=False)
    user = Column(ForeignKey("users.id"))


# -- END -- #

if __name__ == "__main__":
    path = Path(__file__).parent.parent / "test.sqlite3"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{path}"
    db = DbHandler(SQLALCHEMY_DATABASE_URL)
    db.create_all(Base)
    print("Database created")
