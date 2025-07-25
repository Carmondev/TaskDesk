from fastapi import FastAPI
from app.database import engine, Base
from app.api.v1.endpoints import tasks as tasks_endpoint
from app.api.v1.endpoints import users as users_endpoint

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(tasks_endpoint.router, prefix="/api/v1", tags=["tasks"])
app.include_router(users_endpoint.router, prefix="/api/v1", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskDesk API!"}  