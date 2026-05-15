def format_file_size(size_bytes: int) -> str:
    """
    Преобразует размер из байтов в человекочитаемую строку с бинарными префиксами.

    Args:
        size_bytes: Целое неотрицательное количество байт

    Returns:
        Строка вида "{значение} {единица_измерения}"

    Raises:
        ValueError: Если size_bytes отрицательный
        TypeError: Если size_bytes не является целым числом
    """
    # Проверка типа
    if not isinstance(size_bytes, int):
        raise TypeError(f"Expected int, got {type(size_bytes).__name__}")

    # Проверка на отрицательное значение
    if size_bytes < 0:
        raise ValueError(f"Size cannot be negative: {size_bytes}")

    # Определение единиц измерения и их пороговых значений
    units = ["B", "KB", "MB", "GB", "TB"]
    threshold = 1024.0

    # Особый случай для 0 байт
    if size_bytes == 0:
        return "0.0 B"

    # Выбор подходящей единицы измерения
    size = float(size_bytes)
    unit_index = 0

    while size >= threshold and unit_index < len(units) - 1:
        size /= threshold
        unit_index += 1

    # Округление до одного знака после запятой
    # Используем стандартное округление (банковское округление для .5)
    rounded_size = round(size, 1)

    # Форматирование вывода
    # Если после округления получилось 1024.0, увеличиваем единицу измерения
    if rounded_size >= threshold and unit_index < len(units) - 1:
        rounded_size = round(rounded_size / threshold, 1)
        unit_index += 1

    # Формируем строку результата
    # Для целых чисел типа 1.0 выводим без лишних нулей? Нет, по ТЗ нужен один знак
    return f"{rounded_size:.1f} {units[unit_index]}"