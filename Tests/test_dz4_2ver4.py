import pytest
from dz4_2ver4 import Money


# --- Блок 1: Тесты конструктора ---

def test_constructor_normal():
    """Тест конструктора с обычными положительными значениями."""
    money = Money(10, 50)
    assert money.rub == 10
    assert money.kop == 50


def test_constructor_overflow_kop():
    """Тест конструктора, когда копеек больше 99 (должны перейти в рубли)."""
    money = Money(10, 150)
    assert money.rub == 11
    assert money.kop == 50


def test_constructor_with_negative_rubles():
    """Тест конструктора с отрицательными рублями (долг)."""
    money = Money(-10, 50)
    # Ожидает -9, а не -10! Ожидает 50, а не -50!
    assert money.rub == -9
    assert money.kop == 50


def test_constructor_with_negative_and_overflow():
    """Тест отрицательных рублей с избыточными копейками."""
    money = Money(-5, 150)
    # -5 руб 150 коп = -3 руб 50 коп (логика из теста)
    assert money.rub == -3
    assert money.kop == 50


def test_constructor_negative_without_kopecks():
    """Тест отрицательных рублей без копеек."""
    money = Money(-10, 0)
    assert money.rub == -10
    assert money.kop == 0
    # Проверка строкового представления (важный нюанс из теста)
    assert str(money) == "-10руб 0коп"


# --- Блок 2: Тесты арифметических операций ---

def test_addition_positive():
    """Тест сложения двух положительных сумм."""
    m1 = Money(20, 60)
    m2 = Money(10, 45)
    result = m1 + m2
    assert result.rub == 31
    assert result.kop == 5
    assert str(result) == "31руб 5коп"


def test_addition_with_negative():
    """Тест сложения с отрицательной суммой (долг)."""
    m1 = Money(-10, 50)  # Это -9руб 50коп после нормализации
    m2 = Money(5, 75)  # Это 6руб 75коп после нормализации? Нет, это 5руб 75коп.
    # Итого: -9.50 + 5.75 = -3.75
    result = m1 + m2
    assert str(result) == "-3руб 75коп"


def test_subtraction_positive_result():
    """Тест вычитания с положительным результатом."""
    m1 = Money(30, 75)
    m2 = Money(10, 20)
    result = m1 - m2
    assert str(result) == "20руб 55коп"


def test_subtraction_negative_result():
    """Тест вычитания с отрицательным результатом (долг)."""
    m1 = Money(10, 30)
    m2 = Money(20, 60)
    result = m1 - m2
    # Ожидаемый результат: Долг в размере 10 рублей 30 копеек.
    assert str(result) == "-10руб 30коп"


def test_multiplication_by_int():
    """Тест умножения суммы на целое число."""
    money_sum = Money(15, 50)

    # Умножаем сумму на 3
    result_1 = money_sum * 3
    assert str(result_1) == "46руб 50коп"

    # Умножаем число на сумму (обратный порядок)
    result_2 = 2 * money_sum
    assert str(result_2) == "31руб 0коп"


# Проверка умножения на ноль и отрицательное число
def test_multiplication_edge_cases():
    money_sum = Money(10, 50)

    # На ноль
    result_zero = money_sum * 0
    assert str(result_zero) == "0руб 0коп"

    # На отрицательное число (меняет знак всей суммы)
    result_neg = money_sum * -2
    assert str(result_neg) == "-21руб 0коп"


# --- Блок 3: Тесты сравнения ---

def test_comparison_equal():
    """Тест равенства сумм."""
    m1 = Money(20, 50)
    m2 = Money(20, 50)

    assert m1 == m2
    assert not (m1 != m2)


def test_comparison_not_equal():
    """Тест неравенства сумм."""
    m1 = Money(20, 50)
    m3 = Money(15, 30)

    assert m1 != m3


def test_comparison_greater_less():
    """Тест операций больше/меньше."""
    m1 = Money(20, 50)
    m3 = Money(15, 30)

    assert m3 < m1
    assert m1 > m3


# Сложное сравнение: долг (-) меньше положительного числа (+)
def test_comparison_debt_vs_positive():
    debt = Money(-1, 0)  # Долг 1 рубль
    positive = Money(1, 0)  # Положительная сумма

    assert debt < positive

# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__, "-v"])