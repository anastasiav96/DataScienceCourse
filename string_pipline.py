def replace_points(string):
    return string.replace('.', '')


def replace_comma(string):
    return string.replace(',', '')


def replace_double_spaces(string):
    return string.replace('  ', ' ')


def lower_str(string):
    return string.lower()


if __name__ == '__main__':
    file_w = open('output.txt', 'a')
    with open('data.txt', 'r') as f:
        for line in f:
            file_w.write(lower_str(replace_double_spaces(replace_comma(replace_points(line)))))
    file_w.close()
