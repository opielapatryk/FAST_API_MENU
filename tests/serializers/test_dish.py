import json
from restaurant.domain.dish import Dish
from restaurant.serializers.dish import DishJsonEncoder

def test_serializer_domain_dish():
    dish = Dish('pizza','italian dish',2.99)

    expected_json = """
        {
        "name": "pizza",
        "description": "italian dish",
        "price": 2.99
        }
    """

    json_dish = json.dumps(dish, cls=DishJsonEncoder)

    assert json.loads(expected_json) == json.loads(json_dish)