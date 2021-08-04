from typing import Optional

from pydantic import BaseModel
# class MyModel(BaseModel):
    # class Config:
    #     orm_mode = True

class Bank(BaseModel):
    name: str

class Department(BaseModel):
    name: str


class Employee(BaseModel):
    name: Optional[str]
    age : Optional[int]
    bank : Optional[str]
    department : Optional[str]
    role : Optional[str]
