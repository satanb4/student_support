# title: schemas.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-23 19:44:23
# Description: This file contains the Pydantic schemas for the Database models.

from pydantic import BaseModel


# -- These schemas are tentative -- #
class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


# -- END -- #
