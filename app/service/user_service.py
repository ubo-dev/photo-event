
from fastapi import HTTPException
from pytest import Session

from app.models.user import User
from app.repository.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.security import hash_password

class UserService:
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        
    def create_user(self, user: UserCreate):
        existing_user = self.repository.get_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="This email already registered!")
        
        user = User(
            email = user.email,
            hashed_password = hash_password(user.password)
        )
        
        return self.repository.create(user)