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

def test_repository_list():
    repo = MemRepo(dish_dicts)
    dishes = [Dish.from_dict(d) for d in dish_dicts]
    assert repo.list() == dishes

def test_repository_get():
    repo = MemRepo(dish_dicts)
    dishes = [Dish.from_dict(d) for d in dish_dicts]
    assert repo.get(1) == dishes[0]
