# Добавить новый метод

```python
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
```

Пример использования.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.shares
75
>>> s.panic()
>>> s.shares
0
>>>
```
