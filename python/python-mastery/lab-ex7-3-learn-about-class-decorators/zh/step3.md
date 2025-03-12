# 通过继承应用装饰器

在步骤 2 中，我们创建了一个类装饰器来简化代码。类装饰器是一种特殊的函数，它接受一个类作为参数，并返回一个修改后的类。在 Python 中，它是一个很有用的工具，可以在不修改类的原始代码的情况下为其添加功能。然而，我们仍然需要显式地将 `@validate_attributes` 装饰器应用到每个类上。这意味着每次创建一个需要验证的新类时，都必须记得添加这个装饰器，这有点麻烦。

我们可以通过继承自动应用装饰器来进一步改进。继承是面向对象编程中的一个基本概念，子类可以从父类继承属性和方法。Python 3.6 引入了 `__init_subclass__` 方法，允许父类自定义子类的初始化。这意味着当创建子类时，父类可以对其执行一些操作。我们可以利用这个特性，自动将装饰器应用到任何继承自 `Structure` 的类上。

让我们来实现这个功能：

1. 打开 `structure.py` 文件：

```bash
code ~/project/structure.py
```

这里，我们使用 `code` 命令在代码编辑器中打开 `structure.py` 文件。这个文件包含 `Structure` 类的定义，我们将修改它以使用 `__init_subclass__` 方法。

2. 为 `Structure` 类添加 `__init_subclass__` 方法：

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

`__init_subclass__` 是一个类方法，这意味着它可以在类本身而不是类的实例上调用。当创建 `Structure` 的子类时，这个方法会自动被调用。在这个方法内部，我们对 `cls` 子类调用 `validate_attributes` 装饰器。这样，`Structure` 的每个子类都会自动具有验证行为。

3. 保存文件。

对 `structure.py` 文件进行修改后，我们需要保存它，以便应用这些更改。

4. 现在，让我们更新 `stock.py` 文件以利用这个新特性：

```bash
code ~/project/stock.py
```

我们打开 `stock.py` 文件进行修改。这个文件包含 `Stock` 类的定义，我们将让它继承自 `Structure` 类，以实现装饰器的自动应用。

5. 修改 `stock.py` 文件以移除显式的装饰器：

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

注意我们做了以下改动：

- 移除了 `validate_attributes` 导入，因为通过继承自动应用装饰器后，我们不再需要显式导入它。
- 移除了 `@validate_attributes` 装饰器，因为 `Structure` 类中的 `__init_subclass__` 方法会负责应用它。
- 现在代码仅依靠继承自 `Structure` 来获得验证行为。

6. 再次运行测试，验证一切仍然正常工作：

```bash
cd ~/project
python3 teststock.py
```

运行测试很重要，以确保我们的更改没有破坏任何功能。如果所有测试都通过，就意味着通过继承自动应用装饰器的功能正常工作。

你应该会看到所有测试都通过：

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

让我们再次测试 `Stock` 类，确保它按预期工作：

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

这个命令创建了一个 `Stock` 类的实例，并打印出它的表示形式和成本。如果输出符合预期，就意味着 `Stock` 类在自动应用装饰器的情况下正常工作。

输出：

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

这个实现更加简洁！通过使用 `__init_subclass__`，我们消除了显式应用装饰器的需要。任何继承自 `Structure` 的类都会自动获得验证行为。
