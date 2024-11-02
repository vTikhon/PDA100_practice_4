# Задание
# В файле text2.txt в каждой строке хранится одно предложение. Напишите программу,
# которая читает содержимое файла и вычисляет:
# • количество букв в файле в верхнем регистре;
# • количество цифр в файле;
# • количество пробельных символов в файле.

def find_count_chars(path):
    with open(path, 'r', encoding='utf8') as f:
        s = f.read()
        dict_ = {'space chars': 0}
        dict_['upper chars'] = len([ch for ch in s if ch.isupper()])
        dict_['digit chars'] = len(list(filter(lambda x: x.isdigit(), s)))
        for ch in s:
            if ch.isspace():
                dict_['space chars'] += 1
        return dict_

if __name__ == '__main__':
    print(find_count_chars('test2.txt'))