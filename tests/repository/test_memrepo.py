from restaurant.domain.dish import Dish
from restaurant.repository.memrepo import MemRepo
import pytest

@pytest.fixture
def dish_dicts():
    return [
    {
        "id" : 1,
        "name": "pizza",
        "description": "italish",
        "price": 2.99
    },
    {
        "id" : 2,
        "name": "hot-dog",
        "description": "americano",
        "price": 5.99
    },
    {
        "id" : 3,
        "name": "burger",
        "description": "amerciano",
        "price": 9.99
    },
    {
        "id" : 4,
        "name": "spaghetti",
        "description": "italish",
        "price": 7.29
    },
]
@pytest.fixture
def dish_dicts_put():
    return [
    {
        "id" : 1,
        "name": "pizza",
        "description": "italish",
        "price": 2.99
    },
    {
        "id" : 2,
        "name": "hot-dog",
        "description": "americano",
        "price": 5.99
    },
    {
        "id" : 3,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    },
    {
        "id" : 4,
        "name": "spaghetti",
        "description": "italish",
        "price": 7.29
    },
]

@pytest.fixture
def dish_dicts_post():
    return [
    {
        "id" : 1,
        "name": "pizza",
        "description": "italish",
        "price": 2.99
    },
    {
        "id" : 2,
        "name": "hot-dog",
        "description": "americano",
        "price": 5.99
    },
    {
        "id" : 3,
        "name": "burger",
        "description": "amerciano",
        "price": 9.99
    },
    {
        "id" : 4,
        "name": "spaghetti",
        "description": "italish",
        "price": 7.29
    },
    {
        "id" : 5,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    }
]

def test_repository_list(dish_dicts):
    repo = MemRepo(dish_dicts)
    dishes = [Dish.from_dict(d) for d in dish_dicts]
    assert repo.list() == dishes

def test_repository_get(dish_dicts):
    repo = MemRepo(dish_dicts)
    dishes = [Dish.from_dict(d) for d in dish_dicts]
    assert repo.get(1) == dishes[0]

def test_repository_post(dish_dicts,dish_dicts_post):
    repo = MemRepo(dish_dicts)

    dish = {
        "id" : 5,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    }

    result = [Dish.from_dict(dish) for dish in dish_dicts_post]
    assert repo.post(dish) == result


def test_repository_put(dish_dicts,dish_dicts_put):
    repo = MemRepo(dish_dicts)

    updated_dish = {
        "id": 3,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    }

    result = [Dish.from_dict(dish) for dish in dish_dicts_put]

    assert repo.put(updated_dish) == result