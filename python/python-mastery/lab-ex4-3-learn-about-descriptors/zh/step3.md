# 使用描述符实现验证器

在这一步中，我们将使用描述符创建一个验证系统。但首先，让我们了解一下什么是描述符以及为什么要使用它们。描述符是实现了描述符协议的 Python 对象，该协议包括 `__get__`、`__set__` 或 `__delete__` 方法。它们允许你自定义对象属性的访问、设置或删除方式。在我们的例子中，我们将使用描述符创建一个验证系统，以确保数据的完整性。这意味着存储在我们对象中的数据将始终满足某些条件，例如属于特定类型或具有正值。

现在，让我们开始创建验证系统。我们将在项目目录中创建一个名为 `validate.py` 的新文件。这个文件将包含实现我们验证器的类。

```python
# validate.py

class Validator:
    def __init__(self, name):
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

在 `validate.py` 文件中，我们首先定义了一个名为 `Validator` 的基类。这个类有一个 `__init__` 方法，它接受一个 `name` 参数，该参数将用于标识要验证的属性。`check` 方法是一个类方法，它只是返回传递给它的值。`__set__` 方法是一个描述符方法，当在对象上设置属性时会调用它。它调用 `check` 方法来验证值，然后将验证后的值存储在对象的字典中。

然后，我们定义了 `Validator` 的三个子类：`String`、`PositiveInteger` 和 `PositiveFloat`。每个子类都重写了 `check` 方法以执行特定的验证检查。`String` 类检查值是否为字符串，`PositiveInteger` 类检查值是否为正整数，`PositiveFloat` 类检查值是否为正数（整数或浮点数）。

现在我们已经定义了验证器，让我们修改 `Stock` 类以使用这些验证器。我们将创建一个名为 `stock_with_validators.py` 的新文件，并从 `validate.py` 文件中导入验证器。

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

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

在 `stock_with_validators.py` 文件中，我们定义了 `Stock` 类，并将验证器用作类属性。这意味着每当在 `Stock` 对象上设置属性时，相应验证器的 `__set__` 方法将被调用来验证值。`__init__` 方法初始化 `Stock` 对象的属性，`cost`、`sell` 和 `__repr__` 方法提供了额外的功能。

现在，让我们测试基于验证器的 `Stock` 类。我们将打开一个终端，导航到项目目录，并以交互模式运行 `stock_with_validators.py` 文件。

```bash
cd ~/project
python3 -i stock_with_validators.py
```

一旦 Python 解释器运行起来，我们可以尝试一些命令来测试验证系统。

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

在测试代码中，我们首先创建一个具有有效值的 `Stock` 对象，并打印其属性以验证它们是否设置正确。然后，我们尝试将 `shares` 属性更改为有效值，并再次打印以确认更改。最后，我们尝试将 `shares` 属性设置为无效值（字符串和负数），并捕获验证器引发的异常。

注意我们的代码现在变得多么简洁。`Stock` 类不再需要实现所有那些属性方法——验证器处理所有的类型检查和约束。

描述符使我们能够创建一个可重用的验证系统，该系统可以应用于任何类属性。这是一种在应用程序中维护数据完整性的强大模式。
