import os.path
import random

# Задание
# Волшебный шар. Напишите программу, которая моделирует игрушку,
# предсказывающую будущее: дает случайный ответ на общий вопрос, требующий ответа
# "да" или "нет". Файл с ответами: responses_task7.txt. Программа должна предложить
# пользователю задать вопрос и затем показать один из ответов, отобранных из файла
# случайным образом. Программа должна продолжать работу до тех пор, пока
# пользователь не будет готов из нее выйти.

def magic_ball():
    while True:
        s = input('Хотите сыграть в игру? (да\нет): ')
        if s.lower() == 'нет':
            break
        random_answer(input('Задайте вопрос: '))

def random_answer(txt):
    filename = 'responses_task7.txt'
    key = 'a'
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('да\nнет')
    with open(filename, 'r', encoding='utf-8') as f:
        answer = f.readlines()
    if not os.path.exists(filename):
        key = 'w'
    with open('results_task7.txt', key, encoding='utf8') as f:
        f.write(f'{txt}: {random.choice(answer)}\n')


if __name__ == '__main__':
    magic_ball()