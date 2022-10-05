from decimal import *


print ('Калькулятор')


def calculate():

    q1 = Decimal(input('Введите первое число: '))
    q2 = Decimal(input('Введите второе число: '))
    operator_choice = int(input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

    if operator_choice == 1:
        result = q1 + q2
        operation = 'сложения'

    if operator_choice == 2:
        result = (q1 - q2)
        operation = 'вычитания'

    if operator_choice == 3:
        try:
            result = Decimal(q1 / q2)
        except ZeroDivisionError:
            return print('На ноль делить нельзя!')
        operation = 'деления'


    if operator_choice == 4:
        result = Decimal(q1 * q2)
        operation = 'умножения'

    print('Результат ', operation, ' = ', result)



while True:
    calculate()
