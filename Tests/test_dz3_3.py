from dz3_3 import format_file_size
import pytest

@pytest.mark.parametrize("size, expected", [
    # --- Граничные значения и нули ---
    (0, "0.0 B"),
    (1, "1.0 B"),
    (1023, "1023.0 B"),

    # --- Переходы между единицами (границы 1024) ---
    (1024, "1.0 KB"),
    (1025, "1.0 KB"),  # Округление вниз 1025/1024 ≈ 1.0009
    (1536, "1.5 KB"),  # Ровно полтора (1024 + 512)

    # --- Проверка MB ---
    (1048576, "1.0 MB"),  # 1024 * 1024
    (104857600, "100.0 MB"),  # 100 MB

    # --- Проверка GB ---
    (1073741824, "1.0 GB"),  # 1024**3
    (2147483648, "2.0 GB"),  # 2 * 1024**3

    # --- Проверка TB и выше ---
    (1099511627776, "1.0 TB"),  # 1024**4
    (10995116277760, "10.0 TB"),
    (2000000000000000, "1819.0 TB"),  # Проверка поведения выше лимита шкалы

    # --- Округление ---
    (1100, "1.1 KB"),  # 1100 / 1024 ≈ 1.074 -> 1.1 (при обычном округлении)
    (2000, "2.0 KB"),  # 2000 / 1024 ≈ 1.953 -> 2.0
])
def test_format_file_size_positive(size, expected):
    """Тестирование корректных входных данных и переходов единиц."""
    assert format_file_size(size) == expected


def test_format_file_size_negative():
    """Проверка генерации исключения при отрицательном значении."""
    with pytest.raises(ValueError):
        format_file_size(-1)


def test_format_file_size_large_negative():
    """Проверка генерации исключения при больших отрицательных числах."""
    with pytest.raises(ValueError):
        format_file_size(-1024)


@pytest.mark.parametrize("invalid_input", [
    "1024",  # строка вместо int
    1.5,  # float вместо int
    None  # отсутствие значения
])
def test_format_file_size_wrong_types(invalid_input):
    """
    Дополнительный тест на типы данных.
    Хотя в ТЗ указан int, в автотестах полезно проверять реакцию на TypeError.
    """
    with pytest.raises(TypeError):
        format_file_size(invalid_input)