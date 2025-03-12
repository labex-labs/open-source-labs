# 挑战：将可调用对象用作方法

在 Python 中，当你将可调用对象用作类中的方法时，会遇到一个独特的挑战。可调用对象是指像函数一样可以“调用”的对象，比如函数本身，或者带有 `__call__` 方法的对象。当将其用作类方法时，由于 Python 会将实例（`self`）作为第一个参数传递，它并不总是能按预期工作。

让我们通过创建一个 `Stock` 类来探讨这个问题。这个类将表示一只股票，包含名称、股数和价格等属性。我们还将使用一个验证器来确保我们处理的数据是正确的。

首先，打开 `stock.py` 文件，开始编写我们的 `Stock` 类。你可以使用以下命令在编辑器中打开该文件：

```bash
code /home/labex/project/stock.py
```

现在，将以下代码添加到 `stock.py` 文件中。这段代码定义了 `Stock` 类，其中包含一个 `__init__` 方法来初始化股票的属性，一个 `cost` 属性来计算总成本，以及一个 `sell` 方法来减少股数。我们还将尝试使用 `ValidatedFunction` 来验证 `sell` 方法的输入。

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

定义好 `Stock` 类后，我们需要对其进行测试，看看它是否能按预期工作。创建一个名为 `test_stock.py` 的测试文件，并使用以下命令打开它：

```bash
code /home/labex/project/test_stock.py
```

将以下代码添加到 `test_stock.py` 文件中。这段代码创建了一个 `Stock` 类的实例，打印出初始股数和成本，尝试卖出一些股票，然后打印出更新后的股数和成本。

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

现在，使用以下命令运行测试文件：

```bash
python3 /home/labex/project/test_stock.py
```

你可能会遇到类似以下的错误：

```
Error: missing a required argument: 'nshares'
```

这个错误的出现是因为当 Python 调用像 `s.sell(10)` 这样的方法时，实际上在幕后调用的是 `Stock.sell(s, 10)`。`self` 参数代表类的实例，它会自动作为第一个参数传递。然而，我们的 `ValidatedFunction` 没有正确处理这个 `self` 参数，因为它不知道自己被用作方法。

**理解问题**

当你在类中定义一个方法，然后用 `ValidatedFunction` 替换它时，实际上是在包装原始方法。问题在于，包装后的方法不能自动正确处理 `self` 参数。它期望参数的方式没有考虑到实例会作为第一个参数传递。

**解决问题**

为了解决这个问题，我们需要修改处理方法的方式。我们将创建一个名为 `ValidatedMethod` 的新类，它可以正确处理方法调用。将以下代码添加到 `validate.py` 文件的末尾：

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

现在，我们需要修改 `Stock` 类，使用 `ValidatedMethod` 而不是 `ValidatedFunction`。再次打开 `stock.py` 文件：

```bash
code /home/labex/project/stock.py
```

将 `Stock` 类更新如下：

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

`ValidatedMethod` 类是一个描述符（descriptor），它是 Python 中的一种特殊对象，可以改变属性的访问方式。当属性作为方法被访问时，`__get__` 方法会被调用。它会返回一个可调用对象，该对象会正确地将实例作为第一个参数传递。

再次使用以下命令运行测试文件：

```bash
python3 /home/labex/project/test_stock.py
```

现在你应该会看到类似以下的输出：

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

这个挑战向你展示了可调用对象的一个重要方面。当将它们用作类中的方法时，需要特殊处理。通过使用 `__get__` 方法实现描述符协议，我们可以创建既能作为独立函数又能作为方法正常工作的可调用对象。
