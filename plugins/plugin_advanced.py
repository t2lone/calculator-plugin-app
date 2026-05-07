import math

def register():
    return {
        'name': 'Расширенные операции',
        'operations': ['square', 'sqrt', 'power'],
        'calculate': calculate
    }

def calculate(op, a, b):
    if op == 'square':
        return a * a
    elif op == 'sqrt':
        if a < 0:
            return "Ошибка: корень из отрицательного числа"
        return math.sqrt(a)
    elif op == 'power':
        return a ** b
    return "Неизвестная операция"