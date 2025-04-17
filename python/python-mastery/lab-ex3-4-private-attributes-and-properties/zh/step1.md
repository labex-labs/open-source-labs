# 实现私有属性

在 Python 中，我们使用命名约定来表明一个属性旨在供类内部使用。我们在这些属性前加上下划线 (`_`)。这向其他开发者发出信号，表明这些属性不是公共 API 的一部分，不应从类外部直接访问。

让我们看看 `stock.py` 文件中当前的 `Stock` 类。它有一个名为 `types` 的类变量。

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

`types` 类变量在内部用于转换行数据。为了表明这是一个实现细节，我们将它标记为私有。

**说明：**

1.  在编辑器中打开 `stock.py` 文件。

2.  修改 `types` 类变量，添加前导下划线，将其更改为 `_types`。

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  更新 `from_row` 方法以使用重命名的变量 `_types`。

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  保存 `stock.py` 文件。

5.  创建一个名为 `test_stock.py` 的 Python 脚本来测试你的更改。你可以使用以下命令在编辑器中创建文件：

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  将以下代码添加到 `test_stock.py` 文件。此代码创建 `Stock` 类的实例并打印有关它们的信息。

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
    print(f"Cost: {s.cost()}")

    # Create from row
    row = ['AAPL', '50', '142.5']
    apple = Stock.from_row(row)
    print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
    print(f"Cost: {apple.cost()}")
    ```

7.  使用终端中的以下命令运行测试脚本：

    ```bash
    python /home/labex/project/test_stock.py
    ```

    你应该看到类似于以下的输出：

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```
