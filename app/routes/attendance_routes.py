
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models

router = APIRouter(prefix="/attendance", tags=["Attendance"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def mark_attendance(employee_id: int, date: str, status: str, db: Session = Depends(get_db)):
    record = models.Attendance(employee_id=employee_id, date=date, status=status)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/{employee_id}")
def attendance_report(employee_id: int, db: Session = Depends(get_db)):
    return db.query(models.Attendance).filter(models.Attendance.employee_id == employee_id).all()
