from fastapi import APIRouter
from models import product 
import database
import uuid
from typing import Optional

router = APIRouter()

@router.post('/products', response_model=product.ProductResponse, status_code=201)
def create_product(data: product.ProductCreate):
    id = str(uuid.uuid4())
    database.products_db[id] = {**data.model_dump(), 'id': id}
    return database.products_db[id]

@router.get('/products', response_model=list[product.ProductResponse], status_code=200)
def showproducts(category: Optional[str] = None):
    full_category = []
    if category:
        for item in database.products_db.values():
            if category == item['category']:
                full_category.append(item)
        return full_category
    else:
        return list(database.products_db.values())