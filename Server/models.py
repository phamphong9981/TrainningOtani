from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    bank = Column(String)
    department = Column(String)
    role = Column(String)
