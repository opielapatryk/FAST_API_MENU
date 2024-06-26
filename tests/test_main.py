from unittest import mock
from fastapi.testclient import TestClient
from main import app
from restaurant.domain.dish import Dish

dish_dict = {
    "id" : 1,
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

@mock.patch('main.dish_post_use_case')
def test_post(mock_use_case):
    new_dish_data = {
        "id" : 2,
        "name": "pomidorowa",
        "description": "Soup",
        "price": 3.99
    }

    mock_use_case.return_value = [dish_dict] + [new_dish_data] 

    client = TestClient(app)
    response = client.post('/dishes', json=new_dish_data)

    response_data = response.json()
    dish = [dish_dict] + [new_dish_data] 

    assert response_data == dish
    mock_use_case.assert_called()
    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"
    
@mock.patch('main.dish_put_use_case')
def test_put(mock_use_case):
    updated_dish_data = {
        "id" : 1,
        "name": "pomidorowa",
        "description": "Soup",
        "price": 3.99
    }

    mock_use_case.return_value = updated_dish_data

    client = TestClient(app)
    response = client.put('/dishes', json=updated_dish_data)

    response_data = response.json()

    assert response_data == updated_dish_data
    mock_use_case.assert_called()
    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"
    
@mock.patch("main.dish_delete_use_case")
def test_delete(mock_use_case):
    client = TestClient(app)
    response = client.delete('/dishes/1')

    mock_use_case.assert_called()
    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"
    