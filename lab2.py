import turtle
from random import randint, choice

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)   # абсолютна позиція першої вершини
        self.vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.vertex2 = (x2, y2)  # позиція третьої відносно першої вершини
        self.color = "black"     # колір трикутника за промовчанням

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()

        vertices = [self.position,
                    (self.position[0] + self.vertex1[0], self.position[1] + self.vertex1[1]),
                    (self.position[0] + self.vertex2[0], self.position[1] + self.vertex2[1])]

        for vertex in vertices:
            turtle.goto(vertex)
        turtle.goto(self.position)
        turtle.end_fill()

def draw_random_triangles(n):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]
    for _ in range(n):
        x1, y1 = randint(-50, 50), randint(-50, 50)
        x2, y2 = randint(-50, 50), randint(-50, 50)
        triangle = Triangle(x1, y1, x2, y2)
        triangle.set_position(randint(-200, 200), randint(-200, 200))
        triangle.set_color(choice(colors))
        triangle.draw()

if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    draw_random_triangles(100)
    turtle.done()
import math

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self.color = "black"
        self.rotation = 0
        self.scale = (1, 1)

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()

        vertices = [self.position,
                    self._transform(self.vertex1),
                    self._transform(self.vertex2)]

        for vertex in vertices:
            turtle.goto(vertex)
        turtle.goto(self.position)
        turtle.end_fill()

    def _transform(self, vertex):
        x, y = vertex
        x, y = x * self.scale[0], y * self.scale[1]
        rad = self.rotation
        x_new = x * math.cos(rad) - y * math.sin(rad)
        y_new = x * math.sin(rad) + y * math.cos(rad)
        return self.position[0] + x_new, self.position[1] + y_new

def animate_rotation(triangle, steps=360):
    for i in range(steps):
        triangle.set_rotation(math.radians(i))
        turtle.clear()
        triangle.draw()
        turtle.update()

def animate_scale(triangle, steps=100):
    for i in range(steps):
        scale_factor = 1 + i * 0.01
        triangle.set_scale(scale_factor, scale_factor)
        turtle.clear()
        triangle.draw()
        turtle.update()

if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0)

    triangle = Triangle(50, 0, 25, 43)
    triangle.set_position(0, 0)
    triangle.set_color("blue")

    animate_rotation(triangle)
    animate_scale(triangle)
    turtle.done()
class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self.color = "black"
        self.rotation = 0
        self.scale = (1, 1)
        self.pivot = self.position

    def set_position(self, x, y):
        self.position = (x, y)
        self.pivot = self.position  # Оновлюємо точку повороту

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def set_pivot(self, pivot_x, pivot_y):
        self.pivot = (pivot_x, pivot_y)

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()

        vertices = [self.position,
                    self._transform(self.vertex1),
                    self._transform(self.vertex2)]

        for vertex in vertices:
            turtle.goto(vertex)
        turtle.goto(self.position)
        turtle.end_fill()

    def _transform(self, vertex):
        x, y = vertex
        x, y = x * self.scale[0], y * self.scale[1]
        rad = self.rotation
        px, py = self.pivot
        x, y = x + px - self.position[0], y + py - self.position[1]
        x_new = (x - px) * math.cos(rad) - (y - py) * math.sin(rad) + px
        y_new = (x - px) * math.sin(rad) + (y - py) * math.cos(rad) + py
        return x_new, y_new

def animate_rotation_pivot(triangle, steps=360):
    for i in range(steps):
        triangle.set_rotation(math.radians(i))
        turtle.clear()
        triangle.draw()
        turtle.update()

def animate_scale_pivot(triangle, steps=100):
    for i in range(steps):
        scale_factor = 1 + i * 0.01
        triangle.set_scale(scale_factor, scale_factor)
        turtle.clear()
        triangle.draw()
        turtle.update()

if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0)

    triangle = Triangle(50, 0, 25, 43)
    triangle.set_position(0, 0)
    triangle.set_color("blue")
    triangle.set_pivot(25, 21)  # Задаємо точку повороту

    animate_rotation_pivot(triangle)
    animate_scale_pivot(triangle)
    turtle.done()
