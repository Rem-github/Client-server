
data_set = ['разработка', 'администрирование', 'protocol', 'standard']
data_set_bytes = []

for d in data_set:
    data = d.encode('utf-8')
    data_set_bytes.append(data)
    print(data)

for d in data_set_bytes:
    data = d.decode('utf-8')
    print(data)
    