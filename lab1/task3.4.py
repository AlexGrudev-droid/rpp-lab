import sys

args_list = sys.argv
array = []
for i in range(1, len(args_list)):
    array.append(int(args_list[i]))
max_element = max(array)
index = array.index(max_element)
odds_array = []
for element in array:
    if element % 2:
        odds_array.append(element)
odds_array.sort(reverse=True)
odds_array = ' '.join(map(str, odds_array))
if odds_array:
    print(f'Нечетные элементы в порядке убывания: {odds_array}')
else:
    print('Список пуст')
print(f'Максимальный элемент: {max_element} с индексом {index}')