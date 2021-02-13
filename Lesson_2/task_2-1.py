# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе
# символа '0' в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    try:
        num1, operand, num2 = [i for i in input('Введите математическое выражение (число операнд число): ').split()]
    except ValueError:
        print('Неправильный ввод.')
        continue
    num1 = float(num1)
    num2 = float(num2)

    if operand == '0':
        break
    elif operand == '+':
        print(f'{num1} {operand} {num2} = {num1 + num2}')
    elif operand == '-':
        print(f'{num1} {operand} {num2} = {num1 - num2}')
    elif operand == '*':
        print(f'{num1} {operand} {num2} = {num1 * num2}')
    elif operand == '/':
        try:
            print(f'{num1} {operand} {num2} = {num1 / num2}')
        except ZeroDivisionError:
            print('Деление на ноль невозможно')