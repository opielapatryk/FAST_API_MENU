from restaurant.repository.memrepo import MemRepo
from restaurant.repository.postgrerepo import PostgresRepo
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.use_cases.dish_get import dish_get_use_case
from restaurant.use_cases.dish_post import dish_post_use_case
from restaurant.use_cases.dish_put import dish_put_use_case
from restaurant.use_cases.dish_patch import dish_patch_use_case
from restaurant.use_cases.dish_delete import dish_delete_use_case
from fastapi import FastAPI
from fastapi import HTTPException
from restaurant.repository.mongorepo import MongoRepo
import os

app = FastAPI()

dishes = [
    {
    "id" : 1,
    "name": "pizza",
    "description": "italy",
    "price": 10.99
    },
    {
    "id" : 2,
    "name": "burger",
    "description": "american",
    "price": 7.99
    },
    {
    "id" : 3,
    "name": "spaghetti",
    "description": "italy",
    "price": 5.99
    },
    {
    "id" : 4,
    "name": "fries",
    "description": "american",
    "price": 1.99
    },
]

mongo_configuration = {
    "MONGODB_HOSTNAME": 'db',
    "MONGODB_PORT": 27017,
    "MONGODB_USER": 'root',
    "MONGODB_PASSWORD": 'mongodb',
    "APPLICATION_DB": 'restaurant',
}

postgres_configuration = {
    "POSTGRES_USER": 'postgres',
    "POSTGRES_PASSWORD": 'postgres',
    "POSTGRES_HOSTNAME": 'db',
    "POSTGRES_PORT": 5432,
    "APPLICATION_DB": 'postgres',
}

@app.get("/")
def welcome():
    return {"message": "Welcome to the Restaurant API!", "endpoints": {"dishes": "api/v1/dishes"}}

@app.get("/api/v1/dishes")
def dish_list(min_price:float=0,max_price:float=float('inf'),description:str=None,sort_by: str = 'id', sort_order: str = 'asc', page:int = 1, per_page:int = 10):
    repo = MongoRepo(mongo_configuration)
    result = dish_list_use_case(repo)

    # # Apply filters
    filtered_dishes = filter(lambda p: p['price'] >= min_price and p['price'] <= max_price, result)

    if description:
        filtered_dishes = filter(lambda p: p['description'] == description, filtered_dishes)

    # # Sorting 
    sorted_dishes = sorted(filtered_dishes, key=lambda p: p[sort_by], reverse=sort_order.lower() == 'desc')

    # Paginate the results
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_dishes = sorted_dishes[start_index:end_index]
    
    return paginated_dishes

@app.get("/api/v1/dishes/{id}")
def dish_get(id: int):
    repo = MongoRepo(mongo_configuration)
    result = dish_get_use_case(repo, id)

    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Dish not found")

@app.post("/api/v1/dishes", status_code=201)
def create_dish(dish: dict):
    repo = MongoRepo(mongo_configuration)

    id = dish.get('id')
    name = dish.get('name')
    description = dish.get('description')
    price = dish.get('price')

    if not name or not description or not price or not id:
        raise HTTPException(status_code=400, detail="Missing required fields")

    try:
      result = dish_post_use_case(repo, dish)
    except:
      raise HTTPException(status_code=400, detail="Dish already exists")
    

    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Failed to create dish")

@app.put("/api/v1/dishes", status_code=201)
def update_dish(dish: dict):
    repo = MongoRepo(mongo_configuration)
    result = dish_put_use_case(repo, dish)

    if result:
        return result
    else:
        raise HTTPException(status_code=500, detail="Failed to update dish")

@app.patch("/api/v1/dishes/{id}", status_code=201)
def partial_update_dish(dish: dict, id: int):
    repo = MongoRepo(mongo_configuration)
    result = dish_patch_use_case(repo, dish, id)

    if result:
        return result
    else:
        raise HTTPException(status_code=500, detail="Failed to update dish")
    
@app.delete("/api/v1/dishes/{id}", status_code=201)
def dish_delete(id: int):
    repo = MongoRepo(mongo_configuration)
    result = dish_delete_use_case(repo, id)

    if result:
        return result
    else:
        raise HTTPException(status_code=500, detail="Failed to remove dish")
    