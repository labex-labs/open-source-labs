# 创建一个包

在之前的实验中，你创建了以下与类型检查结构、读取数据和生成表格相关的文件：

- `structure.py`
- `validate.py`
- `reader.py`
- `tableformat.py`

你的任务是将所有这些文件移动到一个名为 `structly` 的包中。为此，请按照以下步骤操作：

- 创建一个名为 `structly` 的目录
- 创建一个空文件 `__init__.py` 并将其放入 `structly` 目录中
- 将文件 `structure.py`、`validate.py`、`reader.py` 和 `tableformat.py` 移动到 `structly` 目录中
- 修复模块之间的任何导入语句（具体来说，`structure` 模块依赖于 `validate`）。

完成上述操作后，修改 `stock.py` 程序，使其看起来完全如下并能正常运行：

```python
# stock.py

from structly.structure import Structure

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
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
