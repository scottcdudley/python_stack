 

#In your __init__(), call this display_all() method to display information 
#about the car once the attributes have been defined.
    
    #create class
    class Car(object):
    #define attributes
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
        #If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()
    #In the class have a method called display_all() that returns all the information about the car as a string.
	def display_all(self):
		print "Price: {}".format(self.price)
		print "Speed: {}".format(self.speed)
		print "Fuel: {}".format(self.fuel)
		print "Mileage: {}".format(self.mileage)
		print "Tax: {}".format(self.tax)

		return self

#Create six different instances of the class Car. 
car1 = Car(12000, "90mph", "Full", "35mpg")
print " "
car2 = Car(2000, "75mph", "Quarter Full", "125mpg")
print " "
car3 = Car(5000, "115mph", "Half Full", "15mpg")
print " "
car4 = Car(20000, "205mph", "Full", "5mpg")
print " "
car5 = Car(20000, "125mph", "Empty", "25mpg")
print " "
car6 = Car(200, "5mph", "Full", "7mpg")