# Переопределение существующего метода

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Пример использования.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

Новый метод заменяет старый. Другие методы остаются не затронутыми. Это просто замечательно.
