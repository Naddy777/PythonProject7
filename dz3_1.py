def convert_currency(amount: float, rate: float, precision: int = 2) -> float:
    if amount < 0 or rate <= 0:
        raise ValueError("Amount and rate must be positive numbers.")
    if precision < 0:
        raise ValueError("Precision cannot be negative.")

    result = amount * rate
    return round(result, precision)