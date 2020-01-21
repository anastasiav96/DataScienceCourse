def measure_time(func):
    import timeit

    def wrapper(*args, **kwargs):
        time_start = timeit.default_timer()
        func(*args, **kwargs)
        print(timeit.default_timer() - time_start, 'seconds')

    return wrapper


@measure_time
def search(s, n):
    for i in n:
        if i in s:
            pass


def get_random_stack_needles(stack_size):
    stack_list = [random.random() for _ in range(stack_size)]
    needles_list = [random.choice(stack_list) for _ in range(500)]
    needles_list.extend([random.random() for _ in range(500)])

    return stack_list, needles_list


def get_dict_stack(stack_list):
    return dict(zip(stack_list, range(len(stack_list))))


if __name__ == '__main__':
    import random

    size_stack = [1000, 10000, 100000, 1000000]

    for size in size_stack:
        print('Size of stack: ', size)
        stack, needles = get_random_stack_needles(size)
        
        print('Search in list takes:', end=' ')
        search(stack, needles)
        
        print('Search in tuple takes:', end=' ')
        search(tuple(stack), needles)
        
        print('Search in dict takes:', end=' ')
        search(get_dict_stack(stack), needles)
