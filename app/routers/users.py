from app.models import user
from fastapi import APIRouter, HTTPException
import app.database as database
from app.utils import id_gen

router = APIRouter()

@router.post('/users', status_code=201, response_model= user.UserResponse)
def register_user(data: user.UserCreate,):
    user_id = id_gen.generate_id()
    database.users_db[user_id] = {**data.model_dump(), 'id': user_id}
    return database.users_db[user_id]

@router.get('/users', status_code=200, response_model=list[user.UserResponse])
def show_users():
    return [user for user in database.users_db.values()]

@router.get('/users/{user_id}', status_code=200, response_model=user.UserResponse)
def show_user(user_id: str):
    if user_id not in database.users_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return database.users_db[user_id]

@router.delete('/users/{user_id}', status_code=200,)
def delete_user(user_id: str):
    if user_id not in database.users_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del database.users_db[user_id]
    return {"message": "User deleted successfully"}

@router.put('/users/{user_id}', status_code=200,response_model= user.UserResponse)
def update_user(user_id: str, data: user.UserUpdate):
    if user_id not in database.users_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data = data.model_dump(exclude_unset=True)
    database.users_db[user_id].update(update_data)

    return database.users_db[user_id]