# 理解描述符协议

在这一步中，我们将通过创建一个简单的 `Stock` 类来学习 Python 中描述符的工作原理。Python 中的描述符是一项强大的特性，它允许你自定义属性的访问、设置和删除方式。描述符协议由三个特殊方法组成：`__get__()`、`__set__()` 和 `__delete__()`。这些方法分别定义了在访问、赋值或删除属性时描述符的行为。

首先，你需要在项目目录中创建一个名为 `stock.py` 的新文件。这个文件将包含我们的 `Stock` 类。以下是你应该放在 `stock.py` 文件中的代码：

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

在这个 `Stock` 类中，我们使用 `property` 装饰器为 `name`、`shares` 和 `price` 属性定义了 getter 和 setter 方法。这些 getter 和 setter 方法充当描述符，这意味着它们控制着这些属性的访问和设置方式。例如，setter 方法会验证输入值，以确保它们的类型正确且在可接受的范围内。

现在我们的 `stock.py` 文件已经准备好了，让我们打开一个 Python 交互式 shell 来试验 `Stock` 类，看看描述符是如何实际工作的。为此，请打开你的终端并运行以下命令：

```bash
cd ~/project
python3 -i stock.py
```

`python3` 命令中的 `-i` 选项告诉 Python 在执行 `stock.py` 文件后启动一个交互式 shell。这样，我们就可以直接与刚刚定义的 `Stock` 类进行交互。

在 Python 交互式 shell 中，让我们创建一个股票对象并尝试访问它的属性。你可以这样做：

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

当你访问 `s` 对象的 `name` 和 `shares` 属性时，Python 实际上是在幕后调用描述符的 `__get__` 方法。我们类中的 `property` 装饰器是使用描述符实现的，这意味着它们以可控的方式处理属性的访问和赋值。

让我们仔细查看类字典，以查看描述符对象。类字典包含类中定义的所有属性和方法。你可以使用以下代码查看类字典的键：

```python
Stock.__dict__.keys()
```

你应该会看到类似于以下的输出：

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

键 `name`、`shares` 和 `price` 表示由 `property` 装饰器创建的描述符对象。

现在，让我们通过手动调用描述符的方法来研究描述符是如何工作的。我们将以 `shares` 描述符为例。你可以这样做：

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

当你访问像 `s.shares` 这样的属性时，Python 会调用描述符的 `__get__` 方法来获取值。当你给属性赋值，如 `s.shares = 75` 时，Python 会调用描述符的 `__set__` 方法。然后，描述符可以验证数据，如果输入值无效则会引发错误。

当你完成对 `Stock` 类和描述符的实验后，你可以通过运行以下命令退出 Python 交互式 shell：

```python
exit()
```
