# 使用 `__slots__` 进行内存优化

在 Python 中，`__slots__` 属性是一个特殊工具，能帮助你更高效地管理类。它可以限制类所能拥有的属性。通常，Python 将实例属性存储在一个名为 `__dict__` 的字典中，这允许动态添加新属性。然而，当你定义 `__slots__` 时，Python 会为实例创建一个静态结构。这主要有两个效果：一是防止向实例添加新属性，二是减少内存使用，因为无需维护 `__dict__`。

在我们的 `Stock` 类中，使用 `__slots__` 有两个重要原因：

1. 限制属性创建，仅允许使用我们定义的属性。这意味着类的使用者无法意外或故意添加我们未计划的新属性。
2. 提高内存效率，特别是在创建大量实例时。如果你有大量 `Stock` 类的对象，使用 `__slots__` 可以节省大量内存。

## 说明：

1. 首先，你需要在编辑器中打开 `stock.py` 文件。我们将在这个文件中对 `Stock` 类进行修改。在终端中使用以下命令：

   ```bash
   code /home/labex/project/stock.py
   ```

2. 在 `stock.py` 文件中，我们将添加一个 `__slots__` 类变量。这个变量应列出类使用的所有私有属性名。具体操作如下：

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Define slots to restrict attribute creation
       __slots__ = ('name', '_shares', '_price')

       # Rest of the class...
   ```

   通过这样定义 `__slots__`，我们告诉 Python，`Stock` 类的实例只能有 `name`、`_shares` 和 `_price` 这些属性。

3. 完成这些更改后，保存文件。这样可以确保你的修改被保存下来。

4. 现在，我们需要创建一个测试脚本来验证 `__slots__` 是否按预期工作。使用以下命令打开一个名为 `test_slots.py` 的新文件：

   ```bash
   code /home/labex/project/test_slots.py
   ```

5. 在 `test_slots.py` 文件中添加以下代码。这段代码将创建一个 `Stock` 类的实例，访问其现有属性，然后尝试添加一个新属性。

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)

   # Access existing attributes
   print(f"Name: {s.name}")
   print(f"Shares: {s.shares}")
   print(f"Price: {s.price}")
   print(f"Cost: {s.cost}")

   # Try to add a new attribute
   try:
       s.extra = "This will fail"
       print(f"Extra: {s.extra}")
   except AttributeError as e:
       print(f"Error: {e}")
   ```

   `try` 块尝试向 `Stock` 实例 `s` 添加一个新属性 `extra`。如果 `__slots__` 正常工作，这应该会引发一个 `AttributeError`，因为 `extra` 未在 `__slots__` 中列出。

6. 最后，使用以下命令运行测试脚本：
   ```bash
   python /home/labex/project/test_slots.py
   ```

你应该会看到输出显示你可以访问已定义的属性，但尝试添加新属性会引发 `AttributeError`。这证实了 `__slots__` 按预期工作。

### 理解 `__slots__`

使用 `__slots__` 时，需要牢记以下几点：

1. 你必须列出将存储在实例上的所有属性。如果你忘记列出某个属性，就无法将其赋值给实例。
2. 只有 `__slots__` 中列出的属性才能赋值给实例。这有助于为对象强制执行严格的结构。
3. 实例将不再有 `__dict__` 属性。由于 `__slots__` 创建了一个静态结构，因此不需要动态字典。
4. 子类不会继承其父类的 `__slots__`，除非它们自己定义 `__slots__`。这意味着子类可以灵活地定义自己的属性限制。

使用 `__slots__` 的主要好处有：

1. **内存效率**：由于无需使用 `__dict__` 来存储属性，实例使用的内存更少。
2. **速度**：属性访问稍快，因为 Python 无需在字典中查找属性。
3. **防止意外创建属性**：通过防止添加意外的属性，有助于捕获拼写错误和编程错误。
