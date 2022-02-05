from chardet import detect

with open('task6.txt', 'w', encoding='utf-8') as fl:
    fl.write('сетевое программирование\nсокет\nдекоратор')

with open('task6.txt', 'rb') as fl:
    content = fl.read()
encoding = detect(content)['encoding']

with open('task6.txt', 'r', encoding=encoding) as fl:
    context = fl.read()
print(context)
