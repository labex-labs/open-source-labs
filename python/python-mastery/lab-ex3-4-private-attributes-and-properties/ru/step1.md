# Реализация приватных атрибутов

В Python мы используем соглашение об именовании, чтобы указать, что атрибут предназначен для внутреннего использования внутри класса. Мы добавляем префикс в виде символа подчеркивания (`_`) к таким атрибутам. Это сигнализирует другим разработчикам, что эти атрибуты не являются частью публичного API (public API) и не должны быть доступны напрямую извне класса.

Давайте посмотрим на текущий класс `Stock` в файле `stock.py`. У него есть переменная класса (class variable) с именем `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

Переменная класса `types` используется внутри класса для преобразования данных строки. Чтобы указать, что это деталь реализации (implementation detail), мы отметим ее как приватную.

**Инструкции:**

1.  Откройте файл `stock.py` в редакторе.

2.  Измените переменную класса `types`, добавив в начало символ подчеркивания, изменив ее на `_types`.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  Обновите метод `from_row`, чтобы он использовал переименованную переменную `_types`.

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  Сохраните файл `stock.py`.

5.  Создайте Python-скрипт с именем `test_stock.py` для проверки ваших изменений. Вы можете создать файл в редакторе, используя следующую команду:

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  Добавьте следующий код в файл `test_stock.py`. Этот код создает экземпляры класса `Stock` и выводит информацию о них.

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
    print(f"Cost: {s.cost()}")

    # Create from row
    row = ['AAPL', '50', '142.5']
    apple = Stock.from_row(row)
    print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
    print(f"Cost: {apple.cost()}")
    ```

7.  Запустите тестовый скрипт, используя следующую команду в терминале:

    ```bash
    python /home/labex/project/test_stock.py
    ```

    Вы должны увидеть вывод, похожий на:

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```
