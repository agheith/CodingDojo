class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'Price is $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed)
        print 'Total miles: ' + str(self.miles)

    def ride(self):
        self.miles += 10
        print "Riding"

    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        print "Reversing"

# create instances and run methods
bike1 = Bike(200, "30mph")
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(400, "40mph")
bike2.ride()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(600, "60mph")
bike3.ride()
bike3.reverse()
bike3.displayInfo()
