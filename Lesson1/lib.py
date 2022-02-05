def bytes_create(data):
    for i in range(len(data)):
        if ord(data[i]) > 127:
            return print(f'Слово "{data}" не может быть записано в байтовом типе без преобразования')
    data_byte = eval("b" + f"'{data}'")
    print(f'Набор данных {data_byte} имеет тип {type(data_byte)} и длину {len(data)} символов')

def check_data(data):
    for d in data:
        print(f'Набор данных "{d}" имеет тип {type(d)}')