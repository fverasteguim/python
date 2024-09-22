import math
from employee import Employee
from week import WeekDay
import serializer_delegation
import shapes_abc

class Circle:
    num_instances = 0

    def __init__(self, radius):
        type(self).num_instances += 1
        self.radius = radius

    def calculate_area(self):
        return math.pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

def main():
    circle_1 = Circle(42)
    circle_2 = Circle(5)
    circle_3 = Circle(2)

    print(circle_1.radius)
    print(circle_1.calculate_area())

    print(circle_2.radius)
    print(circle_2.calculate_area())

    circle_1.radius = 2
    print(circle_1.radius)
    print(circle_1.calculate_area())

    print(Circle.num_instances)

    vw_vocho = Car("Volkswagen", "Escarabajo", 1982, "Celeste")
    
    print(vw_vocho.model)
    print(vw_vocho.max_speed)

    print(Circle.__dict__)
    print(Circle.__dict__["num_instances"])
    circle_1.__dict__["radius"] = -2
    circle_1.__dict__["factor"] = 2
    print(circle_1.factor)
    print(circle_1.radius)

    Car.voltear = voltear

    print(Car.__dict__)

    john = Employee("John Doe", "1980-12-04")
    print(f"Company: {john.company}")
    print(f"Name: {john.name}")
    print(f"Age: {john.compute_age()}")
    print(john)

    jane_data = {"name": "Jane Doe", "birth_date": "2001-05-15"}
    jane = Employee.from_dict(jane_data)
    print(jane)

    print(WeekDay.favorite_day())
    print(list(WeekDay))

    empl = serializer_delegation.Employee("Francisco", "44", 1234)
    print(empl.to_json())

    circ = shapes_abc.Circle(3)
    print(f"Area: {circ.get_area()}")
    print(f"Perimeter: {circ.get_perimeter()}")

def voltear():
    pass

if __name__ == "__main__":
    main()
