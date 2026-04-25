def calculate_annuity_payment(amount: int | float, annual_rate: float, months: int) -> float:
    if not isinstance(amount, (int, float)):
        raise TypeError("Параметр 'amount' должен быть числом (int или float)")

    if not isinstance(annual_rate, (int, float)):
        raise TypeError("Параметр 'annual_rate' должен быть числом (int или float)")

    if not isinstance(months, int):
        raise TypeError("Параметр 'months' должен быть целым числом (int)")

    if amount < 0:
        raise ValueError("Сумма кредита ('amount') не может быть отрицательной")

    if annual_rate < 0:
        raise ValueError("Годовая процентная ставка ('annual_rate') не может быть отрицательной")

    if months <= 0:
        raise ValueError("Срок кредита ('months') должен быть положительным числом")

    monthly_rate = annual_rate / 100 / 12
    if monthly_rate == 0:
        return round(amount / months, 2)

    payment = amount *((monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1))
    return round(payment, 2)

if __name__ == "__main__":
    amount = 5566655
    annual_rate = 15.5
    months = 9
    payment = calculate_annuity_payment(amount, annual_rate, months)

    print(f"Сумма кредита: {amount} руб.")
    print(f"Годовая процентная ставка: {annual_rate}%")
    print(f"Срок кредита: {months} месяцев")
    print(f"Ежемесячный аннуитетный платёж: {payment} руб.")