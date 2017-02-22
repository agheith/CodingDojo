class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print 'Price is $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed)
        print 'Total miles: ' + str(self.miles)
        return self

    def ride(self):
        self.miles += 10
        print "Riding"
        return self

    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        print "Reversing"
        return self

# create instances and run methods
bike1 = Bike(200, "30mph")
bike1.ride().reverse().displayInfo()

bike2 = Bike(400, "40mph")
bike1.ride().reverse().displayInfo()

bike3 = Bike(600, "60mph")
bike1.ride().reverse().displayInfo()
