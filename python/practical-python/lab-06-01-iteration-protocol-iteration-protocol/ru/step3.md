# Поддержка итерации

Знание о итерации полезно, если вы хотите добавить его в свои собственные объекты. Например, создать пользовательский контейнер.

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
