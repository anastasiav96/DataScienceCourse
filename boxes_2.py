import random


class Box:
    def __init__(self, name, h, w, l, m):
        self.name = name
        self.h = h
        self.w = w
        self.l = l
        self.m = m
        self.v = self.h * self.w * self.l

    @classmethod
    def create(cls, name):
        return cls(name, random.uniform(2, 8), random.uniform(2, 8), random.uniform(2, 8), random.uniform(2, 8))


class Carriage:
    def __init__(self, name, h, w, l, mass_available):
        self._name = name
        self._h = h
        self._w = w
        self._l = l
        self.mass_available = mass_available
        self.value_available = self._h * self._w * self._l
        self.mass_overall = 0
        self.value_overall = 0
        self.cargo_list = []
        self.cargo_not_in_carriage = []

    @classmethod
    def create(cls, name):
        return cls(name, random.uniform(10, 50), random.uniform(10, 50), random.uniform(10, 50), random.uniform(20, 50))

    def add(self, cargo):
        if self.check(cargo):
            self.cargo_list.append(cargo.name)
            self.mass_available -= cargo.m
            self.value_available -= cargo.v
            self.mass_overall += cargo.m
            self.value_overall += cargo.v
        else:
            self.cargo_not_in_carriage.append(cargo.name)

    def check(self, cargo):
        return (cargo.h <= self._h) and (cargo.w <= self._w) and (cargo.l <= self._l) and (
                self.mass_overall + cargo.m <= self.mass_available) and (
                       self.value_overall + cargo.v <= self.value_available)

    def __str__(self):
        return f'Carriage: {self._name}\nBox in carriage: {self.cargo_list}\nCargo not in carriage: {self.cargo_not_in_carriage}'


if __name__ == '__main__':
    random.seed(0)

    boxes = [Box.create(f'Box_{i}') for i in range(1, 11)]
    carriage = Carriage.create('Box_1')

    for box in boxes:
        carriage.add(box)

    print(carriage)
    print(carriage.__dict__)
