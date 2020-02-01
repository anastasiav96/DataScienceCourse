import random


class Cargo:
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

    def __str__(self):
        return f'Cargo: {self.name}\nAttributes: {self.__dict__}'


class Box(Cargo):
    def __init__(self, name, h, w, l, m):
        super().__init__(name, h, w, l, m)


class Fridge(Cargo):
    def __init__(self, name, h, w, l, m):
        super().__init__(name, h, w, l, m)


class Table(Cargo):
    def __init__(self, name, h, w, l, m):
        super().__init__(name, h, w, l, m)


class Carriage:
    def __init__(self, name, h, w, l, mass_available, open, ready):
        self._name = name
        self._h = h
        self._w = w
        self._l = l
        self.mass_available = mass_available
        self.value_available = self._h * self._w * self._l
        self.mass_overall = 0
        self.value_overall = 0
        self.cargo_list = []
        self.cargo_list_object = []
        self.cargo_not_in_carriage = []
        self.open = True
        self.ready = True
        self.x = 0
        self.y = 0

    @classmethod
    def create(cls, name, open, ready):
        return cls(name, random.uniform(10, 50), random.uniform(10, 50), random.uniform(10, 50), random.uniform(20, 50),
                   open, ready)

    def check_params(self, cargo):
        return (cargo.h <= self._h) and (cargo.w <= self._w) and (cargo.l <= self._l) and (
                self.mass_overall + cargo.m <= self.mass_available) and (
                       self.value_overall + cargo.v <= self.value_available)

    def check_ready(self):
        return self.open is True and self.ready is True

    def add(self, cargo):
        if self.check_params(cargo) and self.check_ready():
            self.cargo_list.append(cargo.name)
            self.cargo_list_object.append(cargo)
            self.mass_available -= cargo.m
            self.value_available -= cargo.v
            self.mass_overall += cargo.m
            self.value_overall += cargo.v
        else:
            self.cargo_not_in_carriage.append(cargo.name)

    def drop(self):
        if self.check_ready():
            cargo_name = self.cargo_list.pop()
            cargo = self.cargo_list_object.pop()
            self.mass_available += cargo.m
            self.value_available += cargo.v
            self.mass_overall -= cargo.m
            self.value_overall -= cargo.v
            return cargo_name

    def movement(self, x, y):
        if self.check_ready():
            self.x += x
            self.y += y
        return self.x, self.y

    def __str__(self):
        return f'Carriage: {self._name}\nCargo in carriage: {self.cargo_list}\nCargo not in carriage: ' \
               f'{self.cargo_not_in_carriage}\nAttributes: {self.__dict__}'


if __name__ == '__main__':
  pass
