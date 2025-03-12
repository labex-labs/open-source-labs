# 为类添加迭代功能以增强其特性

现在，我们已经让 `Structure` 类及其子类支持迭代了。迭代是 Python 中一个强大的概念，它允许你逐个遍历一组对象。当一个类支持迭代时，它会变得更加灵活，并且可以与许多 Python 内置特性协同工作。让我们来探索一下这种迭代支持如何在 Python 中实现许多强大的功能。

## 利用迭代进行序列转换

在 Python 中，有像 `list()` 和 `tuple()` 这样的内置函数。这些函数非常有用，因为它们可以接受任何可迭代对象作为输入。可迭代对象是指你可以进行遍历的对象，比如列表、元组，现在还包括我们的 `Structure` 类实例。由于我们的 `Structure` 类现在支持迭代，我们可以轻松地将其实例转换为列表或元组。

1. 让我们用一个 `Stock` 实例来尝试这些操作。`Stock` 类是 `Structure` 类的子类。在终端中运行以下命令：

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('As list:', list(s)); print('As tuple:', tuple(s))"
```

这个命令首先导入 `Stock` 类，创建一个它的实例，然后分别使用 `list()` 和 `tuple()` 函数将该实例转换为列表和元组。输出将显示该实例以列表和元组形式表示的结果：

```
As list: ['GOOG', 100, 490.1]
As tuple: ('GOOG', 100, 490.1)
```

## 解包

Python 有一个非常有用的特性叫做解包（Unpacking）。解包允许你将一个可迭代对象的元素一次性分配给各个变量。由于我们的 `Stock` 实例是可迭代的，我们可以对其使用解包特性。

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); name, shares, price = s; print(f'Name: {name}, Shares: {shares}, Price: {price}')"
```

在这段代码中，我们创建了一个 `Stock` 实例，然后将其元素解包到三个变量中：`name`、`shares` 和 `price`。接着我们打印这些变量。输出将显示这些变量的值：

```
Name: GOOG, Shares: 100, Price: 490.1
```

## 添加比较功能

当一个类支持迭代时，实现比较操作会变得更加容易。比较操作用于检查两个对象是否相等。让我们为 `Structure` 类添加一个 `__eq__()` 方法来比较实例。

1. 再次打开 `structure.py` 文件。`__eq__()` 方法是 Python 中的一个特殊方法，当你使用 `==` 运算符比较两个对象时会调用该方法。在 `structure.py` 文件的 `Structure` 类中添加以下代码：

```python
def __eq__(self, other):
    return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

这个方法首先使用 `isinstance()` 函数检查 `other` 对象是否与 `self` 是同一类的实例。然后它将 `self` 和 `other` 都转换为元组，并检查这些元组是否相等。

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

    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
```

2. 添加 `__eq__()` 方法后，保存 `structure.py` 文件。

3. 让我们测试一下比较功能。在终端中运行以下命令：

```bash
python3 -c "from stock import Stock; a = Stock('GOOG', 100, 490.1); b = Stock('GOOG', 100, 490.1); c = Stock('AAPL', 200, 123.4); print(f'a == b: {a == b}'); print(f'a == c: {a == c}')"
```

这段代码创建了三个 `Stock` 实例：`a`、`b` 和 `c`。然后使用 `==` 运算符将 `a` 与 `b` 以及 `a` 与 `c` 进行比较。输出将显示这些比较的结果：

```
a == b: True
a == c: False
```

4. 现在，为了确保一切正常工作，我们需要运行单元测试。单元测试是一组代码，用于检查程序的不同部分是否按预期工作。在终端中运行以下命令：

```bash
python3 teststock.py
```

如果一切正常，你应该会看到表明测试通过的输出：

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

通过仅添加两个简单的方法（`__iter__()` 和 `__eq__()`），我们显著增强了 `Structure` 类的功能，使其更具 Python 风格且更易于使用。
