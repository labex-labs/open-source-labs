# Преобразование методов в свойства (Properties)

Свойства (properties) в Python позволяют вам получать доступ к вычисляемым значениям, как к атрибутам. Это устраняет необходимость в круглых скобках при вызове метода, делая ваш код чище и более последовательным.

В настоящее время в нашем классе `Stock` есть метод `cost()`, который вычисляет общую стоимость акций.

```python
def cost(self):
    return self.shares * self.price
```

Чтобы получить значение стоимости, мы должны вызвать его с круглыми скобками:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Мы можем улучшить это, преобразовав метод `cost()` в свойство (property), что позволит нам получать доступ к значению стоимости без круглых скобок:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**Инструкции:**

1.  Откройте файл `stock.py` в редакторе.

2.  Замените метод `cost()` свойством (property), используя декоратор `@property`:

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  Сохраните файл `stock.py`.

4.  Создайте новый файл с именем `test_property.py` в редакторе:

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  Добавьте следующий код в файл `test_property.py`, чтобы создать экземпляр `Stock` и получить доступ к свойству `cost`:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access cost as a property (no parentheses)
    print(f"Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")  # Using the property
    ```

6.  Запустите тестовый скрипт:

    ```bash
    python /home/labex/project/test_property.py
    ```

    Вы должны увидеть вывод, похожий на:

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
