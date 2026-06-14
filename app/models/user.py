from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    name: str 
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str 

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None