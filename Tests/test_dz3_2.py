import pytest
from datetime import date
import dz3_2
from dz3_2 import calculate_age

# Фиксированная дата "сегодня" для тестов
TODAY = date(2020, 4, 29)

@pytest.fixture
def mock_today(monkeypatch):
    """Фикстура, которая фиксирует дату на 1 января 2026 года"""

    class MockDate(date):
        @classmethod
        def today(cls):
            return TODAY

    monkeypatch.setattr(dz3_2,"date", MockDate)
    return MockDate


def test_calculate_age_default_today(mock_today):
    """Проверка вызова с одним аргументом: сегодня — день рождения."""

    birth_date = TODAY.replace(year=TODAY.year - 25)
    # Вызываем БЕЗ второго аргумента
    assert calculate_age(birth_date) == 25

def test_calculate_age_default_tomorrow(mock_today):
    """Проверка вызова с одним аргументом: завтра — день рождения."""

    birth_date = TODAY.replace(year=TODAY.year - 25, day=TODAY.day + 1)
    # Вызываем БЕЗ второго аргумента
    assert calculate_age(birth_date) == 24

def test_calculate_age_default_not_reached(mock_today):
    """Проверка вызова с одним аргументом: день рождения еще не наступил."""

    birth_date = TODAY.replace(year=TODAY.year + 1)
    with pytest.raises(ValueError):
        calculate_age(birth_date)

def test_calculate_age_newborn_no_mock():
    """Проверка для новорожденного, рожденного прямо сейчас."""
    result = calculate_age(date.today())
    assert result == 0
#
# # --- ТЕСТЫ С ЯВНОЙ ПЕРЕДАЧЕЙ ДАТЫ (Граничные случаи) ---
@pytest.mark.parametrize("birth, current, expected", [
    (date(2020, 2, 29), date(2024, 2, 29), 4),  # Високосный день -> Високосный день
    (date(2020, 2, 29), date(2021, 2, 28), 0),  # Високосный день -> Обычный (еще не наступил)
    (date(2020, 2, 29), date(2021, 3, 1), 1),   # Високосный день -> Обычный (прошел)
])
def test_calculate_age_leap_years(birth, current, expected):
    assert calculate_age(birth, current) == expected