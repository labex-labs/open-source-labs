# 创建类型化结构辅助函数

在这一步中，我们将构建一个更实用的示例。我们将实现一个函数，用于创建带有类型验证的类。类型验证至关重要，因为它能确保分配给类属性的数据满足特定标准，比如属于特定的数据类型或处于特定的范围内。这有助于尽早捕获错误，使我们的代码更加健壮。

## 理解 `Structure` 类

首先，你需要在 WebIDE 编辑器中打开 `structure.py` 文件。该文件包含一个基本的 `Structure` 类。这个类为初始化和表示结构化对象提供了基本功能。初始化指的是用提供的数据设置对象，而表示则是指当我们打印对象时它的显示方式。

要打开文件，你可以在终端中使用以下命令：

```bash
cd ~/project
```

运行此命令后，你将进入 `structure.py` 文件所在的正确目录。打开文件后，你会看到基本的 `Structure` 类。我们的目标是扩展这个类以支持类型验证。

## 实现 `typed_structure` 函数

现在，让我们将 `typed_structure` 函数添加到 `structure.py` 文件中。这个函数将创建一个新类，该类继承自 `Structure` 类并包含指定的验证器。继承意味着新类将拥有 `Structure` 类的所有功能，并且还可以添加自己的特性。验证器用于检查分配给类属性的值是否有效。

以下是 `typed_structure` 函数的代码：

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

`clsname` 参数是我们要给新类起的名称。`validators` 参数是一个字典，其中键是属性名，值是验证器对象。`type()` 函数用于动态创建新类。它接受三个参数：类名、基类元组（在这种情况下，只有 `Structure` 类）以及类属性字典（即验证器）。

添加此函数后，你的 `structure.py` 文件应如下所示：

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## 测试 `typed_structure` 函数

让我们使用 `validate.py` 文件中的验证器来测试我们的 `typed_structure` 函数。这些验证器用于检查分配给类属性的值是否为正确的类型并满足其他标准。

首先，打开一个 Python 交互式 shell。你可以在终端中使用以下命令：

```bash
cd ~/project
python3
```

第一个命令将你带到正确的目录，第二个命令启动 Python 交互式 shell。

现在，导入必要的组件并创建一个类型化结构：

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

我们从 `validate.py` 文件中导入 `String`、`PositiveInteger` 和 `PositiveFloat` 验证器。然后使用 `typed_structure` 函数创建一个带有类型验证的 `Stock` 类。我们创建 `Stock` 类的一个实例并通过打印其属性来测试它。最后，我们尝试创建一个无效的股票实例来测试验证功能。

你应该会看到类似于以下的输出：

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

测试完成后，退出 Python shell：

```python
exit()
```

这个示例展示了我们如何使用 `type()` 函数创建具有特定验证规则的自定义类。这种方法非常强大，因为它允许我们以编程方式生成类，这可以节省大量时间并使我们的代码更加灵活。
