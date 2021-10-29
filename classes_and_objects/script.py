class Person:
    name = ""

    def get_name(self):
        return "Name: %s" % self.name


person = Person()

person.name = "John"

print(person.get_name())

class Car:
    make = ""
    color = ""

    def get_description(self):
        return "(Make = %s, Color = %s)" % (self.make, self.color)

car1 = Car()
car1.make = "Renault"
car1.color = "Gray"

car2 = Car()
car2.make = "Mercedes"
car2.color = "Black"

print(car1.get_description())
print(car2.get_description())
