def register():
    return {
        'name': 'Базовые операции',
        'operations': ['+', '-', '*', '/'],
        'calculate': calculate
    }

def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    return "Неизвестная операция"