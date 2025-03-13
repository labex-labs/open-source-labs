# 更新并测试 stock.py 程序

既然我们已经创建了包并修正了内部导入语句，现在是时候更新 `stock.py` 文件以使用新的包结构了。在 Python 中，包是一种将相关模块组织在一起的方式。它有助于保持代码库的条理性，使代码更易于管理和复用。

在编辑器中打开 `stock.py` 文件：

```bash
# 在文件资源管理器中点击 stock.py 或运行：
code stock.py
```

目前 `stock.py` 中的导入语句是基于旧结构的，在旧结构中所有文件都位于同一目录下。在 Python 中，当你导入一个模块时，Python 会在特定位置查找该模块。在旧结构中，由于所有文件都在同一目录下，Python 可以轻松找到这些模块。但现在，有了新的包结构，我们需要更新导入语句，告诉 Python 在 `structly` 包中何处可以找到这些模块。

将 `stock.py` 文件更新为如下内容：

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

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

主要的更改如下：

1. 将 `from structure import Structure, String, PositiveInteger, PositiveFloat` 改为 `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`。这一更改告诉 Python 在 `structly` 包中查找 `structure` 模块。
2. 将 `from reader import read_csv_as_instances` 改为 `from structly.reader import read_csv_as_instances`。同样，这一更改指示 Python 在 `structly` 包中查找 `reader` 模块。
3. 将 `from tableformat import create_formatter, print_table` 改为 `from structly.tableformat import create_formatter, print_table`。这确保 Python 在 `structly` 包中找到 `tableformat` 模块。

做出这些更改后保存文件。保存文件很重要，因为这样可以确保你所做的更改被保存下来，并且在运行程序时可以使用这些更改。

现在，让我们测试更新后的代码，确保一切正常运行：

```bash
python stock.py
```

你应该会看到以下输出：

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

如果你看到了这个输出，恭喜你！你已经成功创建了一个 Python 包，并更新了代码以使用它。这意味着你的代码现在以更模块化的方式进行了组织，便于未来的维护和扩展。
