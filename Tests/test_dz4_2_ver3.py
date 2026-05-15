import pytest
from dz4_2_ver2 import Money


class TestMoneyConstructor:
    def test_constructor_with_negative_rubles(self):
        """Тест конструктора с отрицательными рублями (долг)"""
        money = Money(-10, 50)
        assert money.rub == -9
        assert money.kop == 50
        assert str(money) == "-9руб 50коп"

    def test_constructor_with_negative_and_overflow(self):
        """Тест отрицательных рублей с избыточными копейками"""
        money = Money(-5, 150)
        # -5 руб 150 коп = -500 + 150 = -350 коп = -3 руб 50 коп
        assert money.rub == -3
        assert money.kop == 50
        assert str(money) == "-3руб 50коп"

    def test_constructor_negative_without_kopecks(self):
        """Тест отрицательных рублей без копеек"""
        money = Money(-10, 0)
        assert money.rub == -10
        assert money.kop == 0
        assert str(money) == "-10руб 0коп"

    def test_constructor_negative_with_negative_kopecks(self):
        """Тест с отрицательными рублями и копейками"""
        money = Money(-10, -50)
        assert money.rub == -10
        assert money.kop == -50
        assert str(money) == "-10руб -50коп"

    def test_addition_with_negative(self):
        """Тест сложения с отрицательными суммами"""
        m1 = Money(-10, 50)  # -9руб 50коп
        m2 = Money(5, 75)  # 5руб 75коп
        result = m1 + m2
        assert str(result) == "-3руб 75коп"

    def test_subtraction_negative_result(self):
        """Тест вычитания с отрицательным результатом"""
        m1 = Money(10, 30)  # 10руб 30коп
        m2 = Money(20, 60)  # 20руб 60коп
        result = m1 - m2
        assert str(result) == "-10руб 30коп"
        assert result.rub == -10
        assert result.kop == 30


# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__, "-v"])