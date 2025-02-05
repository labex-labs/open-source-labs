# 简介

类可以定义特殊方法。这些方法对 Python 解释器具有特殊意义。它们总是以 `__` 开头和结尾。例如 `__init__`。

```python
class Stock(object):
    def __init__(self):
     ...
    def __repr__(self):
     ...
```

有几十种特殊方法，但我们只看几个具体的例子。
