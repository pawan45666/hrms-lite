
from fastapi import FastAPI
from .database import Base, engine
from .routes import employee_routes, attendance_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite Full Assignment")

app.include_router(employee_routes.router)
app.include_router(attendance_routes.router)

@app.get("/")
def home():
    return {"message": "HRMS Lite API Running"}
