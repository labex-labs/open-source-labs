# 作为代码生成器的闭包

在这一步中，你将学习如何使用闭包动态生成代码。具体来说，你将使用闭包为类属性构建一个类型检查系统。

首先，让我们了解一下什么是闭包。闭包是一个函数对象，即使封闭作用域中的值不在内存中，它也能记住这些值。在 Python 中，当一个嵌套函数引用其封闭函数中的值时，就会创建闭包。

现在，你将开始实现类型检查系统。

1. 在 `/home/labex/project` 目录下创建一个名为 `typedproperty.py` 的新文件，并添加以下代码：

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Create a property with type checking.

    Args:
        name: The name of the property
        expected_type: The expected type of the property value

    Returns:
        A property object that performs type checking
    """
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

在这段代码中，`typedproperty` 函数是一个闭包。它接受两个参数：`name` 和 `expected_type`。`@property` 装饰器用于为属性创建一个 getter 方法，该方法用于获取私有属性的值。`@value.setter` 装饰器创建一个 setter 方法，用于检查设置的值是否为预期的类型。如果不是，则会引发 `TypeError`。

2. 现在，让我们创建一个使用这些类型化属性的类。创建一个名为 `stock.py` 的文件，并添加以下代码：

```python
from typedproperty import typedproperty

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

在 `Stock` 类中，你使用 `typedproperty` 函数为 `name`、`shares` 和 `price` 创建类型检查属性。当你创建 `Stock` 类的实例时，类型检查将自动应用。

3. 让我们创建一个测试文件来查看实际效果。创建一个名为 `test_stock.py` 的文件，并添加以下代码：

```python
from stock import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

在这个测试文件中，你首先创建一个具有正确类型的 `Stock` 对象。然后，你尝试将 `shares` 属性设置为字符串，这应该会引发 `TypeError`，因为预期的类型是整数。

4. 运行测试文件：

```bash
python3 test_stock.py
```

你应该会看到类似于以下的输出：

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

这个输出表明类型检查正常工作。

5. 现在，让我们通过为常见类型添加便捷函数来增强 `typedproperty.py`。在文件末尾添加以下代码：

```python
def String(name):
    """Create a string property with type checking."""
    return typedproperty(name, str)

def Integer(name):
    """Create an integer property with type checking."""
    return typedproperty(name, int)

def Float(name):
    """Create a float property with type checking."""
    return typedproperty(name, float)
```

这些函数只是 `typedproperty` 函数的包装器，使创建常见类型的属性更加容易。

6. 创建一个名为 `stock_enhanced.py` 的新文件，使用这些便捷函数：

```python
from typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

这个 `Stock` 类使用便捷函数创建类型检查属性，使代码更具可读性。

7. 创建一个测试文件 `test_stock_enhanced.py` 来测试增强版本：

```python
from stock_enhanced import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

这个测试文件与之前的类似，但它测试的是增强后的 `Stock` 类。

8. 运行测试：

```bash
python3 test_stock_enhanced.py
```

你应该会看到类似于以下的输出：

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

在这一步中，你已经演示了如何使用闭包生成代码。`typedproperty` 函数创建执行类型检查的属性对象，而 `String`、`Integer` 和 `Float` 函数为常见类型创建专门的属性。
