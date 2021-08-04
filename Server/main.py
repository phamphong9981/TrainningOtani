from fastapi import FastAPI, Header
import crud
from routes import admin, employee
app=FastAPI()
app.include_router(admin.router)
app.include_router(employee.router)
@app.get("/login",tags=["login"])
def login(username:str, password:str):
    return crud.login_account(username,password)