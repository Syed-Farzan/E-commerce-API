from fastapi import APIRouter, HTTPException
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

@router.get('/products/{product_id}', response_model=product.ProductResponse, status_code=200)
def get_product(product_id: str):
        if product_id not in database.products_db:
             raise HTTPException(status_code=404, detail='the product not found')
        return database.products_db[product_id]
        
@router.put('/products/{product_id}',response_model=product.ProductResponse)
def update_product(product_id: str, data: product.ProductUpdate):
     if product_id not in database.products_db:
             raise HTTPException(status_code=404, detail='the product not found')
     update_data = data.model_dump(exclude_unset=True)
     database.products_db[product_id].update(update_data)
     return database.products_db[product_id]

@router.delete('/products/{product_id}')
def delete_product(product_id: str):
    if product_id not in database.products_db:
        raise HTTPException(status_code=204, detail='Product not found')
    del database.products_db[product_id]
    return {'message': 'item was deleted'}

@router.post('/products/{product_id}/purchase',response_model=product.ProductResponse)
def buy_product(product_id: str):
    if product_id not in database.products_db :
        raise HTTPException(status_code=404, detail='Product not found')
    if database.products_db[product_id]['stock'] <1:
        raise HTTPException(status_code=400, detail='Product not availiable')
    else:
        database.products_db[product_id]['stock'] -= 1
    return database.products_db[product_id]