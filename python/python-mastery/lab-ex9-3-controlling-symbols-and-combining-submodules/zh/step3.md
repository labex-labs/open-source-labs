# 导出所有内容

在 `structly/__init__.py` 中，定义一个包含所有导出符号的 `__all__` 变量。完成此操作后，你应该能够进一步简化 `stock.py` 文件：

```python
# stock.py

from structly import *

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

顺便说一句，Python 社区通常不赞成使用 `from module import *` 语句 —— 尤其是当你不确定自己在做什么的时候。话虽如此，但在某些情况下这样做通常是有意义的。例如，如果一个包定义了大量常用的符号或常量，那么使用它可能会很有用。
