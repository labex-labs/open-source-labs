# Introdução

Classes podem definir métodos especiais. Estes têm um significado especial para o interpretador Python. Eles são sempre precedidos e seguidos por `__`. Por exemplo, `__init__`.

```python
class Stock(object):
    def __init__(self):
        ...
    def __repr__(self):
        ...
```

Existem dezenas de métodos especiais, mas analisaremos apenas alguns exemplos específicos.
