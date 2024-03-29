from restaurant.domain.dish import Dish


class MemRepo:
   def __init__(self, data):
      self.data = data
   
   def list(self):
      return [Dish.from_dict(d) for d in self.data]
    
   def get(self, id):
      try:
         dish = [dish for dish in self.data if dish['id'] == id]
         return dish
      except (IndexError, ValueError):
         return None
