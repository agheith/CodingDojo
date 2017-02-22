class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        
        if self.price > 10000:
            self.tax = .15

    def displayInfo(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed)
        print 'fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage)
        print 'tax: ' + str(self.tax)


car1 = Car(10000, "50mph", "full", "20mpg")
car1.displayInfo()

car2 = Car(150000, "70mph", "full", "50mpg")
car2.displayInfo()

car3 = Car(1200000, "90mph", "full", "40mpg")
car3.displayInfo()

car4 = Car(2000000, "75mph", "full", "30mpg")
car4.displayInfo()

car5 = Car(1400000, "70mph", "full", "25mpg")
car5.displayInfo()

car6 = Car(10000000, "80mph", "full", "65mpg")
car6.displayInfo()
