# 添加行转换功能

在编程中，从数据行创建类的实例通常很有用，尤其是在处理来自 CSV 文件等数据源的数据时。在本节中，我们将添加从数据行创建 `Structure` 类实例的功能。我们将通过在 `Structure` 类中实现一个 `from_row` 类方法来完成此操作。

1. 首先，你需要打开 `structure.py` 文件。我们将在此文件中进行代码更改。在终端中使用以下命令：

```bash
code ~/project/structure.py
```

2. 接下来，我们将修改 `validate_attributes` 函数。这个函数是一个类装饰器，它会提取 `Validator` 实例并自动构建 `_fields` 和 `_types` 列表。我们将更新它以同时收集类型信息。

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

在这个更新后的函数中，我们从每个验证器中收集 `expected_type` 属性，并将其存储在 `_types` 类变量中。这在我们将行数据转换为正确类型时会很有用。

3. 现在，我们将为 `Structure` 类添加 `from_row` 类方法。这个方法将允许我们从数据行（可以是列表或元组）创建类的实例。

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

这个方法的工作原理如下：

- 它接受一行数据，数据可以是列表或元组的形式。
- 它使用 `_types` 列表中对应的函数将行中的每个值转换为预期的类型。
- 然后，它使用转换后的值创建并返回类的一个新实例。

4. 进行这些更改后，保存 `structure.py` 文件。这可确保你的代码更改得以保留。

5. 让我们测试一下 `from_row` 方法，确保它按预期工作。我们将使用 `Stock` 类进行一个简单的测试。在终端中运行以下命令：

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

你应该会看到类似以下的输出：

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

注意，字符串值 '100' 和 '490.1' 被自动转换为了正确的类型（整数和浮点数）。这表明我们的 `from_row` 方法工作正常。

6. 最后，让我们尝试使用 `reader.py` 模块从 CSV 文件中读取数据。在终端中运行以下命令：

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

你应该会看到显示 CSV 文件中股票信息的输出：

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

`from_row` 方法使我们能够轻松地将 CSV 数据转换为 `Stock` 类的实例。与 `read_csv_as_instances` 函数结合使用时，我们就拥有了一种强大的方式来加载和处理结构化数据。
