# 理解用于属性控制的 `__setattr__`

在 Python 中，有一些特殊方法可以让你自定义对象属性的访问和修改方式。其中一个重要的方法是 `__setattr__()`。每当你尝试为对象的属性赋值时，这个方法就会发挥作用。它让你能够对属性赋值过程进行精细控制。

## 什么是 `__setattr__`？

`__setattr__(self, name, value)` 方法充当所有属性赋值的拦截器。当你编写像 `obj.attr = value` 这样的简单赋值语句时，Python 并不会直接赋值。相反，它会在内部调用 `obj.__setattr__("attr", value)`。这种机制让你能够决定在属性赋值期间应该发生什么。

现在让我们来看一个实际的例子，展示如何使用 `__setattr__` 来限制可以在类上设置哪些属性。

### 步骤 1：创建一个新文件

首先，在 WebIDE 中打开一个新文件。你可以通过点击 “File” 菜单，然后选择 “New File” 来完成。将这个文件命名为 `restricted_stock.py`，并将其保存到 `/home/labex/project` 目录中。这个文件将包含我们使用 `__setattr__` 来控制属性赋值的类定义。

### 步骤 2：向 `restricted_stock.py` 添加代码

将以下代码添加到 `restricted_stock.py` 文件中。这段代码定义了一个 `RestrictedStock` 类。

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

在 `__init__` 方法中，我们用 `name`、`shares` 和 `price` 属性初始化对象。`__setattr__` 方法会检查正在赋值的属性名是否在允许的属性集合（`name`、`shares`、`price`）中。如果不在，它会引发一个 `AttributeError`。如果属性是允许的，它会使用父类的 `__setattr__` 方法来实际设置属性。

### 步骤 3：创建一个测试文件

创建一个名为 `test_restricted.py` 的新文件，并将以下代码添加到其中。这段代码将测试 `RestrictedStock` 类的功能。

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

在这段代码中，我们首先导入 `RestrictedStock` 类。然后创建该类的一个实例。我们测试访问现有属性、修改现有属性，最后，我们尝试设置一个无效属性，以查看 `__setattr__` 方法是否按预期工作。

### 步骤 4：运行测试文件

在 WebIDE 中打开一个终端，并执行以下命令来运行 `test_restricted.py` 文件：

```bash
cd /home/labex/project
python3 test_restricted.py
```

运行这些命令后，你应该会看到类似于以下的输出：

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## 工作原理

我们的 `RestrictedStock` 类中的 `__setattr__` 方法按以下步骤工作：

1. 它首先检查属性名是否在允许的集合（`name`、`shares`、`price`）中。
2. 如果属性名不在允许的集合中，它会引发一个 `AttributeError`。这可以防止赋值不需要的属性。
3. 如果属性是允许的，它会使用 `super().__setattr__()` 来实际设置属性。这确保了允许的属性能够正常进行属性赋值过程。

这种方法比我们在之前的例子中看到的 `__slots__` 更灵活。虽然 `__slots__` 可以优化内存使用并限制属性，但在处理继承时它有局限性，并且可能与其他 Python 特性冲突。我们的 `__setattr__` 方法在没有这些局限性的情况下，为我们提供了类似的属性赋值控制。
