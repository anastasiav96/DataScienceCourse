def calculator(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        try:
            return x / y
        except ZeroDivisionError as e:
            return e


if __name__ == '__main__':
    while True:
        operation = input('Input your operation (+, -, *, /) or input "q" for exit:   ')
        if operation != 'q':
            x, y = int(input('Input first number:   ')), int(input('Input second number:   '))
            print(calculator(x, y, operation))
        else:
            print('Goodbye!')
            break
