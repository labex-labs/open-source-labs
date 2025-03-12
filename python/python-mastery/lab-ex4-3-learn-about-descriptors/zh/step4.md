# 改进描述符的实现

在这一步中，我们将增强描述符的实现。你可能已经注意到，在某些情况下，我们会重复指定名称。这会让代码变得有些杂乱，也更难维护。为了解决这个问题，我们将使用 `__set_name__` 方法，这是 Python 3.6 引入的一个实用特性。

`__set_name__` 方法会在类定义时自动调用。它的主要作用是为我们设置描述符的名称，这样我们就不必每次都手动设置了。这会让我们的代码更简洁、更高效。

现在，让我们更新 `validate.py` 文件，加入 `__set_name__` 方法。更新后的代码如下：

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
            self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

在上述代码中，`Validator` 类的 `__set_name__` 方法会检查 `name` 属性是否为 `None`。如果是，它会将 `name` 设置为类定义中使用的实际属性名。这样，我们在创建描述符类的实例时就不必显式指定名称了。

现在我们已经更新了 `validate.py` 文件，可以创建一个改进版的 `Stock` 类。这个新版本不需要我们重复指定名称。以下是改进后的 `Stock` 类的代码：

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

在这个 `Stock` 类中，我们只需创建 `String`、`PositiveInteger` 和 `PositiveFloat` 描述符类的实例，而无需指定名称。`Validator` 类中的 `__set_name__` 方法会自动处理名称的设置。

让我们测试一下改进后的 `Stock` 类。首先，打开终端并导航到项目目录。然后，以交互模式运行 `improved_stock.py` 文件。以下是相应的命令：

```bash
cd ~/project
python3 -i improved_stock.py
```

进入交互式 Python 会话后，你可以尝试以下命令来测试 `Stock` 类的功能：

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

这些命令创建了一个 `Stock` 类的实例，打印其属性，更改属性值，然后尝试设置无效值，以查看是否会引发相应的错误。

`__set_name__` 方法会在类定义时自动设置描述符的名称。这让你的代码更简洁，减少了冗余，因为你不再需要两次指定属性名。

这一改进展示了 Python 的描述符协议是如何不断发展的，让编写简洁、可维护的代码变得更加容易。
