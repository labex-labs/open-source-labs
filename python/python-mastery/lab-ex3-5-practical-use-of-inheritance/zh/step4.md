# 创建额外的格式化器

在编程中，继承是一个强大的概念，它允许我们基于现有的类创建新的类。这有助于代码复用，并使我们的程序更具可扩展性。在这个实验的这一部分，我们将使用继承来为不同的输出格式创建两个新的格式化器：CSV 和 HTML。这些格式化器将继承自一个基类，这意味着它们将共享一些通用的行为，同时拥有各自独特的数据格式化方式。

现在，让我们在 `tableformat.py` 文件中添加以下类。这些类将分别定义如何以 CSV 和 HTML 格式格式化数据。

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

`CSVTableFormatter` 类旨在以 CSV（逗号分隔值）格式格式化数据。`headings` 方法接受一个表头列表，并以逗号分隔的形式打印它们。`row` 方法接受一行数据列表，并同样以逗号分隔的形式打印它们。

另一方面，`HTMLTableFormatter` 类用于生成 HTML 表格代码。`headings` 方法使用 HTML `<th>` 标签创建表格表头，`row` 方法使用 HTML `<td>` 标签创建表格行。

让我们测试这些新的格式化器，看看它们是如何工作的。

1. 首先，让我们测试 CSV 格式化器：

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

在这段代码中，我们首先导入必要的模块。然后，我们从名为 `portfolio.csv` 的 CSV 文件中读取数据，并创建 `Stock` 类的实例。接下来，我们创建 `CSVTableFormatter` 类的一个实例。最后，我们使用 `print_table` 函数以 CSV 格式打印投资组合数据。

你应该会看到以下 CSV 格式的输出：

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. 现在让我们测试 HTML 格式化器：

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

在这里，我们创建 `HTMLTableFormatter` 类的一个实例，并再次使用 `print_table` 函数以 HTML 格式打印投资组合数据。

你应该会看到以下 HTML 格式的输出：

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

如你所见，每个格式化器都以不同的格式生成输出，但它们都共享由 `TableFormatter` 基类定义的相同接口。这是继承和多态性强大功能的一个很好的例子。我们可以编写与基类一起工作的代码，它将自动适用于任何子类。

`print_table()` 函数不需要了解所使用的具体格式化器的任何信息。它只需调用基类中定义的方法，然后根据提供的格式化器类型选择合适的实现。这使得我们的代码更加灵活，更易于维护。
