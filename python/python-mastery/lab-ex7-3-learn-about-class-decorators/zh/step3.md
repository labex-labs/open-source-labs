# 通过继承应用装饰器

在步骤 2 中，我们创建了一个类装饰器来简化我们的代码。类装饰器是一种特殊的函数，它接收一个类作为参数并返回一个修改后的类。它是 Python 中一个有用的工具，可以在不修改类原始代码的情况下为其添加功能。但是，我们仍然需要为每个类显式地应用 `@validate_attributes` 装饰器。这意味着每次我们创建一个需要验证的新类时，都必须记住添加这个装饰器，这可能有点麻烦。

我们可以通过继承自动应用装饰器来进一步改进这一点。继承是面向对象编程中的一个基本概念，子类可以继承父类的属性和方法。Python 的 `__init_subclass__` 方法在 Python 3.6 中引入，允许父类自定义子类的初始化。这意味着当子类被创建时，父类可以对其执行一些操作。我们可以利用这个特性自动将我们的装饰器应用于任何继承自 `Structure` 的类。

让我们来实现这一点：

1. 在你的编辑器中打开 `structure.py` 文件。此文件包含 `Structure` 类的定义，我们将修改它以使用 `__init_subclass__` 方法。

2. 将 `__init_subclass__` 方法添加到 `Structure` 类：

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

`__init_subclass__` 方法是一个类方法，这意味着它可以被类本身调用，而不是类的实例。当创建 `Structure` 的子类时，这个方法将被自动调用。在此方法中，我们对子类 `cls` 调用 `validate_attributes` 装饰器。这样，`Structure` 的每个子类都将自动获得验证行为。

3. 保存文件。

在修改 `structure.py` 文件后，我们需要保存它，以便应用更改。

4. 现在，让我们更新 `stock.py` 文件以利用这个新特性。在你的编辑器中打开 `stock.py` 文件进行修改。此文件包含 `Stock` 类的定义，我们将使其继承自 `Structure` 类以使用自动装饰器应用。

5. 修改 `stock.py` 文件以移除显式装饰器：

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

请注意我们所做的：

- 我们移除了 `validate_attributes` 的导入，因为我们不再需要显式导入它，装饰器将通过继承自动应用。
- 我们移除了 `@validate_attributes` 装饰器，因为 `Structure` 类中的 `__init_subclass__` 方法将负责应用它。
- 代码现在仅依赖于从 `Structure` 继承来获得验证行为。

6. 再次运行测试以验证一切是否仍然正常工作：

```bash
cd ~/project
python3 teststock.py
```

运行测试很重要，以确保我们的更改没有破坏任何东西。如果所有测试都通过，则意味着通过继承自动应用装饰器正在正常工作。

你应该会看到所有测试都通过：

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

让我们再次测试我们的 `Stock` 类，以确保它按预期工作：

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

此命令创建一个 `Stock` 类的实例并打印其表示形式和成本。如果输出符合预期，则表示 `Stock` 类通过自动装饰器应用正常工作。

输出：

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

这个实现更简洁了！通过使用 `__init_subclass__`，我们消除了显式应用装饰器的需要。任何继承自 `Structure` 的类都会自动获得验证行为。
