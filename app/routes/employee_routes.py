
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models

router = APIRouter(prefix="/employees", tags=["Employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_employee(name: str, department: str, db: Session = Depends(get_db)):
    emp = models.Employee(name=name, department=department)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

@router.get("/")
def list_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()
