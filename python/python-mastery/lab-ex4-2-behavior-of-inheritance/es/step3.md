# Usando tus validadores

Tus validadores se pueden usar para agregar la verificación de valores a funciones y clases. Por ejemplo, quizás los validadores se podrían usar en las propiedades de `Stock`:

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

Copia la clase `Stock` de `stock.py` y cámbiala para que use los validadores en el código de la propiedad para `shares` y `price`.
