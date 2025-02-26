# Objekte vergleichbar machen

Was passiert, wenn Sie zwei identische `Stock`-Objekte erstellen und versuchen, sie zu vergleichen? Finden Sie es heraus:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
False
>>>
```

Sie können dies beheben, indem Sie der `Stock`-Klasse eine `__eq__()`-Methode geben. Beispielsweise:

```python
class Stock:
  ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
  ...
```

Machen Sie diese Änderung und versuchen Sie es erneut, zwei Objekte zu vergleichen.
