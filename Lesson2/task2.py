import json

orders = []

def write_order_to_json(item, quantity, price, buyer, date):

    dict = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    orders.append(dict)
    DICT_TO_JSON = {'orders': orders}

    with open('orders.json', 'w', encoding='utf-8') as fl:
        json.dump(DICT_TO_JSON, fl, indent=4, ensure_ascii=False)


write_order_to_json('Мой программный продукт',1,2500,'Теперь очень несчастный человек','10.02.2022')
write_order_to_json('Обучение Python',1,100500,'Думает, что выучит(зря)','10.02.2022')
