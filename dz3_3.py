def format_file_size(size_bytes: int) -> str:

    if not isinstance(size_bytes, int):
        raise TypeError(f"Expected int, got {type(size_bytes).__name__}")

    if size_bytes < 0:
        raise ValueError(f"Size cannot be negative: {size_bytes}")

    units = ["B", "KB", "MB", "GB", "TB"]
    threshold = 1024.0

    if size_bytes == 0:
        return "0.0 B"

    size = float(size_bytes)
    unit_index = 0

    while size >= threshold and unit_index < len(units) - 1:
        size /= threshold
        unit_index += 1

    rounded_size = round(size, 1)

    if rounded_size >= threshold and unit_index < len(units) - 1:
        rounded_size = round(rounded_size / threshold, 1)
        unit_index += 1

    return f"{rounded_size:.1f} {units[unit_index]}"


def format_file_size1(size_bytes: int) -> str:
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

    # Определение единиц измерения
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)

    # Выбор подходящей единицы измерения
    for unit in units:
        if size < 1024.0 or unit == units[-1]:
            # Округление до одного знака после запятой
            rounded_size = round(size, 1)
            return f"{rounded_size:.1f} {unit}"
        size /= 1024.0

    # Эта строка никогда не должна выполниться, но на всякий случай
    return f"{round(size, 1):.1f} {units[-1]}"