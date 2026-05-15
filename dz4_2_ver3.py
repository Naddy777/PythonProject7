class Money:
    def __init__(self, rub, kop):
        # Переводим всё в копейки и нормализуем
        total_kop = rub * 100 + kop

        # Используем divmod для корректной работы с отрицательными числами
        # Но divmod с отрицательными работает не так, как нужно для денег
        # Поэтому лучше использовать математический подход:
        self.rub = total_kop // 100
        self.kop = total_kop % 100

        # Корректируем для отрицательных копеек
        if self.kop < 0:
            self.rub -= 1
            self.kop += 100

    def _to_kopecks(self):
        return self.rub * 100 + self.kop

    @classmethod
    def _from_kopecks(cls, kopecks):
        rub = kopecks // 100
        kop = kopecks % 100
        # Та же корректировка для отрицательных
        if kop < 0:
            rub -= 1
            kop += 100
        return cls(rub, kop)

    def __add__(self, other):
        if isinstance(other, Money):
            return Money._from_kopecks(self._to_kopecks() + other._to_kopecks())
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money._from_kopecks(self._to_kopecks() - other._to_kopecks())
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Money._from_kopecks(self._to_kopecks() * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() == other._to_kopecks()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() != other._to_kopecks()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() < other._to_kopecks()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() <= other._to_kopecks()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() > other._to_kopecks()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() >= other._to_kopecks()
        return NotImplemented

    def __str__(self):
        return f"{self.rub}руб {self.kop}коп"

    def __repr__(self):
        return f"Money({self.rub}, {self.kop})"

if __name__ == "__main__":
    print("=== Пример 1: Создание суммы с лишними копейками ===")
    # Создаем сумму из 20 рублей и 120 копеек
    money_sum1 = Money(20, 120)
    # Выводим сумму, с учетом кол-ва копеек
    print(money_sum1)  # 21руб 20коп
    print()

    print("=== Пример 2: Сложение денежных сумм ===")
    # Создаем две денежные суммы
    money_sum1 = Money(20, 60)
    money_sum2 = Money(10, 45)

    # Складываем суммы
    money_result = money_sum1 + money_sum2
    print(money_result)  # 31руб 5коп
    print()

    print("=== Пример 3: Вычитание денежных сумм ===")
    money_sum1 = Money(30, 75)
    money_sum2 = Money(10, 20)

    money_result = money_sum1 - money_sum2
    print(money_result)  # 20руб 55коп
    print()

    print("=== Пример 4: Вычитание с отрицательным результатом (долг) ===")
    money_sum1 = Money(10, 30)
    money_sum2 = Money(20, 60)

    money_result = money_sum1 - money_sum2
    print(money_result)  # -10руб 30коп
    print()

    print("=== Пример 5: Умножение денежной суммы на целое число ===")
    money_sum = Money(15, 50)

    # Умножаем на 3
    money_result = money_sum * 3
    print(money_result)  # 46руб 50коп

    # Или наоборот
    money_result = 2 * money_sum
    print(money_result)  # 31руб 0коп
    print()

    print("=== Пример 6: Сравнение денежных сумм ===")
    money_sum1 = Money(20, 50)
    money_sum2 = Money(20, 50)
    money_sum3 = Money(15, 30)
    money_sum4 = Money(25, 75)

    print(money_sum1 == money_sum2)  # True
    print(money_sum1 != money_sum3)  # True
    print(money_sum3 < money_sum1)  # True
    print(money_sum1 > money_sum3)  # True
    print(money_sum1 <= money_sum2)  # True
    print(money_sum4 >= money_sum1)  # True
    print()

    print("=== Дополнительные тесты ===")
    # Тест на корректное округление копеек
    m1 = Money(0, 150)
    print(f"0 руб 150 коп = {m1}")  # 1руб 50коп

    # Тест на сложение с отрицательными числами
    m2 = Money(-5, 50)
    m3 = Money(3, 75)
    print(f"{m2} + {m3} = {m2 + m3}")  # -1руб 75коп

    # Тест на умножение на ноль
    m4 = Money(10, 30)
    print(f"{m4} * 0 = {m4 * 0}")  # 0руб 0коп

    # Тест на все операции сравнения
    print(f"{m2} < {m3}: {m2 < m3}")  # True
    print(f"{m2} > {m3}: {m2 > m3}")  # False
