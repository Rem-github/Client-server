import yaml

LIST_TO_YAML = ['Корова', 'лезет', 'на', 'акацию']
INT_TO_YAML = 777
SET_TO_YAML = {
    'сообразим': '1000р',
    'на': '2000р',
    'троих': '3р',
}

DATA_TO_YAML = {
    'list': LIST_TO_YAML,
    'int': INT_TO_YAML,
    'dict': SET_TO_YAML,
}

with open('yamlfile.yaml', 'w', encoding='utf-8') as fl:
    yaml.dump(DATA_TO_YAML, fl, default_flow_style=False, allow_unicode=True)
