def split_data(string):
    return list(filter(None, (re.split(r'[\n\t;-]', string))))


def get_id(lst):
    match = re.search(r'\d+', lst[0])
    return match[0] if match else None


def get_name(lst):
    match = re.search(r'[a-zA-Z]+', lst[1])
    return match[0] if match else None


def get_age(lst):
    match = re.search(r'\d+', lst[2])
    return match[0] if match else None


def get_phone(lst):
    match = re.search(r'^\++\d{,12}', lst[3])
    return match[0] if match else None


def get_email(lst):
    match = re.search(r'[a-zA-Z1-9]+@+[a-zA-Z]+\.[a-zA-Z]+', lst[4])
    return match[0] if match else None


def get_role(lst):
    match = re.search(r'\badmin\b|\buser\b|\bguest\b', lst[5])
    return match[0] if match else None


def get_status(lst):
    match = re.search(r'\bactive\b|\binactive\b', lst[6])
    return match[0] if match else None


if __name__ == '__main__':
    import re
    
    persons = []
    with open('data.txt', 'r') as f:
        header = f.readline()
        keys = split_data(header)

        for line in f.readlines()[1:]:
            data = split_data(line)
            data = [get_id(data), get_name(data), get_age(data), get_phone(data), get_email(data), get_role(data),
                    get_status(data)]
            person = dict(zip(keys, data))
            persons.append(person)
            
    print(persons)
