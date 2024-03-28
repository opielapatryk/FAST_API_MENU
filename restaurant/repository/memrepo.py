from restaurant.domain.dish import Dish


class MemRepo:
   def __init__(self, data):
      self.data = data
   
   def list(self):
      return [Dish.from_dict(d) for d in self.data]
    
   def get(self, id):
      dishes = self.list()
      try:
         dish = dishes[int(id) - 1]
         return dish
      except (IndexError, ValueError):
         return None
