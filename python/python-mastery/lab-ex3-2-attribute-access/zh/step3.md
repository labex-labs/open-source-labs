# 使用属性访问创建表格格式化器

在编程中，属性访问是一个基本概念，它允许我们与对象的属性进行交互。现在，我们将把所学的属性访问知识付诸实践。我们将创建一个实用工具：表格格式化器。这个格式化器会接收一组对象，并以表格形式显示它们，使数据更易于阅读和理解。

## 创建 `tableformat.py` 模块

首先，我们需要创建一个新的 Python 文件。这个文件将包含我们表格格式化器的代码。

要创建该文件，请按照以下步骤操作：

1. 在 WebIDE 中，点击“文件”菜单。
2. 从下拉菜单中选择“新建文件”。
3. 将新创建的文件保存为 `/home/labex/project/tableformat.py`。

现在我们有了文件，让我们在 `tableformat.py` 中编写 `print_table()` 函数的代码。这个函数将负责以表格形式格式化并打印我们的对象。

```python
def print_table(objects, fields):
    """
    Print a collection of objects as a formatted table.

    Args:
        objects: A sequence of objects
        fields: A list of attribute names
    """
    # Print the header
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Print the separator line
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Print the data
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

让我们来详细分析这个函数的功能：

1. 它接受两个参数：一个对象序列和一个属性名列表。对象序列是我们要显示的数据，属性名列表告诉函数要显示对象的哪些属性。
2. 它打印表头行。表头行包含我们感兴趣的属性名称。
3. 它打印分隔线。这条线有助于在视觉上分隔表头和数据。
4. 对于序列中的每个对象，它打印每个指定属性的值。它使用 `getattr()` 函数来访问每个对象的属性值。

现在，让我们测试一下 `print_table()` 函数，看看它是否按预期工作。

```python
# Open a Python interactive shell
python3

# Import our modules
from stock import read_portfolio
import tableformat

# Read the portfolio data
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a table with name, shares, and price columns
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

当你运行上述代码时，你应该会看到以下输出：

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

我们的 `print_table()` 函数的一大优点是它的灵活性。我们只需更改 `fields` 列表，就可以更改显示的列。

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

运行这段代码将得到以下输出：

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

这种方法的强大之处在于它的通用性。只要我们知道要显示的属性名称，就可以使用同一个 `print_table()` 函数为任何类型的对象打印表格。这使得我们的表格格式化器成为编程工具包中非常实用的工具。
