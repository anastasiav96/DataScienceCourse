def split_data(string):
    return list(filter(None, (re.split(r'[\n\t;-]', string))))


def get_id(string):
    match = re.search(r'^\d+$', string)
    return match[0] if match else None


def get_name(string):
    match = re.search(r'^[a-zA-Z]+$', string)
    return match[0] if match else None


def get_age(string):
    match = re.search(r'^\d+$', string)
    return match[0] if match else None


def get_phone(string):
    match = re.search(r'^\+\d{,12}$', string)
    return match[0] if match else None


def get_email(string):
    match = re.search(r'^[a-zA-Z1-9]+@[a-zA-Z]+\.[a-zA-Z]+$', string)
    return match[0] if match else None


def get_role(string):
    match = re.search(r'^admin$|^user$|^guest$', string)
    return match[0] if match else None


def get_status(string):
    match = re.search(r'^active$|^inactive$', string)
    return match[0] if match else None


if __name__ == '__main__':
    import re
    
    persons = []
    with open('data.txt', 'r') as f:
        header = f.readline()
        keys = split_data(header)

        for line in f.readlines()[1:]:
            data = split_data(line)
            val_data = [get_id(data[0]), get_name(data[1]), get_age(data[2]), get_phone(data[3]), get_email(data[4]), 
                        get_role(data[5]), get_status(data[6])]
            
            person = dict(zip(keys, val_data))
            persons.append(person)
            
    print(persons)
