import pytest
from restaurant.domain.dish import Dish
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.use_cases.dish_get import dish_get_use_case
from unittest import mock

@pytest.fixture
def domain_dishes():
    dish_1 = Dish(
        name='pizza',
        description='italiano sepcailze',
        price=9.99
    )
    dish_2 = Dish(
        name='spagetti',
        description='italiano pasta',
        price=14.99
    )
    dish_3 = Dish(
        name='nalesniki',
        description='Something sweet',
        price=7.99,
    )
    dish_4 = Dish(
        name='chips',
        description='fried potatooo',
        price=3.29
    )

    return [dish_1, dish_2, dish_3, dish_4]



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

