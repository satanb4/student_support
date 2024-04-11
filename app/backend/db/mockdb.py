# title: operations.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-23 19:44:07
# Description: This file contains the database operations for the FastAPI application.

from pydantic import BaseModel, Field
from random import choice

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

year = [f"{i}" for i in range(2000, 2023)]
support = ["Yes", "No"]
branch = ["CSE", "ECE", "ME", "CE", "EE"]
advisors = ["Dr. A", "Dr. B", "Dr. C", "Dr. D", "Dr. E"]
students = [
    {
        "id": i,
        "name": f"Student{i}",
        "year": choice(year),
        "branch": choice(branch),
        "advisor": choice(advisors),
        "support": choice(support),
    }
    for i in range(1,200)
]


# -- This is just for Testing purposes --
# -- END -- #
