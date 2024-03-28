from unittest import mock
from fastapi.testclient import TestClient
from main import app
from restaurant.domain.dish import Dish

dish_dict = {
    "name": "pizza",
    "description": "italy",
    "price": 10.99
}

dishes = [Dish.from_dict(dish_dict)]

@mock.patch('main.dish_list_use_case')
def test_list(mock_use_case):
    mock_use_case.return_value = dishes

    client = TestClient(app)
    response = client.get('/dishes')

    response_data = response.json()
    assert response_data == [dish_dict]
    mock_use_case.assert_called()
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

@mock.patch('main.dish_get_use_case')
def test_get(mock_use_case):
    mock_use_case.return_value = dishes[0]

    client = TestClient(app)
    response = client.get('/dishes/0')

    response_data = response.json()
    assert response_data == dish_dict
    mock_use_case.assert_called()
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

