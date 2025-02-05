# 支持迭代

如果你想在自己的对象中添加迭代功能，了解迭代是很有用的。例如，创建一个自定义容器。

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
