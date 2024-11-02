# Задание
# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным
# источникам.
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100
# Пример работы программы:
# results = { 'vk': {'revenue': 103, 'cost': 98},
# 'yandex': {'revenue': 179, 'cost': 153}, 'ok': {'revenue': 103, 'cost': 110},
# 'adwords': {'revenue': 35, 'cost': 34}, 'twitter': {'revenue': 11, 'cost': 24}, }
# Результат: {'adwords': {'revenue': 35, 'cost': 34, 'ROI': 2.94},
# 'ok': {'revenue': 103, 'cost': 110, 'ROI': -6.36},
# 'twitter': {'revenue': 11, 'cost': 24, 'ROI': -54.17}, 'vk': {'revenue': 103, 'cost': 98, 'ROI': 5.1},
# 'yandex': {'revenue': 179, 'cost': 153, 'ROI': 16.99}}

def add_roi(dict_: dict) -> dict:
    for value in dict_.values():
        value['ROI'] = round((value['revenue'] / value['cost'] - 1) * 100, 2)
    return dict_

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'ok': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24}
}

print(add_roi(results))




# Задание
# Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже).
# Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.
# Пример работы программы:
# queries = [ 'смотреть сериалы онлайн', 'новости спорта', 'афиша кино', 'курс доллара', 'сериалы этим летом',
# 'курс по питону', 'сериалы про спорт', ]
# Результат: Поисковых запросов, содержащих 2 слов(а): 42.86% Поисковых запросов, содержащих 3 слов(а): 57.14%

def count_words(list_):
    data = []
    for el in list_:
        data.append(len(el.split()))
    for i in set(data):
        print(f'Поисковых запросов, содержащих {i} слов(а): {round((data.count(i) / len(data))* 100, 2)}%')


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

count_words(queries)



# Задание
# Наши данные представляют собой словарь словарей, в которых хранится почасовая оплата сотрудников компании.
# Задача - получить список компаний, которые платят ниже минимальной заработной платы (< 9 долларов США) хотя бы
# для одного сотрудника.
# companies = { 'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
# 'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
# 'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}
# Ответ: ['CheapCompany', 'SosoCompany']

companies = {
    'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
    'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}
}

def appender(dict_):
    res = []
    for key, value in dict_.items():
        for v in value.values():
            if v < 9:
                res.append(key)
    return sorted(set(res))

print(appender(companies))

