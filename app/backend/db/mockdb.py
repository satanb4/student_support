# title: operations.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-23 19:44:07
# Description: This file contains the database operations for the FastAPI application.
# TODO: DELETE this file after the database models are implemented.

import datetime
from pydantic import BaseModel, Field
from random import choice
from faker import Faker

# -- This is just for Testing purposes --


class userModel(BaseModel):
    # Sample model to use until we have a database
    id: int
    username: str
    email: str
    user_type: str


users = [
    userModel(
        id=1, username="John Doe", email="johndoe@example.com", user_type="staff"
    ),
    userModel(
        id=2, username="Jane Doe", email="janedoe@example.com", user_type="student"
    ),
    userModel(
        id=3, username="John Smith", email="johnsmith@example.com", user_type="staff"
    ),
]

school = ["School of Engineering", "School of Science", "School of Business"]
year = [f"{i}" for i in range(2024, 2027)]
support = ["Yes", "No"]
branch = ["CSE", "ECE", "ME", "CE", "EE"]
advisors = ["Dr. Alyson", "Dr. Brian", "Dr. Claire", "Dr. Desmond", "Dr. Elysse"]
students = [
    {
        "id": i,
        "name": f"Student{i}",
        "year": choice(year),
        "branch": choice(branch),
        "advisor": choice(advisors),
        "support": choice(support),
        "school": choice(school),
    }
    for i in range(1, 200)
]


eng_courses = [
    "Introduction to Python",
    "Introduction to Macroeconomics",
    "Advanced Numerical Simulations",
    "Differential Equations",
    "Introduction to Quantum Mechanics",
    "Introduction to Data Science",
]
sci_courses = [
    "Introduction to Biology",
    "Introduction to Chemistry",
    "Introduction to Physics",
    "Introduction to Mathematics",
    "Introduction to Astronomy",
    "Introduction to Geology",
]
bus_courses = [
    "Introduction to Business",
    "Introduction to Marketing",
]
courses = (
    [
        {
            "id": i,
            "name": eng_courses[i],
            "year": choice(year),
            "branch": choice(branch),
            "professor": choice(advisors),
            "school": "School of Engineering",
        }
        for i in range(len(eng_courses))
    ]
    + [
        {
            "id": len(eng_courses) + i,
            "name": sci_courses[i],
            "year": choice(year),
            "branch": choice(branch),
            "professor": choice(advisors),
            "school": "School of Science",
        }
        for i in range(len(sci_courses))
    ]
    + [
        {
            "id": len(eng_courses) + len(sci_courses) + i,
            "name": bus_courses[i],
            "year": choice(year),
            "branch": choice(branch),
            "professor": choice(advisors),
            "school": "School of Business",
        }
        for i in range(len(bus_courses))
    ]
)

work_types = ["Assignment", "Project", "Quiz", "Exam"]
work_status = ["Pending", "In Progress", "Completed"]

calendar = [
    {
        "id": i,
        "name": f"Work {i}",
        "type": choice(work_types),
        "status": choice(work_status),
        "due_date": f"{choice(year)}-12-31",
    }
    for i in range(1, 17)
]


# -- This is just for Testing purposes --
# -- END -- #
