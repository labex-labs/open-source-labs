# Atributos simples

Considera la siguiente clase.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Una característica sorprendente es que puedes establecer los atributos en cualquier valor:

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

Podrías ver eso y pensar que quieres algunas comprobaciones adicionales.

```python
s.shares = '50'     # Genera un TypeError, esto es una cadena
```

¿Cómo lo harías?
