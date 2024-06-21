from abc import ABC, abstractmethod
import math

# Базовий клас Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Інтерфейс IDrawable
class IDrawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Клас Circle
class Circle(Shape, IDrawable):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def draw(self):
        print("Drawing a circle")

# Клас Square
class Square(Shape, IDrawable):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def draw(self):
        print("Drawing a square")

# Клас Triangle
class Triangle(Shape, IDrawable):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print("Drawing a triangle")

# Використання поліморфізму для обчислення площі та виклику методу draw()
shapes = [Circle(5), Square(4), Triangle(6, 3)]

for shape in shapes:
    print(f"Area: {shape.calculate_area()}")
    shape.draw()
