# Начало сначала

Создайте новый файл `stock.py` (или удалите весь предыдущий код). Начните сначала, определив `Stock` следующим образом:

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

После этого запустите свои юнит-тесты из `teststock.py`. Вы, вероятно, получите много ошибок, но по крайней мере несколько тестов должны пройти.
