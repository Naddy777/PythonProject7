class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self._owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        """Возвращает текущий баланс счета"""
        return self._balance

    @property
    def owner(self) -> str:
        """Возвращает имя владельца счета"""
        return self._owner

    def deposit(self, amount: float) -> None:
        """Увеличивает баланс на указанную сумму"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Уменьшает баланс на указанную сумму"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if self._balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal")

        self._balance -= amount

    def transfer(self, target_account: 'BankAccount', amount: float) -> None:
        """Переводит указанную сумму на счет другого аккаунта"""
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        if self._balance - amount < 0:
            raise ValueError("Insufficient funds for transfer")

        # Выполняем перевод
        self._balance -= amount
        target_account._balance += amount

    def __str__(self) -> str:
        """Возвращает строковое представление счета"""
        return f"Account(owner='{self._owner}', balance={self._balance})"

if __name__ == "__main__":
    # Пример с депозитом и снятием
    try:
        acc = BankAccount("Алексей", 1000.0)
        acc.deposit(500)
        print(acc)  # Account(owner='Алексей', balance=1500.0)

        acc.withdraw(2000)
    except ValueError as e:
        print(f"Ошибка транзакции: {e}")

    # Пример с переводом денег
    try:
        # Создаем два аккаунта
        acc1 = BankAccount("Михаил", 1000.0)
        acc2 = BankAccount("Мария", 500.0)

        print(f"До перевода:")
        print(f"Михаил: {acc1.balance}")  # 1000.0
        print(f"Мария: {acc2.balance}")  # 500.0

        # Михаил переводит 300 на счет Марии
        acc1.transfer(acc2, 300)

        print(f"\nПосле перевода 300 рублей:")
        print(f"Михаил: {acc1.balance}")  # 700.0
        print(f"Мария: {acc2.balance}")  # 800.0

        # Попытка перевода больше, чем есть на счете
        acc1.transfer(acc2, 1000)
    except ValueError as e:
        print(f"Ошибка: {e}")
    # Вывод: Ошибка: Insufficient funds for transfer