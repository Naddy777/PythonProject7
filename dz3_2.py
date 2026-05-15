from datetime import date


def calculate_age(birth_date: date, current_date: date = None) -> int:
    """
    Вычисляет возраст человека на основе даты рождения.

    Args:
        birth_date: Дата рождения
        current_date: Дата, на которую вычисляется возраст (по умолчанию - сегодня)

    Returns:
        Возраст в годах

    Raises:
        ValueError: Если дата рождения позже текущей даты
    """
    if current_date is None:
        current_date = date.today()

    # Проверка, что дата рождения не в будущем
    if birth_date > current_date:
        raise ValueError("Дата рождения не может быть в будущем")

    # Вычисляем возраст
    age = current_date.year - birth_date.year

    # Проверяем, был ли уже день рождения в текущем году
    # Если нет, то вычитаем 1 год
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age