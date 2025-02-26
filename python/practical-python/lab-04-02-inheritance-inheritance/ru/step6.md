# Переопределение

Иногда класс расширяет существующий метод, но хочет использовать исходную реализацию внутри переопределения. Для этого используйте `super()`:

```python
class Stock:
 ...
    def cost(self):
        return self.shares * self.price
 ...

class MyStock(Stock):
    def cost(self):
        # Проверьте вызов `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

Используйте `super()` для вызова предыдущей версии.

_Внимание: В Python 2 синтаксис был более подробным._

```python
actual_cost = super(MyStock, self).cost()
```
