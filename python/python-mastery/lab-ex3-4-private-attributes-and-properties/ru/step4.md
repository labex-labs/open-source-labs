# Использование `__slots__` для оптимизации памяти (Memory Optimization)

Атрибут `__slots__` ограничивает атрибуты, которые может иметь класс. Он предотвращает добавление новых атрибутов к экземплярам и снижает использование памяти.

В нашем классе `Stock` мы будем использовать `__slots__`, чтобы:

1.  Ограничить создание атрибутов только атрибутами, которые мы определили.
2.  Повысить эффективность использования памяти, особенно при создании большого количества экземпляров.

**Инструкции:**

1.  Откройте файл `stock.py` в редакторе.
2.  Добавьте переменную класса `__slots__`, перечислив все имена приватных атрибутов, используемых классом:

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  Сохраните файл.

4.  Создайте тестовый скрипт с именем `test_slots.py`:

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  Добавьте следующий код в файл `test_slots.py`:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  Запустите тестовый скрипт:

    ```bash
    python /home/labex/project/test_slots.py
    ```

    Вы должны увидеть вывод, показывающий, что вы можете получить доступ к определенным атрибутам, но попытка добавить новый атрибут вызывает `AttributeError`.

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```
