from pydantic import BaseModel
from typing import List, Optional
#from fastapi_filter import Filter
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int
    created_at: datetime  # когда была создана задача

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str  # нужна валидация данных Field(@mail\@bk\@gmail...) TODO
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True


#class TaskFilter(Filter):
#    name__in: Optional[list[str]] = Field(alias="names")
#    type__not_in: Optional[list[ProductType]] = Field(alias="types")
#    production_date__gte: Optional[datetime] = Field(alias="productionDatesFrom")
#    quantity__lte: Optional[int] = Field(alias="quantityTo")
    
#    class Constants(Filter.Constants):
#        model = Product

#    class Config:
#        allow_population_by_field_name = True