from restaurant.repository.memrepo import MemRepo
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.use_cases.dish_get import dish_get_use_case
from restaurant.use_cases.dish_post import dish_post_use_case
from restaurant.use_cases.dish_put import dish_put_use_case
from fastapi import FastAPI
from fastapi import HTTPException

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


@app.get("/")
def welcome():
    return {"message": "Welcome to the Restaurant API!", "endpoints": {"dishes": "/dishes"}}

@app.get("/dishes")
def dish_list():
    repo = MemRepo(dishes)
    result = dish_list_use_case(repo)
    return result

@app.get("/dishes/{id}")
def dish_get(id: int):
    repo = MemRepo(dishes)
    result = dish_get_use_case(repo, id)
    return result

@app.post("/dishes", status_code=201)
def create_dish(dish: dict):
    repo = MemRepo(dishes)
    result = dish_post_use_case(repo, dish)

    if result:
        return result
    else:
        raise HTTPException(status_code=500, detail="Failed to create dish")

@app.put("/dishes", status_code=201)
def update_dish(dish: dict):
    repo = MemRepo(dishes)
    result = dish_put_use_case(repo, dish)

    if result:
        return result
    else:
        raise HTTPException(status_code=500, detail="Failed to update dish")
