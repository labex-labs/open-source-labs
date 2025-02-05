# 控制导出符号

修改 `structly` 包中的所有子模块，以便它们显式定义一个 `__all__` 变量，该变量用于导出选定的符号。具体来说：

- `structure.py` 应导出 `Structure`
- `reader.py` 应导出所有各种 `read_csv_as_*()` 函数
- `tableformat.py` 导出 `create_formatter()` 和 `print_table()`

现在，在 `__init__.py` 文件中，像这样统一所有子模块：

```python
# structly/__init__.py

from.structure import *
from.reader import *
from.tableformat import *
```

完成此操作后，你应该能够从单个逻辑模块导入所有内容：

```python
# stock.py

from structly import Structure

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
    from structly import read_csv_as_instances, create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
