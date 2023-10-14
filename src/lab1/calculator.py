def calc(oper):
    if oper[-2:] == '/0':
        return 'Делить на ноль нельзя'
    a = '012345678908+.-*/%'
    f = 1
    for i in oper:
        if i not in a:
            f = 0
    if f:
        return eval(oper)
    return 'Неверный ввод. Пишите слитно, используя существующие числа и знаки операций'

if __name__ == "__main__":
    print("Калькулятор")
    p = input("Что нужно посчитать? Используй знаки(+, -, *, /)\n")
    print(calc(p))
