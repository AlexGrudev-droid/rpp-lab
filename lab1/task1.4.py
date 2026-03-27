sum = 0
count = 0
num = int(input('Введите число: '))
while num != 0:
    sum += num
    count += 1
    num = int(input('Введите число: '))
print(f'Сумма: {sum}, счетчик: {count}')