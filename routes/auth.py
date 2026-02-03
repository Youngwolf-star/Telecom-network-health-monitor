from fastapi import APIRouter
from models import User
from database import SessionLocal
from passlib.hash import bcrypt

router = APIRouter()

@router.post("/signup")
def signup(email: str, password: str):
    db = SessionLocal()
    user = User(email=email, password=bcrypt.hash(password))
    db.add(user)
    db.commit()
    return {"message": "User created"}
