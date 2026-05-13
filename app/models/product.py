from pydantic import BaseModel, Field
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    price: float = Field(gt=0)
    category: str
    stock: int = Field(ge=0)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)

class ProductResponse(BaseModel):
    id: str
    name: str 
    price: float 
    category: str
    stock: int 