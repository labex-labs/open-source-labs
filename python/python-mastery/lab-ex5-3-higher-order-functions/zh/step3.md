# 重构现有函数

现在，我们已经创建了一个名为 `convert_csv()` 的高阶函数。高阶函数是可以接受其他函数作为参数或返回函数作为结果的函数。它们是 Python 中一个强大的概念，能帮助我们编写更具模块化和可复用性的代码。在本节中，我们将使用这个高阶函数来重构原始的 `csv_as_dicts()` 和 `csv_as_instances()` 函数。重构是在不改变现有代码外部行为的前提下对其进行结构调整的过程，目的是改善其内部结构，例如消除代码重复。

让我们先在 WebIDE 中打开 `reader.py` 文件。我们将按以下方式更新这些函数：

1. 首先，我们将替换 `csv_as_dicts()` 函数。这个函数用于将 CSV 数据行转换为字典列表。以下是新代码：

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

在这段代码中，我们定义了一个内部函数 `dict_converter`，它接受 `headers` 和 `row` 作为参数。它使用字典推导式创建一个字典，其中键是列名，值是将相应的类型转换函数应用于行中值的结果。然后，我们将 `dict_converter` 函数作为参数调用 `convert_csv()` 函数。

2. 接下来，我们将替换 `csv_as_instances()` 函数。这个函数用于将 CSV 数据行转换为给定类的实例列表。以下是新代码：

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

在这段代码中，我们定义了一个内部函数 `instance_converter`，它接受 `headers` 和 `row` 作为参数。它调用给定类 `cls` 的 `from_row` 类方法，从行数据创建一个实例。然后，我们将 `instance_converter` 函数作为参数调用 `convert_csv()` 函数。

重构这些函数后，我们需要对它们进行测试，以确保它们仍能按预期工作。为此，我们将在 Python shell 中运行以下命令：

```bash
cd ~/project
python3 -i reader.py
```

`cd ~/project` 命令将当前工作目录更改为 `project` 目录。`python3 -i reader.py` 命令以交互模式运行 `reader.py` 文件，这意味着在文件运行结束后，我们可以继续执行 Python 代码。

Python shell 打开后，我们将运行以下代码来测试重构后的函数：

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

在这段代码中，我们首先定义了一个简单的 `Stock` 类用于测试。`__init__` 方法初始化 `Stock` 实例的属性。`from_row` 类方法从 CSV 数据行创建一个 `Stock` 实例。`__repr__` 方法提供 `Stock` 实例的字符串表示形式。

然后，我们通过打开 `portfolio.csv` 文件并将其与类型转换函数列表一起传递给 `csv_as_dicts()` 函数来测试该函数。我们打印结果列表中的第一个字典。

最后，我们通过打开 `portfolio.csv` 文件并将其与 `Stock` 类一起传递给 `csv_as_instances()` 函数来测试该函数。我们打印结果列表中的第一个实例。

如果一切正常，你应该会看到类似于以下的输出：

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

这个输出表明我们重构后的函数工作正常。我们成功消除了代码重复，同时保持了相同的功能。

要退出 Python shell，你可以输入 `exit()` 或按 Ctrl+D。
