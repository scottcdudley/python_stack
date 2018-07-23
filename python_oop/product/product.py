class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

		self.display_info()

	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self, tax):
		return self.price * (1 + tax)

	def return_product(self, reason):
		if reason.lower() == "defective":
			self.price = 0
			self.status = "Defective"
		elif reason.lower() == "like new":
			self.status = "for sale"
		elif reason.lower() == "open":
			self.status = "used"
			self.price *= 0.8

		return self

	def display_info(self):
		print "Item Name: {}".format(self.item_name)
		print "Price: {}".format(self.price)
		print "Weight: {}".format(self.weight)
		print "Brand: {}".format(self.brand)
		print "Status: {}".format(self.status)

		return self


product1 = Product(200, 'Zune', '10oz', 'Microsoft')
print " "
print product1.add_tax(0.1)
print " "
product1.sell()
product1.display_info()
print " "
product1.return_product("defective")
product1.display_info()
print " "

product2 = Product(1000, "iPod", "1lb", "Apple")
print " "
print product2.add_tax(0.7)
print " "
product2.sell()
product2.display_info()
print " "
product2.return_product("open")
product2.display_info()
print " "