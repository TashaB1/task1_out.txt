import re
import os
import sys
import argparse
import logging

def createParser():
    parser = argparse.ArgumentParser(description='Формирование выходного файла "out.txt" из файла "a.txt", с изменением чисел на соответствующие значения из файла "b.txt".')
    parser.add_argument('-a', '--file_a', nargs='?', type=argparse.FileType(mode='r', encoding='utf-8'),  help='Исходный файл, на основании которого формируется выходной файл', metavar='ИСХОДНЫЙ ФАЙЛ')
    parser.add_argument('-b', '--file_b', nargs='?', type=argparse.FileType(mode='r', encoding='utf-8'),  help='Файл, содержащий значения для замены', metavar='ФАЙЛ-СЛОВАРЬ')
    return parser

def fun1(m):
    return dict1[int(m[0])] if int(m[0]) in dict1 else logging.error(' Значение номера "' + m[0] + '" не задано. ')

def run(file_a,file_b):
    for line in file_b:
        m = re.search('(\d+)[\s.)]([\D\d]+[^\n])', line)
        if m:  # проверка на соответствие шаблону
            if int(m[1]) in dict1:  # проверка дублей ключей
                logging.info(' Внимание! Для номера "' + m[1] + '" задано несколько значений. Номеру присвоено последнее для него значение в списке.')
            dict1[int(m[1])] = m[2]
    if not dict1:
        logging.error(' Файл, содержащий значения для замены, не соответствует требуемой структуре.')
        parser.print_help()
    f3 = open(os.getcwd() + r"\resources\out.txt", "w")  # ?1
    for line in file_a:
        with open(os.getcwd() + r"\resources\out.txt", "a", encoding="utf-8") as f3:  # ?1
            f3.write(re.sub(r'(\d+)', fun1, line))
    logging.info(' Выходной файл ' + os.getcwd() + r'\resources\out.txt сформирован.')

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(os.getcwd() + r'\resources\log.txt', 'w', 'utf-8')], level=logging.INFO)
    parser = createParser()
    files = parser.parse_args(sys.argv[1:])
    dict1 = dict()
    parser.print_help() if files.file_a is None or files.file_a is None else run(files.file_a, files.file_b)
