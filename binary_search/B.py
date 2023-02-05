'''
Задача B: Рядом
Вам дан отсортированный массив и запросы для поиска элемента, максимально близкого к запрошенному.
Если есть несколько значений с минимальной разницей по модулю, надо вывести минимальное.
'''

n, k = map(int, input().split())
N = list(map(int, input().split()))
K = list(map(int, input().split()))


def binary_search(key, last_key):
    start_element = 0
    end_element = n - 1

    while start_element <= end_element:
        middle_element = (start_element + end_element) // 2

        if N[middle_element] == key:
            return key
        elif N[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    if last_key != key:
        return binary_search(key + 1, key)
    else:
        return binary_search(key - 1, key)


for k_i in K:
    print(binary_search(k_i, k_i))