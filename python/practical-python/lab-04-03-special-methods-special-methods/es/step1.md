# Introducción

Las clases pueden definir métodos especiales. Estos tienen un significado especial para el intérprete de Python. Siempre están precedidos y seguidos por `__`. Por ejemplo `__init__`.

```python
class Stock(object):
    def __init__(self):
     ...
    def __repr__(self):
     ...
```

Hay docenas de métodos especiales, pero solo veremos algunos ejemplos específicos.
