# 协调类型验证与类变量

在我们的 Python 编程之旅中，我们创建了一个 `Stock` 类。目前，这个类有两种不同的方式来处理数据类型。理解这些机制至关重要，因为它有助于我们更好地管理和组织代码。

第一种机制是 `_types` 类变量。这个变量用于从行数据中转换数据类型。当我们以行格式获取数据时，`_types` 变量帮助我们将这些数据转换为 `Stock` 类所需的适当类型。

第二种机制是属性的 setter 方法。这些 setter 方法强制执行类型检查。每当我们尝试为 `Stock` 类的某个属性设置值时，属性的 setter 方法会确保该值是正确的类型。

然而，使用两种独立的机制会使我们的类难以维护。为了解决这个问题，我们需要协调这两种机制，让它们使用相同的类型信息。这样，我们就能确保类的一致性，并且在创建子类时，类会更加可靠。

## 说明：

1. 首先，我们需要在编辑器中打开 `stock.py` 文件。这个文件包含了 `Stock` 类的代码。要打开它，请在终端中运行以下命令：

   ```bash
   code /home/labex/project/stock.py
   ```

2. 现在，我们将修改 `stock.py` 文件中的属性 setter 方法。我们希望它们使用 `_types` 类变量中定义的类型。这样可以确保属性 setter 方法中的类型检查与 `_types` 变量进行的类型转换保持一致。以下是修改属性 setter 方法的代码：

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, self._types[1]):
           raise TypeError(f"Expected {self._types[1].__name__}")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, self._types[2]):
           raise TypeError(f"Expected {self._types[2].__name__}")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

3. 完成这些更改后，保存 `stock.py` 文件。保存文件可以确保我们的修改被保留。

4. 接下来，我们将创建一个测试脚本来验证使用不同类型的子类是否按预期工作。要创建这个脚本，请在终端中运行以下命令：

   ```bash
   code /home/labex/project/test_subclass.py
   ```

5. 现在，在 `test_subclass.py` 文件中添加以下代码。这段代码创建了一个 `Stock` 类的子类，使用不同的类型，并对基类和子类进行测试。

   ```python
   from stock import Stock
   from decimal import Decimal

   # Create a subclass with different types
   class DStock(Stock):
       _types = (str, int, Decimal)

   # Test the base class
   s = Stock('GOOG', 100, 490.10)
   print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

   # Test valid update with float
   try:
       s.price = 500.25
       print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
   except Exception as e:
       print(f"Error updating Stock price: {e}")

   # Test the subclass with Decimal
   ds = DStock('AAPL', 50, Decimal('142.50'))
   print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

   # Test invalid update with float (should require Decimal)
   try:
       ds.price = 150.75
       print(f"Updated DStock price: {ds.price}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")

   # Test valid update with Decimal
   try:
       ds.price = Decimal('155.25')
       print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
   except Exception as e:
       print(f"Error updating DStock price: {e}")
   ```

6. 最后，运行测试脚本来查看结果。在终端中运行以下命令：

   ```bash
   python /home/labex/project/test_subclass.py
   ```

当你运行测试脚本时，你应该会看到基类 `Stock` 接受浮点数作为价格，而子类 `DStock` 要求使用 `Decimal` 类型的值。这表明我们的类型协调按预期工作。

### 讨论

通过协调 `Stock` 类中的类型信息，我们使类更加一致。现在，属性的 setter 方法使用与 `from_row` 方法相同的类型信息。这种一致性使类更易于维护和扩展，特别是在创建子类时。

虽然我们当前的 `Stock` 类实现对于一个简单的概念来说可能看起来很复杂，但它展示了 Python 中封装和类型安全的重要技术。在实际应用中，你可能希望使用更高级的工具，如数据类（dataclasses）或第三方库来简化这种实现。这些工具可以使你的代码更加简洁，更易于管理。
