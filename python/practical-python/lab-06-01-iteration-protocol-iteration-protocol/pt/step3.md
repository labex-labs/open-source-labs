# Suportando Iteração (Supporting Iteration)

Conhecer a iteração é útil se você deseja adicioná-la aos seus próprios objetos. Por exemplo, criando um container personalizado.

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
