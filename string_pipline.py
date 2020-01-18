def replace_points(string):
    return string.replace('.', '')


def replace_commas(string):
    return string.replace(',', '')


def replace_double_spaces(string):
    return string.replace('  ', ' ')


def lower_str(string):
    return string.lower()


if __name__ == '__main__':
    file_w = open('output.txt', 'w')
    with open('data.txt', 'r') as f:
        for line in f:
            file_w.write(lower_str(replace_double_spaces(replace_commas(replace_points(line)))))
    file_w.close()
