import random


class Carriage:
    def __init__(self, h, w, l, mass_available, open, ready):
        self._h = h
        self._w = w
        self._l = l
        self._mass_available = mass_available
        self._volume_available = self._h * self._w * self._l
        self._mass_overall = 0
        self._volume_overall = 0
        self._cargo_list = []
        self._open = True
        self._ready = True
        self._x = 0
        self._y = 0

    @property
    def h(self):
        return self._h

    @property
    def w(self):
        return self._w

    @property
    def l(self):
        return self._l

    @property
    def mass_available(self):
        return self._mass_available

    @property
    def volume_available(self):
        return self._volume_available

    @property
    def mass_overall(self):
        return self._mass_overall

    @property
    def value_overall(self):
        return self._volume_overall

    @property
    def cargo_list(self):
        return self._cargo_list

    @property
    def open(self):
        return self._open

    @property
    def ready(self):
        return self._ready

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @classmethod
    def create(cls, open, ready):
        return cls(h=random.uniform(10, 50), w=random.uniform(10, 50), l=random.uniform(10, 50),
                   mass_available=random.uniform(20, 50), open=open, ready=ready)

    def check_params(self, cargo):
        return (cargo.h <= self._h) and (cargo.w <= self._w) and (cargo.l <= self._l) and (
                self._mass_overall + cargo.m <= self._mass_available) and (
                       self._volume_overall + cargo.v <= self._volume_available)

    def check_ready(self):
        return self._open is True and self._ready is True

    def add(self, cargo):
        if self.check_params(cargo) and self.check_ready():
            self._cargo_list.append(cargo)
            self._mass_available -= cargo.m
            self._volume_available -= cargo.v
            self._mass_overall += cargo.m
            self._volume_overall += cargo.v
            return True

    def drop(self):
        if self.check_ready():
            cargo = self._cargo_list.pop()
            self._mass_available += cargo.m
            self._volume_available += cargo.v
            self._mass_overall -= cargo.m
            self._volume_overall -= cargo.v
            return cargo

    def __str__(self):
        return f'height: {self._h}, width: {self._w}, length: {self._l}, mass_available: {self._mass_available},' \
               f' volume: {self._volume_available}, mass_overall: {self._mass_overall}, ' \
               f'volume_overall: {self._volume_overall}, cargo in carriage: {self._cargo_list}, door: {self._open}, ' \
               f'ready: {self._ready}, coordinates: {self._x, self._y}'


class Train:
    def __init__(self, number, x, y):
        self._number = number
        self._open = True
        self._ready = True
        self._x = x
        self._y = y
        self._carriage_list = []

    @property
    def number(self):
        return self._number

    @property
    def carriage_list(self):
        return self._carriage_list

    @property
    def open(self):
        return self._open

    @property
    def ready(self):
        return self._ready

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def add_carriage(self, carriage):
        self._carriage_list.append(carriage)

    def drop_carriage(self):
        self._carriage_list.pop()

    def movement(self, x, y, carriage):
        if carriage.check_ready():
            self._x += x
            self._y += y
        return self._x, self._y

    def __iter__(self):
        return TrainIterator(self)

    def __str__(self):
        return f'Number of train: {self._number}, carriages in train: {self._carriage_list}, door: {self._open}, ' \
               f'ready: {self._ready}, coordinates: {self._x, self._y}'


class TrainIterator:
    def __init__(self, train):
        self._train = train
        self._index = 0

    def __next__(self):
        if self._index < len(self._train._carriage_list):
            result = self._train._carriage_list[self._index]
            self._index += 1
            return result
        raise StopIteration


class Cargo:
    def __init__(self, h, w, l, m):
        self._h = h
        self._w = w
        self._l = l
        self._m = m
        self._v = self._h * self._w * self._l

    @property
    def h(self):
        return self._h

    @property
    def w(self):
        return self._w

    @property
    def l(self):
        return self._l

    @property
    def m(self):
        return self._l

    @property
    def v(self):
        return self._v

    def __str__(self):
        return f'height: {self._h}, width: {self._w}, length: {self._l}, mass: {self._m}, volume: {self._v}'


class Box(Cargo):
    def __str__(self):
        return f'height: {self._h}, width: {self._w}, length: {self._l}, mass: {self._m}, volume: {self._v}'


class Fridge(Cargo):
    def __str__(self):
        return f'height: {self._h}, width: {self._w}, length: {self._l}, mass: {self._m}, volume: {self._v}'


class Table(Cargo):
    def __str__(self):
        return f'height: {self._h}, width: {self._w}, length: {self._l}, mass: {self._m}, volume: {self._v}'


class BoxFactory:
    @staticmethod
    def create_boxes():
        return Box(h=random.uniform(2, 8), w=random.uniform(2, 8), l=random.uniform(2, 8),
                   m=random.uniform(2, 8))


class FridgeFactory:
    @staticmethod
    def create_fridges():
        return Fridge(h=random.uniform(3, 10), w=random.uniform(3, 10), l=random.uniform(3, 10),
                      m=random.uniform(3, 10))


class TableFactory:
    @staticmethod
    def create_tables():
        return Table(h=random.uniform(1, 7), w=random.uniform(1, 7), l=random.uniform(1, 7),
                     m=random.uniform(1, 7))


def create(name):
    if name == 'Box':
        return BoxFactory.create_boxes()
    elif name == 'Table':
        return TableFactory.create_tables()
    elif name == 'Fridge':
        return FridgeFactory.create_fridges()


def generator():
    for vagon in train:
        while True:
            cargo = create(random.choice(['Box', 'Table', 'Fridge']))
            if vagon.add(cargo):
                continue
            del cargo
            break


if __name__ == '__main__':
    random.seed(0)

    train = Train('№1', 0, 0)
    carriages = [Carriage.create(True, True) for _ in range(5)]

    for carriage in carriages:
        train.add_carriage(carriage)

    generator()

    for vagon in train:
        print(vagon.cargo_list)
