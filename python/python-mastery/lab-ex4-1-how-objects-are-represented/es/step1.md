# Preparación

Comience esta práctica volviendo a una versión simple de la clase `Stock` que creó. En el prompt interactivo, defina una nueva clase llamada `SimpleStock` que se vea así:

```python
>>> class SimpleStock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def cost(self):
            return self.shares * self.price

>>>
```

Una vez que haya definido esta clase, cree algunas instancias.

```python
>>> goog = SimpleStock('GOOG',100,490.10)
>>> ibm  = SimpleStock('IBM',50, 91.23)
>>>
```
