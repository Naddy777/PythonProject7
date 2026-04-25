
def validate_password(password: str) -> dict [str, bool]:
    if not isinstance(password, str):
        raise TypeError(f"Ожидался тип str, получен {type(password).__name__}")
    if len(password) == 0:
        raise ValueError("Пароль не может быть пустой строкой")

    length_check = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    case_check = has_upper and has_lower
    digits_check = any(c.isdigit() for c in password)
    special_chars = set('!@#$%^&*()-_+=')
    special_check = any(c in special_chars for c in password)
    is_strong = length_check and case_check and digits_check and special_check

    return {
        'length': length_check,
        'case': case_check,
        'digits': digits_check,
        'special': special_check,
        'is_strong': is_strong
    }


if __name__ == "__main__":
    print(validate_password("Short1!"))
    print(validate_password("longpassword"))
    print(validate_password(""))
    print(validate_password("LongPassword1"))
    print(validate_password("LongPass1#"))


