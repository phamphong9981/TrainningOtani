from pydantic import BaseModel
class Bank(BaseModel):
    name: str
    class Config:
        orm_mode = True

class Department(BaseModel):
    name: str
    class Config:
        orm_mode = True

class Employee(BaseModel):
    name: str=""
    age : int=0
    bank : str=""
    department : str=""
    role : str=""
    class Config:
        orm_mode = True