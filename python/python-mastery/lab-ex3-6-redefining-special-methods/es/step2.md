# Haciendo que los objetos sean comparables

¿Qué sucede si creas dos objetos `Stock` idénticos y tratas de compararlos? Descúbrelo:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
False
>>>
```

Puedes solucionar esto dándole a la clase `Stock` un método `__eq__()`. Por ejemplo:

```python
class Stock:
  ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
  ...
```

Haz este cambio y vuelve a intentar comparar dos objetos.
