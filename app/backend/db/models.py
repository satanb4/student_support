# title: models.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-31 20:19:14
# Description: This file declares the models for the Database used in the MyPath Application. Edit this file to add new models or modify existing ones.

from enum import Enum
from typing import Optional, List
from sqlmodel import SQLModel, Field


class UserType(str, Enum):
    """
    Enum class to define the User Types in the application.
    """

    student = "student"
    staff = "staff"
    admin = "admin"


class User(SQLModel, table=True):
    """
    Model class to define the User Table in the Database.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    user_type: UserType


class Courses(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    course_name: str
    course_code: str
    course_description: str
    course_units: int
    course_instructor: str
    students_enrolled: int
    course_duration: int
