class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    
    def displayInfo(self):
        print('Price: {}' .format(self.price))
        print 'Max Speed: {}'.format(self.max_speed)
        print "Miles: {}" .format(self.miles)
        return self


    def ride(self):
        print('Riding')
        self.miles += 10
        return self
    
    def reverse(self):
        print('Reverse')
        if self.miles < 0:
            self.miles = 0
        else:
            self.miles -= 5
        return self

bike1.ride().ride().ride().reverse().displayInfo()
print " "
bike2.ride().ride().reverse().reverse().displayInfo()
print " "
bike3.reverse().reverse().displayInfo()
print " "
