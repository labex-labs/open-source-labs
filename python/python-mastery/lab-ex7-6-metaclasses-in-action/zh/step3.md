# 创建 StructureMeta 元类

现在，让我们来谈谈接下来要做的事情。我们已经找到了收集所有验证器类型的方法。下一步是创建一个元类。但元类究竟是什么呢？在 Python 中，元类是一种特殊的类。它的实例本身就是类。这意味着元类可以控制类的创建方式，还能管理定义类属性的命名空间。

在我们的场景中，我们希望创建一个元类，以便在定义 `Structure` 子类时可以直接使用验证器类型，而无需每次都显式导入这些验证器类型。

让我们再次打开 `structure.py` 文件。你可以使用以下命令打开它：

```bash
code structure.py
```

文件打开后，我们需要在 `Structure` 类定义之前的文件顶部添加一些代码，这些代码将用于定义我们的元类。

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

现在我们已经定义了元类，需要修改 `Structure` 类以使用它。这样，任何继承自 `Structure` 的类都能受益于元类的功能。

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

让我们详细分析一下这段代码的作用：

1. `__prepare__()` 方法是 Python 中的一个特殊方法，它在类创建之前被调用，其作用是准备定义类属性的命名空间。我们在这里使用了 `ChainMap`，它是一个很有用的工具，可以创建一个分层字典。在我们的例子中，它包含了我们的验证器类型，使得这些类型在类的命名空间中可以被访问。

2. `__new__()` 方法负责创建新的类。我们只提取了局部命名空间，也就是 `ChainMap` 中的第一个字典。我们舍弃了验证器字典，因为我们已经让验证器类型在命名空间中可用了。

通过这样的设置，任何继承自 `Structure` 的类都可以访问所有的验证器类型，而无需显式导入它们。

现在，让我们测试一下我们的实现。我们将使用增强后的 `Structure` 基类创建一个 `Stock` 类。

```bash
cat > stock.py << EOF
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
EOF
```

如果我们的元类正常工作，我们应该能够在不导入验证器类型的情况下定义 `Stock` 类。这是因为元类已经让这些类型在命名空间中可用了。
