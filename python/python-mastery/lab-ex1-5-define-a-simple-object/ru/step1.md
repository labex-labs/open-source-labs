# Определение простого объекта

Создайте файл `stock.py` и определите следующий класс:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
```

После этого запустите свою программу и проведите эксперименты с новым объектом `Stock`:

Примечание: Для этого вам может потребоваться запустить python с использованием параметра `-i`. Например:

```bash
python3 -i stock.py
```

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>> print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
      GOOG        100     490.10
>>> t = Stock('IBM', 50, 91.5)
>>> t.cost()
4575.0
>>>
```
