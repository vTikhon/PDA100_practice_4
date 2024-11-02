import statistics
import requests

# Задание
# В файле temper.stat представлена ежемесячная максимальная температура в градусах по Фаренгейту одного
# из аэропортов мира в период с 1948 по 2016.
# Необходимо определить максимальные и минимальные значения, среднюю
# температуру.
# Определить, сколько уникальных температур содержится в файле.
# начало решения
# Файл temper.stat

def get_response(url_):
    result = requests.get(url_)
    list_ = result.text.split('\n')
    return list_.pop()

def get_min(list_):
    new_list = [float(el) for el in list_]
    return min(new_list)

def get_max(list_):
    return max(map(float, list_))

def get_avg(list_):
    return statistics.mean(map(float, list_))

def get_unique(list_):
    return len(set(map(float, list_)))

url = 'https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat'

if __name__ == '__main__':
    data = get_response(url)
    print(data)
    print(get_min(data))
    print(get_max(data))
    print(get_avg(data))
    print(get_unique(data))