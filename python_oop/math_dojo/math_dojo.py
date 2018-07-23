class MathDojo(object):
	def __init__(self):
		self.sum = 0

	def add(self, *nums):
		for x in nums:
			if type(x) == int:
				self.sum += x
			else: 
				self.sum += sum(x)
		return self

	def subtract(self, *nums):
		for x in nums:
			if type(x) == int:
				self.sum -= x
			else: 
				self.sum -= sum(x)
		return self

	def result(self):
		return self.sum

y = md.add(2).add(2,5,1).subtract(3,2).result
print(y)      

