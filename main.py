from restaurant.repository.memrepo import MemRepo
from restaurant.use_cases.dish_list import dish_list_use_case
from fastapi import FastAPI

app = FastAPI()

dishes = [
    {
    "name": "pizza",
    "description": "italy",
    "price": 10.99
    },
    {
    "name": "burger",
    "description": "american",
    "price": 7.99
    },
    {
    "name": "spaghetti",
    "description": "italy",
    "price": 5.99
    },
    {
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

