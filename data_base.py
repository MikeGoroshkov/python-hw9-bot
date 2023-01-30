import os

def data_write(fullname, number, description):
    with open('base.txt', 'a', encoding='utf8') as file:
        file.write(f'{fullname}:{number}:{description}\n')

def data_read_base():
    with open('base.txt', 'r', encoding='utf8') as file:
        base = [line.split(':') for line in file]
    return base

def find_data(desired):
    base = data_read_base()
    finded = []
    for item in base:
        try:
            if desired.lower() in item[0].lower() or desired in item[1]:
                finded.append(item)
        except:
            continue
    return finded

def delete_data(finded):
    for i in finded:
        os.rename('base.txt', 'base_tmp.txt')
        with open('base_tmp.txt', 'r', encoding='utf8') as file:
            for line in file:
                if line != f'{str(i[0])}:{str(i[1])}:{str(i[2])}':
                    with open('base.txt', 'a', encoding='utf8') as f:
                        f.write(line)
        os.remove('base_tmp.txt')
