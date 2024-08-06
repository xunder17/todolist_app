from pydantic import BaseModel
from typing import List, Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode: True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode: True
