class Money:
    def __init__(self, rub, kop):
        # 1. Приводим всё к копейкам, чтобы работать с одним числом
        # Это гарантирует корректную работу с отрицательными значениями
        total_kop = rub * 100 + kop

        # 2. Сохраняем знак всей суммы (отрицательная сумма = долг)
        self.is_negative = total_kop < 0

        # 3. Работаем с абсолютным значением для вычисления рублей и копеек
        abs_total = abs(total_kop)
        self.rub = abs_total // 100
        self.kop = abs_total % 100

    def __add__(self, other):
        # При сложении/вычитании переводим всё в копейки, считаем, и создаем новый объект
        total_kop_self = (-1 if self.is_negative else 1) * (self.rub * 100 + self.kop)
        total_kop_other = (-1 if other.is_negative else 1) * (other.rub * 100 + other.kop)
        return Money(0, total_kop_self + total_kop_other)

    def __sub__(self, other):
        # Вычитание — это сложение с отрицательным числом
        total_kop_self = (-1 if self.is_negative else 1) * (self.rub * 100 + self.kop)
        total_kop_other = (-1 if other.is_negative else 1) * (other.rub * 100 + other.kop)
        return Money(0, total_kop_self - total_kop_other)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        # 1. Определяем исходный знак суммы
        current_sign = -1 if self.is_negative else 1

        # 2. Определяем знак множителя
        multiplier_sign = -1 if other < 0 else 1

        # 3. Итоговый знак = произведение исходного знака и знака множителя
        final_sign = current_sign * multiplier_sign

        # 4. Работаем с абсолютным значением суммы в копейках
        abs_total_kop = self.rub * 100 + self.kop

        # 5. Умножаем и применяем итоговый знак
        total_kop = abs_total_kop * abs(other) * final_sign

        return Money(0, total_kop)

    def __rmul__(self, other):
        return self.__mul__(other)

    # Методы сравнения (сравниваем абсолютные значения с учетом знака)
    def __eq__(self, other):
        return (self.rub == other.rub and
                self.kop == other.kop and
                self.is_negative == other.is_negative)

    def __lt__(self, other):
        self_val = - (self.rub * 100 + self.kop) if self.is_negative else (self.rub * 100 + self.kop)
        other_val = - (other.rub * 100 + other.kop) if other.is_negative else (other.rub * 100 + other.kop)
        return self_val < other_val


    # но для простоты тестов достаточно этих двух.
    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return other.__lt__(self)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __str__(self):
        sign = '-' if self.is_negative else ''
        # Если копейки равны 0, выводим просто "0коп", иначе — с ведущим нулём
        kop_str = str(self.kop) if self.kop != 0 else '0'
        return f"{sign}{abs(self.rub)}руб {kop_str}коп"

if __name__ == "__main__":
     # Создаем сумму из 20 рублей и 120 копеек
    money_sum1 = Money(20, 120)
    print(money_sum1)  # 21руб 20коп

    # Сложение
    money_sum1 = Money(20, 60)
    money_sum2 = Money(10, 45)
    money_result = money_sum1 + money_sum2
    print(money_result)  # 31руб 5коп

    # Вычитание
    money_sum1 = Money(30, 75)
    money_sum2 = Money(10, 20)
    money_result = money_sum1 - money_sum2
    print(money_result)  # 20руб 55коп

    # Отрицательный результат (долг)
    money_sum1 = Money(10, 30)
    money_sum2 = Money(20, 60)
    money_result = money_sum1 - money_sum2
    print(money_result)  # -10руб 30коп

    # Умножение
    money_sum = Money(15, 50)
    money_result = money_sum * 3
    print(money_result)  # 46руб 50коп

    money_sum = Money(10, 50)
    money_result = money_sum * (-3)
    print(money_result)  # -31руб 50коп

    money_sum = Money(15, 50)
    money_result = 2 * money_sum
    print(money_result)  # 31руб 0коп

    # Сравнение
    m1 = Money(20, 50)
    m2 = Money(20, 50)
    m3 = Money(15, 30)
    m4 = Money(25, 75)

    print(m1 == m2)  # True
    print(m1 != m3)  # True
    print(m3 < m1)  # True
    print(m1 > m3)  # True
    print(m1 <= m2)  # True
    print(m4 >= m1)  # True

    # Проверка отрицательных сумм
    print("Тест 1:", Money(-10, 50))  # -9руб 50коп
    print("Тест 2:", Money(-5, 150))  # -3руб 50коп
    print("Тест 3:", Money(-10, -50))  # -10руб -50коп