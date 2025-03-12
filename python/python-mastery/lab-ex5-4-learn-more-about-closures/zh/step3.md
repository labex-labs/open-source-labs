# 使用描述符消除属性名冗余

在上一步中，当创建类型化属性时，你必须显式指定属性名。这是多余的，因为属性名已经在类定义中指定了。在这一步中，你将使用描述符（descriptor）来消除这种冗余。

在 Python 中，描述符是一种特殊的对象，它控制属性访问的方式。当你在描述符中实现 `__set_name__` 方法时，它可以自动从类定义中获取属性名。

让我们从创建一个新文件开始。

1. 创建一个名为 `improved_typedproperty.py` 的新文件，并添加以下代码：

```python
# improved_typedproperty.py

class TypedProperty:
    """
    A descriptor that performs type checking.

    This descriptor automatically captures the attribute name from the class definition.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Convenience functions
def String():
    """Create a string property with type checking."""
    return TypedProperty(str)

def Integer():
    """Create an integer property with type checking."""
    return TypedProperty(int)

def Float():
    """Create a float property with type checking."""
    return TypedProperty(float)
```

这段代码定义了一个名为 `TypedProperty` 的描述符类，用于检查分配给属性的值的类型。当描述符被分配给类属性时，`__set_name__` 方法会自动调用。这使得描述符可以自动捕获属性名，而无需手动指定。

接下来，你将创建一个使用这些改进后的类型化属性的类。

2. 创建一个名为 `stock_improved.py` 的新文件，使用改进后的类型化属性：

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    # No need to specify property names anymore
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

注意，在创建类型化属性时，你不再需要指定属性名。描述符会自动从类定义中获取属性名。

现在，让我们测试改进后的类。

3. 创建一个测试文件 `test_stock_improved.py` 来测试改进后的版本：

```python
from stock_improved import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try setting attributes with wrong types
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

最后，你将运行测试，看看一切是否按预期工作。

4. 运行测试：

```bash
python3 test_stock_improved.py
```

你应该会看到类似于以下的输出：

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

在这一步中，你通过使用描述符和 `__set_name__` 方法改进了类型检查系统。这消除了多余的属性名指定，使代码更简洁，减少了出错的可能性。

`__set_name__` 方法是描述符的一个非常有用的特性。它允许描述符自动收集它们在类定义中的使用信息。这可以用于创建更易于理解和使用的 API。
