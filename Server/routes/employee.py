from fastapi import APIRouter, Depends, HTTPException, Header

import crud
import schemas
from dependencies.is_valid_account import is_valid_account

router = APIRouter(
    prefix="/employee",
    tags=["employee"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(is_valid_account)]
)
@router.get("/{employee_id}")
def get_all_employee(employee_id:int):
    return crud.get_employee(employee_id)

@router.get("/getAll")
def get_all_employee():
    return crud.get_all_employee()

@router.post("/add")
def add_empoloyee(employee: schemas.Employee):
    return crud.add_employee(employee)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int):
    return crud.delete_employee(employee_id)

@router.put("/update/{employee_id}")
def update_employee(employee: schemas.Employee,employee_id:int):
    return crud.put_employee(employee,employee_id)

@router.patch("/patch/{employee_id}")
def patch_empolyee(employee:schemas.Employee,employee_id:int):
    payload=employee.dict(exclude_none=True)
    return crud.patch_employee(payload,employee_id)