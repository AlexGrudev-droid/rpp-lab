num1 = int(input('Введите 1 число: '))
num2 = int(input('Введите 2 число: '))
num3 = int(input('Введите 3 число: '))
numbers = [num1, num2, num3]
for i in range(len(numbers)):
    if 50 >= numbers[i] >= 1:
        print('Число в диапозоне [1,50]: ', numbers[i])