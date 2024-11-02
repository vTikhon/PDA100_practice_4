import os.path

# Задание
# Объедините содержимое нескольких файлов. Файлы сцепляются в том порядке, в
# котором указываются с клавиатуры. Добавьте обработку ошибок, если файл не может
# быть открыт.
# Укажите входные файлы:
# 1.txt 2.txt
# Укажите выходной файл:
# 3.txt

def union_files(*inputfiles, outputfile):
    key = 'w'
    if os.path.exists(outputfile):
        key = 'a'
    with open(outputfile, key, encoding='utf8') as output_f:
        try:
            for file in inputfiles:
                try:
                    with open(file, 'r', encoding='utf8') as input_f:
                        output_f.write(input_f.read())
                except FileNotFoundError:
                    print(f'Файл {input_f} не найден')
        except UnboundLocalError:
            print('Ошибка! Не удалось открыть файл')

if __name__ == '__main__':
    union_files('test.txt', 'test2.txt', outputfile='outputfile_task8.txt')