class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Health: {}".format(self.health)
		return self



class Dog(Animal):
	def __init__(self):
		super(Dog, self).__init__("dog", 150)

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self):
		super(Dragon, self).__init__("dragon", 170)

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		super(Dragon, self).displayHealth()
		print "I am a Dragon"
		return self


animal1 = Animal("Generic Animal", 100).walk().walk().walk().run().run().displayHealth()

dog1 = Dog().walk().walk().walk().run().run().pet().displayHealth()  #.fly() Doesn't work!

dragon1 = Dragon().fly().displayHealth()