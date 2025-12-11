# @property


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height


rect = Rectangle(5, 3)
print(rect.area)
