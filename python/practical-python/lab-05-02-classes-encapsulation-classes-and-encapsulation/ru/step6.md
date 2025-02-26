# Управляемые атрибуты

Одним подходом является введение методов доступа.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Функция, которая слоирует операцию "получения"
    def get_shares(self):
        return self._shares

    # Функция, которая слоирует операцию "установки"
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
```

К сожалению, это сломает весь наш существующий код. `s.shares = 50` становится `s.set_shares(50)`
