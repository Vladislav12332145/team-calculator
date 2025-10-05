import operations
import history

def run_tests():
    """Запускает все тесты"""
    print("🧪 ЗАПУСК ТЕСТОВ КАЛЬКУЛЯТОРА")
    print("=" * 40)
    
    test_basic_operations()
    test_advanced_operations() 
    test_error_cases()
    test_history()
    
    print("=" * 40)
    print("✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ!")

def test_basic_operations():
    """Тестирует базовые операции"""
    print("\n📊 ТЕСТИРУЕМ БАЗОВЫЕ ОПЕРАЦИИ:")
    
    # Тест сложения
    result = operations.add(5, 3)
    print(f"5 + 3 = {result}")
    history.add_to_history('+', 5, 3, result)
    
    # Тест вычитания  
    result = operations.subtract(10, 4)
    print(f"10 - 4 = {result}")
    history.add_to_history('-', 10, 4, result)

def test_advanced_operations():
    """Тестирует продвинутые операции"""
    print("\n📈 ТЕСТИРУЕМ ПРОДВИНУТЫЕ ОПЕРАЦИИ:")
    
    # Тест умножения
    result = operations.multiply(3, 7)
    print(f"3 * 7 = {result}")
    history.add_to_history('*', 3, 7, result)
    
    # Тест деления
    result = operations.divide(15, 3)
    print(f"15 / 3 = {result}")
    history.add_to_history('/', 15, 3, result)
    
    # Тест степени
    result = operations.power(2, 3)
    print(f"2  3 = {result}")
    history.add_to_history('', 2, 3, result)

def test_error_cases():
    """Тестирует обработку ошибок"""
    print("\n⚠️ ТЕСТИРУЕМ ОБРАБОТКУ ОШИБОК:")
    
    # Тест деления на ноль
    try:
        result = operations.divide(10, 0)
        print(f"10 / 0 = {result}")
        history.add_to_history('/', 10, 0, result)
    except Exception as e:
        print(f"Ошибка при делении на ноль: {e}")

def test_history():
    """Тестирует модуль истории"""
    print("\n📝 ТЕСТИРУЕМ ИСТОРИЮ ОПЕРАЦИЙ:")
    history.show_history()
    print(f"Всего операций в истории: {history.get_history_count()}")

# Запуск тестов при непосредственном выполнении файла
if name == "main":
    run_tests()