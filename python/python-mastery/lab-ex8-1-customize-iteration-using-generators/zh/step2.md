# 为自定义类添加迭代功能

既然你已经掌握了生成器的基础知识，我们将使用它们为自定义类添加迭代功能。在 Python 中，如果你想让一个类可迭代，就需要实现 `__iter__()` 特殊方法。一个可迭代的类允许你遍历其元素，就像你可以遍历列表或元组一样。这是一个强大的特性，它使你的自定义类更加灵活且易于使用。

## 理解 `__iter__()` 方法

`__iter__()` 方法是使类可迭代的关键部分。它应该返回一个迭代器对象。迭代器是一个可以被迭代（遍历）的对象。实现这一点的一个简单有效的方法是将 `__iter__()` 定义为一个生成器函数。生成器函数使用 `yield` 关键字一次产生一个值的序列。每次遇到 `yield` 语句时，函数会暂停并返回该值。下次调用迭代器时，函数会从上次暂停的地方继续执行。

## 修改 `Structure` 类

在本次实验的设置中，我们提供了一个基础的 `Structure` 类。其他类（如 `Stock`）可以继承这个 `Structure` 类。继承是创建一个新类的方式，新类可以继承现有类的属性和方法。通过为 `Structure` 类添加 `__iter__()` 方法，我们可以使它的所有子类都可迭代。这意味着任何继承自 `Structure` 的类都将自动具备可遍历的能力。

1. 在 WebIDE 中打开 `structure.py` 文件：

```bash
cd ~/project
```

这个命令将当前工作目录更改为 `project` 目录，`structure.py` 文件就位于该目录中。你需要处于正确的目录才能访问和修改该文件。

2. 查看 `Structure` 类的当前实现：

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

`Structure` 类有一个 `_fields` 列表，用于存储属性的名称。`__init__()` 方法是类的构造函数。它通过检查传入的参数数量是否等于字段数量来初始化对象的属性。如果不相等，它会引发一个 `TypeError`。否则，它使用 `setattr()` 函数设置属性。

3. 添加一个 `__iter__()` 方法，按顺序产生每个属性的值：

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

这个 `__iter__()` 方法是一个生成器函数。它遍历 `_fields` 列表，并使用 `getattr()` 函数获取每个属性的值。然后，`yield` 关键字逐个返回这些值。

现在完整的 `structure.py` 文件应该如下所示：

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
```

这个更新后的 `Structure` 类现在有了 `__iter__()` 方法，这使得它及其子类都可迭代。

4. 保存文件。
   对 `structure.py` 文件进行更改后，你需要保存它，以便应用这些更改。

5. 现在，让我们通过创建一个 `Stock` 实例并对其进行迭代来测试迭代功能：

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

这个命令创建了一个 `Stock` 类的实例，该类继承自 `Structure` 类。然后，它使用列表推导式对该实例进行迭代，并打印每个值。

你应该会看到如下输出：

```
Iterating over Stock:
GOOG
100
490.1
```

现在，任何继承自 `Structure` 的类都将自动可迭代，并且迭代将按照 `_fields` 列表定义的顺序产生属性值。这意味着你可以轻松地遍历 `Structure` 任何子类的属性，而无需为迭代编写额外的代码。
