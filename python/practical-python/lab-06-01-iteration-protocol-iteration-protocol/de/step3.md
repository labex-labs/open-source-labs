# Iteration unterstützen

Wenn Sie die Iteration zu Ihren eigenen Objekten hinzufügen möchten, ist es hilfreich, sich mit ihr vertraut zu machen. Beispielsweise bei der Erstellung eines benutzerdefinierten Containers.

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
