# Atributo `__slots__`

Você pode restringir o conjunto de nomes de atributos.

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
        ...
```

Isso levantará um erro para outros atributos.

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AttributeError: 'Stock' object has no attribute 'prices'
```

Embora isso evite erros e restrinja o uso de objetos, ele é realmente usado para desempenho e faz com que o Python use a memória de forma mais eficiente.
