from fastapi import HTTPException
from starlette import status

import schemas
from database import SessionLocal
import jwt
session =SessionLocal()
import models
def get_employee(employee_id:int):
    return session.query(models.Employee).filter(models.Employee.id==employee_id).first()
def get_all_employee():
    return session.query(models.Employee).all()

def add_employee(employee: schemas.Employee):
    db_employee = models.Employee(name=employee.name, age=employee.age, bank=employee.bank, department=employee.department, role=employee.role)
    session.add(db_employee)
    session.commit()
    session.refresh(db_employee)
    return "Done"

def delete_employee(employee_id: int):
    # session.delete(session.query(models.Employee).filter(id==employee_id))
    session.delete(session.query(models.Employee).filter(models.Employee.id==employee_id).first())
    session.commit()

def put_employee(employee:schemas.Employee,employee_id:int):
    try:
        session.query(models.Employee).filter(models.Employee.id==employee_id).update({"name": employee.name,"age":employee.age,"bank":employee.bank,"department":employee.department,"role":employee.role},synchronize_session="fetch")
    except:
        session.rollback()
        return False
    else:
        session.commit()
    return True

def patch_employee(payload:dict,employee_id:int):
    print(payload)
    try:
        session.query(models.Employee).filter(models.Employee.id==employee_id).update(payload,synchronize_session="fetch")
        session.commit()
    except:
        session.rollback()
        return False
    return True

def login_account(username:str,password:str):
    account=session.query(models.Account).filter(models.Account.username==username,models.Account.password==password).first()
    if(account):
        return jwt.encode({"username":account.username,"password":account.password,"role":account.role},"secret",algorithm="HS256",headers={"alg": "HS256"})
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong username or password")
