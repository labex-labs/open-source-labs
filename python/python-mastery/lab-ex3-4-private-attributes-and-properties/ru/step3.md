# Реализация валидации свойств (Property Validation)

Свойства (properties) также позволяют вам контролировать, как значения атрибутов извлекаются, устанавливаются и удаляются. Это полезно для добавления валидации (validation) к вашим атрибутам, гарантируя, что значения соответствуют определенным критериям.

В нашем классе `Stock` мы хотим убедиться, что `shares` является неотрицательным целым числом, а `price` - неотрицательным числом с плавающей точкой. Мы будем использовать декораторы свойств (property decorators) вместе с геттерами (getters) и сеттерами (setters) для достижения этой цели.

**Инструкции:**

1.  Откройте файл `stock.py` в редакторе.

2.  Добавьте приватные атрибуты `_shares` и `_price` в класс `Stock` и измените конструктор, чтобы использовать их:

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  Определите свойства (properties) для `shares` и `price` с валидацией (validation):

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

4.  Обновите конструктор, чтобы использовать сеттеры свойств (property setters) для валидации (validation):

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  Сохраните файл `stock.py`.

6.  Создайте тестовый скрипт с именем `test_validation.py`:

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  Добавьте следующий код в файл `test_validation.py`:

    ```python
    from stock import Stock

    # Create a valid stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

    # Test valid updates
    try:
        s.shares = 50  # Valid update
        print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting shares=50: {e}")

    try:
        s.price = 123.45  # Valid update
        print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting price=123.45: {e}")

    # Test invalid updates
    try:
        s.shares = "50"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares='50': {e}")

    try:
        s.shares = -10  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares=-10: {e}")

    try:
        s.price = "123.45"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price='123.45': {e}")

    try:
        s.price = -10.0  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price=-10.0: {e}")
    ```

8.  Запустите тестовый скрипт:

    ```bash
    python /home/labex/project/test_validation.py
    ```

    Вы должны увидеть вывод, показывающий успешные допустимые обновления и соответствующие сообщения об ошибках для недопустимых обновлений.

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```
