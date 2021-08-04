from fastapi import FastAPI
from routes import admin
import models, schemas, crud

app=FastAPI()
app.include_router(admin.router)


@app.get("/{employee_id}")
def get_all_employee(employee_id:int):
    return crud.get_employee(employee_id)

@app.get("/getAll")
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
    return crud.put_employee(employee,employee_id)

@app.patch("/patch/{employee_id}")
def patch_empolyee(employee:schemas.Employee,employee_id:int):
    payload=employee.dict(exclude_none=True)
    return crud.patch_employee(payload,employee_id)