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
    print("-" * 30)
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry['a']} {entry['operation']} {entry['b']} = {entry['result']}")
    print("-" * 30)

def clear_history():
    """Очищает историю операций"""
    history.clear()
    print("🗑 История операций очищена")

def get_history_count():
    """Возвращает количество операций в истории"""
    return len(history)

# Пример использования (можно удалить потом)
if name == "main":
    print("🧪 Тестируем модуль истории...")
    add_to_history('+', 5, 3, 8)
    add_to_history('*', 2, 4, 8)
    show_history()
    print(f"Всего операций: {get_history_count()}")