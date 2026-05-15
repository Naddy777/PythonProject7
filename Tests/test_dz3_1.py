from dz3_1 import convert_currency
import pytest

# 1. Тест базового позитивного сценария
def test_convert_currency_basic():
    assert convert_currency(100, 2.0) == 200.0

# 2. Тест точности округления (параметр precision)
def test_convert_currency_precision():
    # 100 * 1.555 = 155.5, округляем до 2 знаков -> 155.5
    assert convert_currency(100, 1.555, 2) == 155.5
    # 10 * 1.1111 = 11.111, округляем до 0 знаков -> 11.0
    assert convert_currency(10, 1.1111, 0) == 11.0

# 3. Граничное значение: Сумма равна нулю
def test_convert_currency_zero_amount():
    assert convert_currency(0, 75.5) == 0.0

# 4. Граничное значение: Очень маленькие числа (плавающая запятая)
def test_convert_currency_small_values():
    assert convert_currency(0.0001, 0.0001, 8) == 0.00000001

# 5. Исключение: Отрицательная сумма
def test_convert_currency_negative_amount():
    with pytest.raises(ValueError):
        convert_currency(-100, 2.0)

# 6. Исключение: Курс равен нулю
def test_convert_currency_zero_rate():
    with pytest.raises(ValueError):
        convert_currency(100, 0)

# 7. Исключение: Отрицательный курс
def test_convert_currency_negative_rate():
    with pytest.raises(ValueError):
        convert_currency(100, -1.5)

# 8. Исключение: Отрицательная точность округления
def test_convert_currency_negative_precision():
    with pytest.raises(ValueError):
        convert_currency(100, 2.0, -1)

# 9. Тест на корректность типов (передача целых чисел вместо float)
def test_convert_currency_integer_inputs():
    # Функция должна корректно работать с int
    result = convert_currency(10, 5)
    assert result == 50.0
    assert isinstance(result, int)

# 10. Параметризованный тест для проверки разных валютных пар (краткая запись нескольких тестов)
@pytest.mark.parametrize("amount, rate, expected", [
    (10, 0.5, 5.0),
    (100, 1.1, 110.0),
    (0.5, 2.0, 1.0),
])
def test_convert_currency_multiple_variants(amount, rate, expected):
    assert convert_currency(amount, rate) == expected
