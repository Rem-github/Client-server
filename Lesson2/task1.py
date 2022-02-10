import csv
import re

from chardet import detect


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']

    for i in range(3):
        datafile = f'info_{i+1}.txt'
        with open(datafile, 'rb') as fl:
            content = fl.read()
        encoding = detect(content)['encoding']

        with open(datafile, 'r', encoding=encoding) as fl:
            context = csv.reader(fl)
            for row in context:
                for name in main_data:
                    key = r'^' + name
                    match = re.search(key, row[0])
                    if match:
                        if name == 'Изготовитель ОС':
                            m = re.search(r'():(\s+([\w+\s+\-]+))', row[0])
                            os_prod_list.append(m.group(3))
                        elif name == 'Название ОС':
                            m = re.search(r'():(\s+([\w+\s+\-]+))', row[0])
                            os_name_list.append(m.group(3))
                        elif name == 'Код продукта':
                            m = re.search(r'():(\s+([\w+\s+\-]+))', row[0])
                            os_code_list.append(m.group(3))
                        elif name == 'Тип системы':
                            m = re.search(r'():(\s+([\w+\s+\-]+))', row[0])
                            os_type_list.append(m.group(3))
    main_data = [main_data]
    for i in range(3):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])


    return main_data

def write_to_csv(link):

    data = get_data()
    with open(link, 'w', encoding='utf-8') as fl:
        fl_writer = csv.writer(fl)
        fl_writer.writerows(data)

write_to_csv('result.csv')