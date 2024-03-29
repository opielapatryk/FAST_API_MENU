import pytest
from restaurant.domain.dish import Dish
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.use_cases.dish_get import dish_get_use_case
from restaurant.use_cases.dish_post import dish_post_use_case
from restaurant.use_cases.dish_put import dish_put_use_case
from restaurant.use_cases.dish_delete import dish_delete_use_case
from unittest import mock

@pytest.fixture
def domain_dishes():
    dish_1 = Dish(
        id=1,
        name='pizza',
        description='italiano sepcailze',
        price=9.99
    )
    dish_2 = Dish(
        id=2,
        name='spagetti',
        description='italiano pasta',
        price=14.99
    )
    dish_3 = Dish(
        id=3,
        name='nalesniki',
        description='Something sweet',
        price=7.99,
    )
    dish_4 = Dish(
        id=4,
        name='chips',
        description='fried potatooo',
        price=3.29
    )

    return [dish_1, dish_2, dish_3, dish_4]

@pytest.fixture
def domain_dishes_put():
    dish_1 = Dish(
        id=1,
        name='pizza',
        description='italiano sepcailze',
        price=9.99
    )
    dish_2 = Dish(
        id=2,
        name='spagetti',
        description='italiano pasta',
        price=14.99
    )
    dish_3 = Dish(
        id=3,
        name='nic dobrego',
        description='Meh',
        price=0.01,
    )
    dish_4 = Dish(
        id=4,
        name='chips',
        description='fried potatooo',
        price=3.29
    )

    return [dish_1, dish_2, dish_3, dish_4]

@pytest.fixture
def domain_dishes_post():
    dish_1 = Dish(
        id=1,
        name='pizza',
        description='italiano sepcailze',
        price=9.99
    )
    dish_2 = Dish(
        id=2,
        name='spagetti',
        description='italiano pasta',
        price=14.99
    )
    dish_3 = Dish(
        id=3,
        name='nalesniki',
        description='Something sweet',
        price=7.99,
    )
    dish_4 = Dish(
        id=4,
        name='chips',
        description='fried potatooo',
        price=3.29
    )
    dish_5 = Dish(
        id=5,
        name='pomidorowa',
        description='Soup',
        price=3.99
    )

    return [dish_1, dish_2, dish_3, dish_4, dish_5]



def test_list_dishes(domain_dishes):
    repo = mock.Mock()
    repo.list.return_value = domain_dishes

    result = dish_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_dishes

def test_get_dish(domain_dishes):
    repo = mock.Mock()
    repo.get.return_value = domain_dishes[0]

    result = dish_get_use_case(repo, 0)

    repo.get.assert_called_with(0)
    assert result == domain_dishes[0]

def test_dish_post(domain_dishes_post):
    repo = mock.Mock()
    repo.post.return_value = domain_dishes_post

    dish = Dish(
        id=1,
        name='pomidorowa',
        description='Soup',
        price=3.99
    )

    result = dish_post_use_case(repo, dish)
    
    repo.post.assert_called_with(dish)
    assert result == domain_dishes_post

def test_dish_put(domain_dishes_put):
    repo = mock.Mock()
    repo.put.return_value = domain_dishes_put

    updated_dish = Dish(
        id=1,
        name='nic dobrego',
        description='Meh',
        price=0.01,
    )

    result = dish_put_use_case(repo, updated_dish)
    
    repo.put.assert_called_with(updated_dish)
    assert result == domain_dishes_put

def test_dish_delete_use_case(domain_dishes):
    repo = mock.Mock()
    repo.delete.return_value = [dish for dish in domain_dishes if dish.id != 3] 
    
    result = dish_delete_use_case(repo, 3)

    repo.delete.assert_called_with(3)
    assert result == [dish for dish in domain_dishes if dish.id != 3]