def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел с проверкой на ноль"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b

def power(a, b):
    """Возведение в степень"""
    return a ** b

# Тестирование функций
if __name__ == "__main__":
    print("Тест сложения:", add(5, 3))
    print("Тест вычитания:", subtract(10, 4))
    print("Тест умножения:", multiply(3, 4))
    print("Тест деления:", divide(15, 3))
    print("Тест степени:", power(2, 3))
    
    try:
        divide(5, 0)  # Тест ошибки
    except ValueError as e:
        print("Тест ошибки деления на ноль:", e)
