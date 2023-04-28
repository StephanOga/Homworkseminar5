def sum_rec(number1, number2):
    if number2 == 0:
        return number1
    result = sum_rec(number1, number2 - 1) + 1
    return result


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(f'Сумма этих чисел равна {sum_rec(a, b)}')