# 理解 Python 中的属性访问

在 Python 中，对象是一个基本概念。对象可以将数据存储在属性中，属性就像是存储值的具名容器。你可以把属性看作是属于对象的变量。有几种方法可以访问这些属性。最直接且常用的方法是点号 (`.`) 表示法。不过，Python 还提供了一些特定的函数，让你在处理属性时拥有更多的灵活性。

## 点号表示法

让我们先创建一个 `Stock` 对象，看看如何使用点号表示法来操作它的属性。点号表示法是一种简单直观的访问和修改对象属性的方式。

首先，打开一个新的终端并启动 Python 交互式 shell。在这里，你可以逐行编写和执行 Python 代码。

```python
# Open a new terminal and run Python interactive shell
python3

# Import the Stock class from the stock module
from stock import Stock

# Create a Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(s.name)    # Output: 'GOOG'

# Set an attribute
s.shares = 50
print(s.shares)  # Output: 50

# Delete an attribute
del s.shares
# If we try to access s.shares now, we'll get an AttributeError
```

在上面的代码中，我们首先从 `stock` 模块导入 `Stock` 类。然后创建一个名为 `s` 的 `Stock` 类实例。要获取 `name` 属性的值，我们使用 `s.name`。要更改 `shares` 属性的值，我们只需为 `s.shares` 赋一个新值。如果我们想删除一个属性，可以使用 `del` 关键字，后面跟上属性名。

## 属性访问函数

Python 提供了四个非常有用的内置函数，用于属性操作。这些函数在处理属性时能让你拥有更多的控制权，特别是当你需要动态处理属性时。

1. `getattr()` - 此函数用于获取属性的值。
2. `setattr()` - 它允许你设置属性的值。
3. `delattr()` - 你可以使用此函数删除属性。
4. `hasattr()` - 此函数用于检查对象中是否存在某个属性。

让我们看看如何使用这些函数：

```python
# Create a new Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(getattr(s, 'name'))       # Output: 'GOOG'

# Set an attribute
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Check if an attribute exists
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Delete an attribute
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

当你需要动态处理属性时，这些函数特别有用。你可以使用变量名，而不是硬编码的属性名。例如，如果你有一个变量存储了属性名，你可以将该变量传递给这些函数，以对相应的属性执行操作。这让你的代码更具灵活性，特别是在以更动态的方式处理不同的对象和属性时。
