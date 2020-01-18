def replace_points(string):
    return string.replace('.', '')


def replace_commas(string):
    return string.replace(',', '')


def replace_double_spaces(string):
    return string.replace('  ', ' ')


def lower_str(string):
    return string.lower()


if __name__ == '__main__':
    with open('output.txt', 'w') as file_w, open('data.txt', 'r') as f:
        for line in f:
            line = replace_points(line)
            line = replace_commas(line)
            line = replace_double_spaces(line)
            line = lower_str(line)
            file_w.write(line)
