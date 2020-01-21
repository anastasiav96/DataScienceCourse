def measure_time(func):
    import timeit

    def wrapper(*args, **kwargs):
        time_start = timeit.default_timer()
        func(*args, **kwargs)
        print(f'Function {func.__name__} takes {timeit.default_timer() - time_start} seconds')

    return wrapper


@measure_time
def list_search(s, n):
    for i in n:
        if i in s:
            s.index(i)


@measure_time
def tuple_search(s, n):
    for i in n:
        if i in s:
            s.index(i)


@measure_time
def dict_search(s, n):
    for i in n:
        if i in s.keys():
            s.get(i)


def get_random_stack_needles(stack_size):
    stack_list = [random.random() for i in range(stack_size)]
    needles_list = [random.choice(stack_list) for j in range(stack_size // 2)]
    needles_list.extend([random.random() for k in range(stack_size // 2)])

    return stack_list, needles_list


def get_tuple_stack(stack_list):
    return tuple(stack_list)


def get_dict_stack(stack_list):
    return dict(zip(stack_list, range(len(stack_list))))


if __name__ == '__main__':
    import random

    size_stack = [100000, 1000000, 10000000]

    for size in size_stack:
        print('Size of stack: ', size)
        stack, needles = get_random_stack_needles(size)

        list_search(stack, needles)
        tuple_search(get_tuple_stack(stack), needles)
        dict_search(get_dict_stack(stack), needles)
        
