# Redefinindo um método existente (Redefining an existing method)

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Exemplo de uso (Usage example).

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

O novo método substitui o antigo. Os outros métodos não são afetados. É tremendo.
