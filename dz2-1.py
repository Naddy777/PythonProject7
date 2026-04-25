def rle_encode(data: str) -> str:
    if not isinstance(data, str):
        raise TypeError(f"Ожидался тип 'str', но получен тип '{type(data).__name__}'")

    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1

    result.append(f"{count}{current_char}")
    return "".join(result)


if __name__ == "__main__":
    test_string = 12365
    result = rle_encode(test_string)
    print(f"Исходная строка: {test_string}")
    print(f"Закодированная строка: {result}")
