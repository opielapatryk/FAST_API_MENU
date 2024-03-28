from restaurant.domain.dish import Dish


class MemRepo:
    def __init__(self, data):
      self.data = data
    
    def list(self):
       return [Dish.from_dict(d) for d in self.data]
    