# Supporting Iteration

Knowing about iteration is useful if you want to add it to your own objects.
For example, making a custom container.

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
