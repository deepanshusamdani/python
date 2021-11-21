#@property: Syntax and Logic

#instance attribute is public because its name doesn't have a leading underscore.
class House:

	def __init__(self, price):
		self.price = price

# Access value
obj.price

# Modify value
obj.price = 40000

#-----------------------------------------------------------------------------------------------------------------------------
# Changed from obj.price
obj.get_price()

# Changed from obj.price = 40000
obj.set_price(40000)

# protected variable by using "_" before price.
class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price
    
    
#define three methods for a property:
  #A getter - to access the value of the attribute.
  #A setter - to set the value of the attribute.
  #A deleter - to delete the instance attribute.
