class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        print str(self.name), "is walking"
        return self


    def run(self):
        self.health -= 5
        print str(self.name), "is running"
        return self

    def displayHealth(self):
        print "health is", str(self.health)
        return self

dog = Animal('dog', 'self.health')
dog.run().run().run().walk().walk().displayHealth()


class Dog(Animal):
    def pet(self):
        self.health += 5
        print str(self.name), "is petting"
        return self

doggy = Dog('doggy',150)
doggy.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal): #170 health
    def fly(self):
        self.health -= 10
        print str(self.name), "is flying"
        return self
    def displayHealth(self):
        print "This is Dragon", str(self.health)
        return self

drag = Dragon('drag',170)
drag.walk().walk().walk().run().run().fly().fly().displayHealth()
