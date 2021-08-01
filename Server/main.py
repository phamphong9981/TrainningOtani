from typing import Optional

from fastapi import FastAPI, Path
from sqlalchemy.orm import Session
import models, schemas, crud

app=FastAPI()

@app.get("/")
def get_all_employee():
    return crud.get_all_employee()

@app.post("/add")
def add_empoloyee(employee: schemas.Employee):
    return crud.add_employee(employee)

@app.delete("/{employee_id}")
def delete_employee(employee_id: int):
    return crud.delete_employee(employee_id)

@app.put("/update/{employee_id}")
def update_employee(employee: schemas.Employee,employee_id:int):
    return crud.update_employee(employee,employee_id)

@app.patch("/patch/{employee_id}")
def patch_empolyee(employee:schemas.Employee,employee_id:int):
    return crud.patch_employee(employee,employee_id)