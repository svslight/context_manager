
from datetime import datetime
# from timeit import default_timer as timer

start_time = datetime.now()
# start = timer()

import codecs
import functools

open = functools.partial(codecs.open, encoding='utf-8')


class Points:
    def __init__(self, path, path2, encoding='utf-8'):
        self.path = path
        self.path2 = path2
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.path)
        self.file2 = open(self.path2)
        self.list_txt = self.file.read()  # читаем первый файл
        self.list_txt2 = self.file2.read()  # читаем второй файл
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print('File 1 close')
        self.file.close()
        print('File 2 close')


with Points('points.txt', 'graphs.txt') as points:
    list_points = points.list_txt.splitlines()   # strip splitlines()  split('\n') rstrip('\n')
    dict_points = {}
    for line in list_points:
        line = line.split(' ')
        dict_points[line[0]] = line[1:]

    for keys, values in dict_points.items():
        print('Точка:{} Соответствует координатам: {}'.format(keys, values))

    list_graphs = points.list_txt2.splitlines()
    dict_graphs = {}
    for line in list_graphs:
        line = line.split(' ')
        dict_graphs[line[0]] = line[1:]

    for keys, values in dict_graphs.items():
        print('Название пути:{} точки, через которые он проходит: {}'.format(keys, values))

end_time = datetime.now()
# end = timer()
print('Время запуска кода: {}'.format(start_time))
print('Время окончания работы кода: {}'.format(end_time))
print('Время выполнения: {}'.format(end_time - start_time))
# print('Время выполнения: {}'.format(end - start))