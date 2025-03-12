# 使用代理创建只读对象

在这一步中，我们将探索代理类（proxy classes），这是 Python 中非常有用的一种模式。代理类允许你在不修改现有对象原始代码的情况下，改变其行为。这就像是给对象套上一个特殊的包装，以添加新功能或施加限制。

## 什么是代理？

代理是介于你和另一个对象之间的对象。它具有与原始对象相同的一组函数和属性，但可以做额外的事情。例如，它可以控制谁能访问该对象、记录操作（日志记录）或添加其他有用的功能。

让我们创建一个只读代理。这种代理将阻止你更改对象的属性。

### 步骤 1：创建只读代理类

首先，我们需要创建一个 Python 文件来定义我们的只读代理。

1. 导航到 `/home/labex/project` 目录。
2. 在该目录下创建一个名为 `readonly_proxy.py` 的新文件。
3. 打开 `readonly_proxy.py` 文件，并添加以下代码：

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

在这段代码中，定义了 `ReadonlyProxy` 类。`__init__` 方法存储我们要包装的对象。我们使用 `self.__dict__` 直接存储它，以避免调用 `__setattr__` 方法。`__getattr__` 方法在我们尝试访问代理的属性时使用。它只是将请求传递给被包装的对象。`__setattr__` 方法在我们尝试更改属性时被调用。它会引发一个错误，以防止任何更改。

### 步骤 2：创建测试文件

现在，我们将创建一个测试文件，以查看我们的只读代理如何工作。

1. 在同一 `/home/labex/project` 目录下创建一个名为 `test_readonly.py` 的新文件。
2. 将以下代码添加到 `test_readonly.py` 文件中：

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

在这个测试代码中，我们首先创建一个普通的 `Stock` 对象并打印其信息。然后我们修改它的一个属性并打印更新后的信息。接下来，我们为 `Stock` 对象创建一个只读代理并打印其信息。最后，我们尝试修改只读代理，并期望得到一个错误。

### 步骤 3：运行测试脚本

创建代理类和测试文件后，我们需要运行测试脚本以查看结果。

1. 打开一个终端，并使用以下命令导航到 `/home/labex/project` 目录：

```bash
cd /home/labex/project
```

2. 使用以下命令运行测试脚本：

```bash
python3 test_readonly.py
```

你应该会看到类似于以下的输出：

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## 代理的工作原理

`ReadonlyProxy` 类使用两个特殊方法来实现其只读功能：

1. `__getattr__(self, name)`：当 Python 无法以正常方式找到属性时，会调用此方法。在我们的 `ReadonlyProxy` 类中，我们使用 `getattr()` 函数将属性访问请求传递给被包装的对象。因此，当你尝试访问代理的属性时，它实际上会从被包装的对象获取该属性。

2. `__setattr__(self, name, value)`：当你尝试为属性赋值时，会调用此方法。在我们的实现中，我们引发一个 `AttributeError` 来阻止对代理属性进行任何更改。

3. 在 `__init__` 方法中，我们直接修改 `self.__dict__` 来存储被包装的对象。这很重要，因为如果我们使用正常方式分配对象，它会调用 `__setattr__` 方法，这会引发错误。

这种代理模式允许我们在不更改任何现有对象原始类的情况下，为其添加一个只读层。代理对象的行为就像被包装的对象，但不允许你进行任何修改。
