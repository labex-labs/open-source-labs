# Redefiniendo un método existente

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Ejemplo de uso.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

El nuevo método reemplaza al antiguo. Los otros métodos no se ven afectados. Es genial.
