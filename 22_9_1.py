error = 'Ошибка. Перезапустите программу'
all_numbers = input('Введите последовательность целых чисел через пробел: ')
input_number = int(input('Введите любое число: '))


def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False


if " " not in all_numbers:
    print("\nВ вводе нет пробелов. (введите числа, соответсвующие условиям ввода.)")
    all_numbers = input('Введите целые числа через пробел: ')
if not is_int(all_numbers):
    print('\nВ вводе содержатся не целые числа или не числа. (введите числа, соответствующие условиям ввода.)\n')
    print(error)
else:
    all_numbers = all_numbers.split()

list_all_numbers = [int(item) for item in all_numbers]


def merge_sort(l):
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = merge_sort(l[:middle])
        right = merge_sort(l[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_all_numbers = merge_sort(list_all_numbers)


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Введенное число выходит за диапазон списка, введите меньшее число.'


print(f'Список по возрастанию: {list_all_numbers}')

if not binary_search(list_all_numbers, input_number, 0, len(list_all_numbers)):
    rI = min(list_all_numbers, key=lambda x: (abs(x - input_number), x))
    ind = list_all_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < input_number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_all_numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_all_numbers.index(rI)}
В списке нет меньшего элемента''')
    elif rI > input_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_all_numbers.index(rI)}
Ближайший меньший элемент: {list_all_numbers[min_ind]} его индекс: {min_ind}''')
    elif list_all_numbers.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_all_numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_all_numbers, input_number, 0, len(list_all_numbers))}')
