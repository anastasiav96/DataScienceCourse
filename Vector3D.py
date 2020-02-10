import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __mul__(self, other):
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __abs__(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def __bool__(self):
        return self.__abs__() > 0.0

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


if __name__ == '__main__':
    a = Vector3D(0, 0, 0)
    b = Vector3D(1, 2, 3)
    print(a + b)
    a += b
    print(a * 5)
    b += a
    print(b)
    print(b * 2)
    print(abs(b))
    print(bool(b))
    print(bool(a))
