def exponentiation_rec(base, exponent):
    if exponent == 0:
        return 1
    result = base * exponentiation_rec(base, exponent - 1)
    return result


a = int(input('Введите основание степени: '))
b = int(input('Введите показатель степени: '))
print(f'{a} в степени {b} равно {exponentiation_rec(a, b)}')