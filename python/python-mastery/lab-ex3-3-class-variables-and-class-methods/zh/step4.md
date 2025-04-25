# 创建通用的 CSV 读取器

在这最后一步，我们将创建一个通用函数。该函数能够读取 CSV 文件，并创建任何实现了 `from_row()` 类方法的类的对象。这展示了将类方法用作统一接口的强大之处。统一接口意味着不同的类可以以相同的方式使用，这使我们的代码更灵活、更易于管理。

## 修改 `read_portfolio()` 函数

首先，我们将更新 `stock.py` 文件中的 `read_portfolio()` 函数。我们将使用新的 `from_row()` 类方法。打开 `stock.py` 文件，并将 `read_portfolio()` 函数修改如下：

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

这个新版本的函数更简单。它将类型转换的职责交给了 `Stock` 类，这才是它真正所属的地方。类型转换是指将数据从一种类型转换为另一种类型，比如将字符串转换为整数。通过这样做，我们使代码更有条理、更易于理解。

## 创建通用的 CSV 读取器

现在，我们将在 `reader.py` 文件中创建一个更通用的函数。这个函数可以读取 CSV 数据，并创建任何具有 `from_row()` 类方法的类的实例。

打开 `reader.py` 文件，并添加以下函数：

```python
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of the given class.

    Args:
        filename: Name of the CSV file
        cls: Class to instantiate (must have from_row class method)

    Returns:
        List of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

这个函数接受两个输入：一个文件名和一个类。然后，它返回一个由该类的实例组成的列表，这些实例是根据 CSV 文件中的数据创建的。这非常有用，因为只要类具有 `from_row()` 方法，我们就可以将该函数与不同的类一起使用。

## 测试通用的 CSV 读取器

让我们创建一个测试文件，看看我们的通用读取器是如何工作的。创建一个名为 `test_csv_reader.py` 的文件，内容如下：

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Read portfolio as Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"Portfolio contains {len(portfolio)} stocks")
print(f"First stock: {portfolio[0].name}, {portfolio[0].shares} shares at ${portfolio[0].price}")

# Read portfolio as DStock instances (with Decimal prices)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nDecimal portfolio contains {len(decimal_portfolio)} stocks")
print(f"First stock: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} shares at ${decimal_portfolio[0].price}")

# Define a new class for reading the bus data
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Read some bus data (just the first 5 records for brevity)
print("\nReading bus data...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip header
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Only read 5 records for the example
            break
        bus_rides.append(BusRide.from_row(row))

# Display the bus data
for ride in bus_rides:
    print(f"Route: {ride.route}, Date: {ride.date}, Type: {ride.daytype}, Rides: {ride.rides}")
```

运行这个文件以查看结果。打开终端并使用以下命令：

```bash
cd ~/project
python test_csv_reader.py
```

你应该会看到输出显示投资组合数据被加载为 `Stock` 和 `DStock` 实例，公交路线数据被加载为 `BusRide` 实例。这证明我们的通用读取器可以与不同的类一起使用。

## 这种方法的主要优点

这种方法展示了几个强大的概念：

1. **关注点分离**：读取数据与创建对象是分开的。这意味着读取 CSV 文件的代码不会与创建对象的代码混合在一起。这使代码更易于理解和维护。
2. **多态性**：相同的代码可以与遵循相同接口的不同类一起工作。在我们的例子中，只要一个类具有 `from_row()` 方法，我们的通用读取器就可以使用它。
3. **灵活性**：我们可以通过使用不同的类轻松更改数据的转换方式。例如，我们可以使用 `Stock` 或 `DStock` 以不同的方式处理投资组合数据。
4. **可扩展性**：我们可以添加与读取器一起工作的新类，而无需更改读取器代码。这使我们的代码更具前瞻性。

这是 Python 中一种常见的模式，它使代码更模块化、可重用和易于维护。

## 关于类方法的最后说明

在 Python 中，类方法通常用作替代构造函数。你通常可以通过它们的名称来区分，因为它们的名称中通常包含“from”这个词。例如：

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

遵循这个约定，你可以使代码更具可读性，并与 Python 的内置库保持一致。这有助于其他开发者更轻松地理解你的代码。
