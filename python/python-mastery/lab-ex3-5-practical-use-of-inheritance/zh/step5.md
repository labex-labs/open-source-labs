# 创建工厂函数

在使用继承时，一个常见的挑战是用户必须记住具体格式化器类的名称。这可能会很麻烦，尤其是当类的数量增加时。为了简化这个过程，我们可以创建一个工厂函数。工厂函数是一种特殊类型的函数，它可以创建并返回对象。在我们的例子中，它将根据一个简单的格式名称返回合适的格式化器。

让我们在 `tableformat.py` 文件中添加以下函数。这个函数将接受一个格式名称作为参数，并返回相应的格式化器对象。

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

`create_formatter()` 函数是一个工厂函数。它会检查你提供的 `format_name` 参数。如果是 'text'，它会创建并返回一个 `TextTableFormatter` 对象；如果是 'csv'，它会返回一个 `CSVTableFormatter` 对象；如果是 'html'，它会返回一个 `HTMLTableFormatter` 对象。如果格式名称未被识别，它会抛出一个 `ValueError`。这样，用户只需提供一个简单的名称就能轻松选择格式化器，而无需了解具体的类名。

现在，让我们测试这个工厂函数。我们将使用一些现有的函数和类从 CSV 文件中读取数据，并以不同的格式打印出来。

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

在这段代码中，我们首先导入必要的模块和函数。然后从 `portfolio.csv` 文件中读取数据并创建一个 `portfolio` 对象。之后，我们使用不同的格式名称（'text'、'csv' 和 'html'）测试 `create_formatter()` 函数。对于每种格式，我们创建一个格式化器对象，打印格式名称，然后使用 `print_table()` 函数以指定的格式打印 `portfolio` 数据。

当你运行这段代码时，你应该会看到三种格式的输出，每种格式由格式名称分隔：

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

工厂函数使代码更具用户友好性，因为它隐藏了类实例化的细节。用户无需知道如何创建格式化器对象，只需指定他们想要的格式即可。

使用工厂函数创建对象的这种模式是面向对象编程中一种常见的设计模式，称为工厂模式（Factory Pattern）。它在客户端代码（使用格式化器的代码）和实际实现类（格式化器类）之间提供了一层抽象。这使得代码更具模块化，更易于使用。

**关键概念回顾：**

1. **抽象基类**：`TableFormatter` 类充当一个接口。接口定义了一组所有实现它的类必须具备的方法。在我们的例子中，所有格式化器类都必须实现 `TableFormatter` 类中定义的方法。
2. **继承**：具体的格式化器类，如 `TextTableFormatter`、`CSVTableFormatter` 和 `HTMLTableFormatter`，继承自基类 `TableFormatter`。这意味着它们从基类获取基本结构和方法，并可以提供自己的特定实现。
3. **多态性**：`print_table()` 函数可以与任何实现了所需接口的格式化器一起工作。这意味着你可以将不同的格式化器对象传递给 `print_table()` 函数，它都能正确处理。
4. **工厂模式**：`create_formatter()` 函数简化了格式化器对象的创建过程。它根据格式名称处理创建正确对象的细节，因此用户无需为此操心。

通过运用这些面向对象的原则，我们创建了一个灵活且可扩展的系统，用于以各种输出格式格式化表格数据。
