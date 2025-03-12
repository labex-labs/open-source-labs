# 实现私有属性

在 Python 中，当我们设计一个类时，有些属性仅用于类内部。这些属性是类内部实现的一部分。为了向其他开发者表明这一点，我们遵循一种命名约定，即在这些内部属性前加一个下划线 (`_`)。这就像是一个标志，表明这些属性不属于公共 API。公共 API 是代码其他部分应该与之交互的一组方法和属性。因此，带有下划线的属性不应该从类外部直接访问。

让我们看一下 `stock.py` 文件中当前的 `Stock` 类。这个类用于表示股票，它有一个名为 `types` 的类变量。

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

`types` 类变量在类内部用于转换行数据。例如，当我们获取一行数据时，我们使用这些类型将数据转换为正确的格式。由于这只是一个实现细节，不是代码其他部分应该直接交互的内容，我们应该将其标记为私有。

## 说明：

1. 首先，你需要在编辑器中打开 `stock.py` 文件。你可以在终端中使用以下命令来完成。这个命令将在代码编辑器中打开该文件。

   ```bash
   code /home/labex/project/stock.py
   ```

2. 现在，你要修改 `types` 类变量。在它前面加上一个下划线，使其变为 `_types`。这个更改表明这个变量是私有的，不应该从类外部直接访问。

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Rest of the class...
   ```

3. 重命名变量后，你需要更新 `from_row` 方法。这个方法使用 `types` 变量来转换行数据。现在你已将其重命名为 `_types`，需要相应地更新该方法。

   ```python
   @classmethod
   def from_row(cls, row):
       values = [func(val) for func, val in zip(cls._types, row)]
       return cls(*values)
   ```

4. 完成这些更改后，你需要保存文件。保存文件可确保你的更改被保存下来，以便后续使用。

5. 为了测试你的更改，你要创建一个名为 `test_stock.py` 的 Python 脚本。你可以使用以下命令在编辑器中打开该文件。

   ```bash
   code /home/labex/project/test_stock.py
   ```

6. 现在，将以下代码添加到 `test_stock.py` 文件中。这段代码创建 `Stock` 类的实例，既可以直接创建，也可以使用 `from_row` 方法创建。然后，它会打印出这些实例的信息，如名称、股数、价格和成本。

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

7. 最后，在终端中使用以下命令运行测试脚本。这将执行 `test_stock.py` 文件中的代码，并显示输出结果。

   ```bash
   python /home/labex/project/test_stock.py
   ```

你应该会看到类似于以下的输出：

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Name: AAPL, Shares: 50, Price: 142.5
Cost: 7125.0
```
