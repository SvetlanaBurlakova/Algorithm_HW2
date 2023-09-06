from random import randint,choice
from time import time

UPPER = 10

def how_long(func_list, x):
    for func in func_list:
        start = time()
        func(x)
        print(f'На запуск {func} это ушло времени {time() - start}')

def heap_sort(lst):
    length = len(lst)
    for i in range(length // 2 - 1, -1, -1):
        heap_sort_recursion(lst, length, i) # построение дерева
    for i in range(length - 1, 0, -1):
        lst[0],lst[i] = lst[i],lst[0] # перемещаем текущий корневой элемент в конец
        heap_sort_recursion(lst, i, 0) # вызываем процедуру на уменьшенном дереве
    print(lst)

def heap_sort_recursion(lst, n, i):
    max_n = i # инициализация корневого элемента - индекс
    left = max_n * 2 + 1 # индекс левого элемента
    right = max_n * 2 + 2 # индекс правого элемента
    if (left < n and lst[i] < lst[left]):
        max_n = left # если левый элемент больше корневого, то максимальный элемент становится левый
    if (right < n and lst[max_n] < lst[right]):
        max_n = right # если правый элемент больше корневого, то максимальный становится правый
    if (max_n != i): # если  максимальный не равен корневому, то делаем замену корневого
        lst[i], lst[max_n] = lst[max_n], lst[i]
        heap_sort_recursion(lst, n, max_n) # рукурсивно проверяем поддерево

lst = [randint(-10,10) for _ in range(UPPER)]
print(lst)
heap_sort(lst)
func_list = []
#func_list.append(heap_sort)