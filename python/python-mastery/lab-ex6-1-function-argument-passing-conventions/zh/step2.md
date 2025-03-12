# 创建结构基类

既然我们已经很好地理解了函数参数传递，接下来我们将为数据结构创建一个可复用的基类。这一步至关重要，因为当我们创建简单的数据持有类时，它能帮助我们避免反复编写相同的代码。通过使用基类，我们可以简化代码并提高效率。

## 重复代码的问题

在前面的练习中，你定义了一个 `Stock` 类，如下所示：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

仔细观察 `__init__` 方法，你会发现它相当重复。你必须逐个手动分配每个属性。这会变得非常繁琐且耗时，尤其是当你有许多具有大量属性的类时。

## 创建灵活的基类

让我们创建一个 `Structure` 基类，它可以自动处理属性分配。首先，打开 WebIDE 并创建一个名为 `structure.py` 的新文件。然后，将以下代码添加到该文件中：

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

这个基类有几个重要的特性：

1. 它定义了一个 `_fields` 类变量。默认情况下，这个变量为空。这个变量将保存类将具有的属性名称。
2. 它会检查传递给构造函数的参数数量是否与 `_fields` 中定义的字段数量匹配。如果不匹配，它会引发一个 `TypeError`。这有助于我们尽早捕获错误。
3. 它使用字段名称和作为参数提供的值来设置对象的属性。`setattr` 函数用于动态设置属性。

## 测试我们的结构基类

现在，让我们创建一些继承自 `Structure` 基类的示例类。将以下代码添加到你的 `structure.py` 文件中：

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

为了测试我们的实现是否正确，我们将创建一个名为 `test_structure.py` 的测试文件。将以下代码添加到该文件中：

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

要运行测试，请打开终端并执行以下命令：

```bash
python3 test_structure.py
```

你应该会看到以下输出：

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

如你所见，我们的基类按预期工作。它让定义新的数据结构变得容易多了，无需反复编写相同的样板代码。
