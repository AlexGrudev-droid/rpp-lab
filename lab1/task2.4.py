text = input('Введите строку: ')
count_swap = 0
count_all = 0
final_text = ''
for i in text:
    count_all += 1
    if i == 'a':
        final_text += 'o'
        count_swap += 1
    else:
        final_text += i
print(f'Замен: {count_swap}\nВсего символов: {count_all}\nФинальный текст: {final_text}')