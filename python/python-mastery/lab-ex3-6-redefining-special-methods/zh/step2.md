# 使用 `__eq__` 使对象可比较

在 Python 中，当你使用 `==` 运算符比较两个对象时，Python 实际上会调用 `__eq__` 特殊方法。默认情况下，这个方法比较对象的标识，即检查它们是否存储在相同的内存地址，而不是比较它们的内容。

让我们来看一个例子。假设我们有一个 `Stock` 类，并且创建了两个具有相同值的 `Stock` 对象。然后我们尝试使用 `==` 运算符来比较它们。在 Python 解释器中，你可以这样做：

首先，在终端中运行以下命令启动 Python 解释器：

```bash
python3
```

然后，在 Python 解释器中执行以下代码：

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
False
```

如你所见，尽管两个 `Stock` 对象 `a` 和 `b` 的属性（`name`、`shares` 和 `price`）具有相同的值，但 Python 认为它们是不同的对象，因为它们存储在不同的内存位置。

为了解决这个问题，我们可以在 `Stock` 类中实现 `__eq__` 方法。每当对 `Stock` 类的对象使用 `==` 运算符时，就会调用这个方法。

现在，再次打开 `stock.py` 文件。在 `Stock` 类中，添加以下 `__eq__` 方法：

```python
def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, other.shares, other.price))
```

让我们来分析一下这个方法的作用：

1. 首先，它使用 `isinstance` 函数检查 `other` 对象是否是 `Stock` 类的实例。这很重要，因为我们只想将 `Stock` 对象与其他 `Stock` 对象进行比较。
2. 如果 `other` 是 `Stock` 对象，它会比较 `self` 对象和 `other` 对象的属性（`name`、`shares` 和 `price`）。
3. 只有当两个对象都是 `Stock` 实例且它们的属性完全相同时，它才会返回 `True`。

添加 `__eq__` 方法后，你完整的 `Stock` 类应该如下所示：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
```

现在，让我们测试改进后的 `Stock` 类。再次启动 Python 解释器：

```bash
python3
```

然后，在 Python 解释器中运行以下代码：

```python
>>> import stock
>>> a = stock.Stock('GOOG', 100, 490.1)
>>> b = stock.Stock('GOOG', 100, 490.1)
>>> a == b
True
>>> c = stock.Stock('GOOG', 200, 490.1)
>>> a == c
False
```

太棒了！现在我们的 `Stock` 对象可以根据其内容进行正确比较，而不是根据它们的内存地址。

`__eq__` 方法中的 `isinstance` 检查至关重要。它确保我们只比较 `Stock` 对象。如果没有这个检查，将 `Stock` 对象与非 `Stock` 对象进行比较可能会引发错误。

测试完成后，你可以通过运行以下命令退出 Python 解释器：

```python
>>> exit()
```
