# Soporte para iteración

Es útil conocer sobre la iteración si deseas agregarla a tus propios objetos. Por ejemplo, crear un contenedor personalizado.

```python
class Portfolio:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()
  ...

port = Portfolio()
for s in port:
  ...
```
