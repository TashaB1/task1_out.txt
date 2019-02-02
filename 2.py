import re, os, sys, argparse
from tkinter import messagebox as mb
def createParser():
    parser = argparse.ArgumentParser(description='Формирование выходного файла "out.txt" из файла "a.txt", с изменением чисел на соответствующие значения из файла "b.txt".')
    parser.add_argument('-a', '--file_a', nargs='?', type=argparse.FileType(mode='r', encoding='utf-8'),  help='Исходный файл, на основании которого формируется выходной файл', metavar='ИСХОДНЫЙ ФАЙЛ')
    parser.add_argument('-b', '--file_b', nargs='?', type=argparse.FileType(mode='r', encoding='utf-8'),  help='Файл, содержащий значения для замены', metavar='ФАЙЛ-СЛОВАРЬ')
    return parser
def fun1(m):
    return dict1[int(m[0])] if int(m[0]) in dict1 else '<Значение номера "' + m[0] + '" не задано> '
def run(file_a,file_b):
    for line in file_b:
        m = re.search('(\d+)[\s.)]([\D\d]+[^\n])', line)
        if m:  # проверка на соответствие шаблону
            if int(m[1]) in dict1:  # проверка дублей ключей
                answer = mb.askyesno(title='Внимание!', message='Значение номера "' + m[1] + '" задано: "' + dict1[int(m[1])] + '". Перезаписать его новым: "' + m[2] + '"?')
                if answer: dict1[int(m[1])] = m[2]
            else:
                dict1[int(m[1])] = m[2]
    if dict1:
        f3 = open("out.txt", "w")  # ?1
        for line in file_a:
            with open("out.txt", "a") as f3:  # ?1
                f3.write(re.sub(r'(\d+)', fun1, line))
        mb.showinfo('Информация', 'Выходной файл ' + os.getcwd() + '\out.txt успешно сформирован.')
    else:
        mb.showinfo('Информация', 'Файл, содержащий значения для замены, пустой.')
if __name__ == '__main__':
    parser = createParser()
    files = parser.parse_args(sys.argv[1:])
    dict1 = dict()
    parser.print_help() if files.file_a == None or files.file_a == None else run(files.file_a, files.file_b)

