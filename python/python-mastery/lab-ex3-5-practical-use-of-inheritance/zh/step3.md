# 实现具体的格式化器

现在我们已经定义了抽象基类并更新了 `print_table()` 函数，接下来是时候创建一个具体的格式化器类了。具体的格式化器类会为抽象基类中定义的方法提供实际的实现。在我们的例子中，我们将创建一个可以将数据格式化为纯文本表格的类。

让我们在 `tableformat.py` 文件中添加以下类。这个类将继承自 `TableFormatter` 抽象基类，并实现 `headings()` 和 `row()` 方法。

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

`TextTableFormatter` 类继承自 `TableFormatter`。这意味着它继承了 `TableFormatter` 类的所有属性和方法，但同时也为 `headings()` 和 `row()` 方法提供了自己的实现。这些方法分别负责格式化表格的表头和行。`headings()` 方法以良好的格式打印表头，随后打印一行短横线，用于将表头与数据分隔开。`row()` 方法以类似的方式格式化每一行数据。

现在，让我们测试一下新的格式化器。我们将使用 `stock`、`reader` 和 `tableformat` 模块从 CSV 文件中读取数据，并使用新的格式化器打印数据。

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

当你运行这段代码时，你应该会看到与之前相同的输出。这是因为我们的新格式化器被设计为生成与原始 `print_table()` 函数相同的纯文本表格。

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

这个输出证实了我们的 `TextTableFormatter` 工作正常。使用这种方法的优势在于，我们使代码更具模块化和可扩展性。通过将格式化逻辑分离到一个独立的类层次结构中，我们可以轻松添加新的输出格式。我们只需创建 `TableFormatter` 的新子类，而无需修改 `print_table()` 函数。这样，我们将来就可以支持不同的输出格式，如 CSV 或 HTML。
