# 实现属性验证

Python 中的属性（property）是一个强大的特性。它不仅允许你像访问普通属性一样访问计算值，还能让你控制这些属性值的获取、设置和删除方式。当你需要对属性进行验证时，这种控制就非常有用。验证可以确保分配给属性的值符合特定标准，有助于维护数据的完整性。

在我们的 `Stock` 类中，有两个重要的属性：`shares` 和 `price`。我们要确保 `shares` 是一个非负整数，`price` 是一个非负浮点数。为了实现这种验证，我们将使用属性装饰器以及 getter 和 setter 方法。

## 说明：

1. 首先，你需要在编辑器中打开 `stock.py` 文件。我们将在这个文件中对 `Stock` 类进行所有修改。在终端中使用以下命令：

   ```bash
   code /home/labex/project/stock.py
   ```

2. 在 Python 中，我们可以使用私有属性来存储类变量的实际值。私有属性以一个下划线开头。在 `Stock` 类中添加私有属性 `_shares` 和 `_price`，并修改构造函数以使用它们。构造函数是在创建类的新实例时调用的方法。具体操作如下：

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self._shares = shares  # Using private attribute
       self._price = price    # Using private attribute
   ```

3. 现在，我们将为 `shares` 和 `price` 定义带有适当验证的属性。属性使用 `@property` 装饰器定义 getter 方法，使用 `@<property_name>.setter` 装饰器定义 setter 方法。getter 方法用于获取属性的值，setter 方法用于设置属性的值。以下是添加带有验证的属性定义的代码：

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, int):
           raise TypeError("Expected integer")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, float):
           raise TypeError("Expected float")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

4. 更新构造函数以使用属性的 setter 方法进行验证。这样，每当创建 `Stock` 类的新实例时，`shares` 和 `price` 的值将自动进行验证。以下是更新后的构造函数：

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self.shares = shares  # Using property setter
       self.price = price    # Using property setter
   ```

5. 完成所有这些更改后，保存 `stock.py` 文件。这样可以确保你的更改被保存下来。

6. 为了验证我们的验证机制是否正常工作，我们将创建一个测试脚本。使用以下命令在编辑器中打开一个名为 `test_validation.py` 的新文件：

   ```bash
   code /home/labex/project/test_validation.py
   ```

7. 在 `test_validation.py` 文件中添加以下代码。这段代码创建一个有效的 `Stock` 实例，然后尝试用有效和无效的值更新 `shares` 和 `price` 属性。它还会打印结果以及出现的任何错误消息。

   ```python
   from stock import Stock

   # Create a valid stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

   # Test valid updates
   try:
       s.shares = 50  # Valid update
       print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting shares=50: {e}")

   try:
       s.price = 123.45  # Valid update
       print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting price=123.45: {e}")

   # Test invalid updates
   try:
       s.shares = "50"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares='50': {e}")

   try:
       s.shares = -10  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares=-10: {e}")

   try:
       s.price = "123.45"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price='123.45': {e}")

   try:
       s.price = -10.0  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price=-10.0: {e}")
   ```

8. 最后，在终端中使用以下命令运行测试脚本：
   ```bash
   python /home/labex/project/test_validation.py
   ```

你应该会看到输出显示有效的更新成功，并且对于无效的更新会显示相应的错误消息。这证实了我们的属性验证机制按预期工作。
