# Использование ваших проверяющих классов

Ваши проверяющие классы можно использовать для добавления проверки значений в функции и классы. Например, возможно, проверяющие классы можно использовать в свойствах класса `Stock`:

```python
class Stock:
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)
  ...
```

Скопируйте класс `Stock` из `stock.py` и измените его так, чтобы он использовал проверяющие классы в коде свойств для `shares` и `price`.
