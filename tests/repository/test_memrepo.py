from restaurant.domain.dish import Dish
from restaurant.repository.memrepo import MemRepo

dish_dicts = [
    {
        "name": "pizza",
        "description": "italish",
        "price": 2.99
    },
    {
        "name": "hot-dog",
        "description": "americano",
        "price": 5.99
    },
    {
        "name": "burger",
        "description": "amerciano",
        "price": 9.99
    },
    {
        "name": "spaghetti",
        "description": "italish",
        "price": 7.29
    },
]

dish_dicts_post = [
    {
        "name": "pizza",
        "description": "italish",
        "price": 2.99
    },
    {
        "name": "hot-dog",
        "description": "americano",
        "price": 5.99
    },
    {
        "name": "burger",
        "description": "amerciano",
        "price": 9.99
    },
    {
        "name": "spaghetti",
        "description": "italish",
        "price": 7.29
    },
    {
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    }
]

def test_repository_list():
    repo = MemRepo(dish_dicts)
    dishes = [Dish.from_dict(d) for d in dish_dicts]
    assert repo.list() == dishes

def test_repository_get():
    repo = MemRepo(dish_dicts)
    dishes = [Dish.from_dict(d) for d in dish_dicts]
    assert repo.get(1) == dishes[0]

def test_repository_post():
    repo = MemRepo(dish_dicts)

    dish = {
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    }

    result = [Dish.from_dict(dish) for dish in dish_dicts_post]
    assert repo.post(dish) == result
