def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def umn(a, b):
    return a * b
def delit(a, b):
    return a / b

if __name__ == "__main__":
    while True:
        choose_oper = input('Введите операцию: ')
        if choose_oper == '+':
            try:
                a = float(input('Введите первое число: '))
                b = float(input('Введите второе число: '))
                print(plus(a, b))
            except:
                print('Ошибка в вводе')
        elif choose_oper == '-':
            try:
                a = float(input('Введите первое число: '))
                b = float(input('Введите второе число: '))
                print(minus(a, b))
            except:
                print('Ошибка в вводе')
        elif choose_oper == '*':
            try:
                a = float(input('Введите первое число: '))
                b = float(input('Введите второе число: '))
                print(umn(a, b))
            except:
                print('Ошибка в вводе')
        elif choose_oper == '/':
            try:
                a = float(input('Введите первое число: '))
                b = float(input('Введите второе число: '))
                print(delit(a, b))
            except ZeroDivisionError:
                print('Нельзя делить на ноль!')
            except:
                print('Ошибка в вводе')
        else:
            print('Ошибка в операции')