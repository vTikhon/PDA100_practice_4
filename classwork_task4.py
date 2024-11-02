# Задание
# Напишите программу, которая определяет самое длинное слово в файле. В качестве
# результата длина самого длинного слова и все слова такой длины. Любые не
# пробельные символы, включая цифры и знаки препинания, принимаем за значимые
# буквы.


def open_file(path):
    with open(path, 'r', encoding='utf8') as f:
        return f.read()

def get_length_and_words(s):
    new_s = s.replace('\n', ' ').replace('\t', ' ')
    data = new_s.split()
    max_word = max(data, key=len)
    length = len(max_word)
    res = [s for s in data if len(s) == length]
    return length, res

if __name__ == '__main__':
    str_ = open_file('test.txt')
    tup = get_length_and_words(str_)
    print(*tup)
