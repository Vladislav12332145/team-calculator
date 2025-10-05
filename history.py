# history.py - модуль для истории операций калькулятора

# Глобальный список для хранения истории операций
history = []

def add_to_history(operation, a, b, result):
    """
    Добавляет операцию в историю вычислений
    
    Args:
        operation (str): символ операции (+, -, *, /, **)
        a (float): первое число
        b (float): второе число  
        result (float): результат операции
    """
    history_entry = {
        'operation': operation,
        'a': a,
        'b': b,
        'result': result
    }
    history.append(history_entry)
    print(f"✅ Операция добавлена в историю: {a} {operation} {b} = {result}")

def show_history():
    """Показывает всю историю операций"""
    if not history:
        print("📝 История операций пуста")
        return
    
    print("\n📋 ИСТОРИЯ ОПЕРАЦИЙ:")
    print("-" * 40)
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry['a']} {entry['operation']} {entry['b']} = {entry['result']}")
    print("-" * 40)

def clear_history():
    """Очищает историю операций"""
    history.clear()
    print("🗑️ История операций очищена")

def get_history_count():
    """Возвращает количество операций в истории"""
    return len(history)

def get_last_operation():
    """Возвращает последнюю операцию или None если история пуста"""
    if not history:
        return None
    return history[-1]

# Тестирование модуля
if __name__ == "__main__":
    print("🧪 Тестируем модуль истории...")
    
    # Добавляем тестовые операции
    add_to_history('+', 5, 3, 8)
    add_to_history('*', 2, 4, 8)
    add_to_history('/', 10, 2, 5)
    
    # Показываем историю
    show_history()
    
    # Показываем количество операций
    print(f"Всего операций в истории: {get_history_count()}")
    
    # Показываем последнюю операцию
    last_op = get_last_operation()
    if last_op:
        print(f"Последняя операция: {last_op['a']} {last_op['operation']} {last_op['b']} = {last_op['result']}")
    
    # Очищаем историю
    clear_history()
    show_history()
