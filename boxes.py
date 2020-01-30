'''
Домашнее задание №5
Написать программу реализующую заполнение вагона коробками разного размера.

Нужно создать 2 класса:
- вагон, атрибуты: высота, ширина, длина, список коробок, текущая масса
(состоящая из массы всех коробок загруженных в вагон), максимальная масса груза которую можно поместить в вагон
- коробка, атрибуты: высота, ширина, длина, масса

Программа должна:
- автоматически создавать объекты вагона (константа: 1 штука) и коробок (константа: 10 штук) с произмольными,
но реалистичными, значениями атрибутов (высота, ширина, длина и масса для коробок и максимальная масса для вагона)
- заполнять вагон коробками

В вагон можно поместить коробку если:
- размер коробки по всем измерениям не превышает размер вагона
- текущая масса вагона, с учетом коробки которую хотим поместить, не превышает максимальную массу вагона
- заполненный объем вагона, с учетом коробки которую хотим поместить, не превышает общий объем вагона

В результате программа должна вывести следующие обьекты с атрибутами:
- вагон
- коробки которые удалось поместить в вагон
- коробки которые не удалось поместить в вагон
'''


class Car:
    def __init__(self, height, width, length, max_mass):
        self.height = height
        self.width = width
        self.length = length
        self.max_mass = max_mass

        self.list_boxes = []
        self.total_mass_boxes = 0
        self.volume = self.height * self.width * self.length

    def add_in_car(self, box):
        self.list_boxes.append(box)

    def add_mass(self, box_mass):
        self.total_mass_boxes += box_mass

    def volume_change(self, box_volume):
        self.volume -= box_volume


class Box:
    def __init__(self, height, width, length, box_mass):
        self.height = height
        self.width = width
        self.length = length
        self.box_mass = box_mass

        self.volume = self.height * self.width * self.length


def generate_boxes(n=10):
    boxes = {'box_{}'.format(i): random.sample(range(1, 10), 4) for i in range(1, n + 1)}
    box_classes = {k: Box(boxes[k][0], boxes[k][1], boxes[k][2], boxes[k][3]) for k in boxes}
    # print(boxes)
    return boxes, box_classes


def generate_car(n=1):
    cars = {'car_{}'.format(j): random.sample(range(10, 40), 4) for j in range(1, n + 1)}
    car_classes = {k: Car(cars[k][0], cars[k][1], cars[k][2], cars[k][3]) for k in cars}
    # print(cars)
    return cars, car_classes


if __name__ == '__main__':
    import random
    random.seed(0)

    cars_list, cars = generate_car(5)
    boxes_list, boxes = generate_boxes(10)

    for car in cars:
        for box in boxes:
            if (cars[car].height - boxes[box].height >= 0) and (cars[car].width - boxes[box].width >= 0) and (
                    cars[car].length - boxes[box].length >= 0) and (
                    boxes[box].box_mass + cars[car].total_mass_boxes <= cars[car].max_mass) and (
                    cars[car].volume - boxes[box].volume >= 0):
                cars[car].add_in_car(box)
                cars[car].add_mass(boxes[box].box_mass)
                cars[car].volume_change(boxes[box].volume)

        boxes_in_car = cars[car].list_boxes
        boxes_not_in_car = list(set(boxes.keys()) - set(cars[car].list_boxes))
        boxes = {k: v for (k, v) in boxes.items() if k in boxes_not_in_car}

        if not boxes_in_car:
            print('All boxes loaded on cars')
            break

        print('Car name: ', car)
        print('Boxes in {} : '.format(car), boxes_in_car)
        print('Boxes not in cars: ', boxes_not_in_car)
