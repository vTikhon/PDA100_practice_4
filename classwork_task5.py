import requests
from collections import Counter

# Задание
# Определите частоту встречаемости слов для текста, расположенного в сети Интернет:
# http://dfedorov.spb.ru/python3/src/romeo.txt
# collections -> Counter

url = 'http://dfedorov.spb.ru/python3/src/romeo.txt'

def get_response(url_):
    return requests.get(url_).text

def count_words(s):
    list_ = s.lower().replace('\n', ' ').strip().split(' ')
    return dict(Counter(list_))

if __name__ == '__main__':
    s = get_response(url)
    print(count_words(s))