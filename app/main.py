from fastapi import FastAPI
from app.routers import users, products

app = FastAPI(
    title='Mini E-commerce API',
    description='Month 1 CRUD project in-memory storage',
    version = '1.0.0'
)

app.include_router(users.router)
app.include_router(products.router)

@app.get('/')
def root():
    return {'message': ": 'API is running. Visit /docs for Swagger UI'"}