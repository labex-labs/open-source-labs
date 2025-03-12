# 手动创建类

在 Python 编程中，类是一个基本概念，它允许你将数据和函数组合在一起。通常，我们使用标准的 Python 语法来定义类。例如，下面是一个简单的 `Stock` 类。这个类表示一支股票，具有 `name`、`shares` 和 `price` 等属性，并且有计算成本和卖出股票的方法。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

但你是否想过 Python 在幕后是如何实际创建类的呢？如果我们不想使用标准的类语法来创建这个类，该怎么办呢？在本节中，我们将探索 Python 类是如何在底层构建的。

## 启动 Python 交互式 shell

要开始手动创建类的实验，我们需要打开一个 Python 交互式 shell。这个 shell 允许我们逐行执行 Python 代码，非常适合学习和测试。

在 WebIDE 中打开一个终端，并通过输入以下命令启动 Python 交互式 shell。第一个命令 `cd ~/project` 将当前目录更改为项目目录，第二个命令 `python3` 启动 Python 3 交互式 shell。

```bash
cd ~/project
python3
```

## 将方法定义为普通函数

在手动创建类之前，我们需要定义将成为类一部分的方法。在 Python 中，方法只是与类关联的函数。因此，让我们将类中需要的方法定义为普通的 Python 函数。

```python
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares
```

这里，`__init__` 函数是 Python 类中的一个特殊方法。它被称为构造函数，用于在创建类的实例时初始化对象的属性。`cost` 方法计算股票的总成本，`sell` 方法减少股票的数量。

## 创建方法字典

现在我们已经将方法定义为普通函数，需要以一种 Python 在创建类时能够理解的方式来组织它们。我们通过创建一个包含类所有方法的字典来实现这一点。

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

在这个字典中，键是方法在类中使用的名称，值是我们之前定义的实际函数对象。

## 使用 `type()` 构造函数创建类

在 Python 中，`type()` 函数是一个内置函数，可用于在底层创建类。`type()` 函数接受三个参数：

1. 类的名称：这是一个字符串，表示我们要创建的类的名称。
2. 基类的元组：在 Python 中，类可以继承自其他类。这里，我们使用 `(object,)`，这意味着我们的类继承自基类 `object`，它是 Python 中所有类的基类。
3. 包含方法和属性的字典：这是我们之前创建的包含类所有方法的字典。

```python
Stock = type('Stock', (object,), methods)
```

这行代码使用 `type()` 函数创建了一个名为 `Stock` 的新类。该类继承自 `object` 类，并具有 `methods` 字典中定义的方法。

## 测试我们手动创建的类

现在我们已经手动创建了类，让我们测试一下，确保它能按预期工作。我们将创建新类的一个实例并调用其方法。

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

在第一行中，我们创建了一个 `Stock` 类的实例，股票名称为 `GOOG`，有 100 股，价格为 490.10。然后我们打印股票的名称，计算并打印成本，卖出 25 股，最后打印剩余的股票数量。

你应该会看到以下输出：

```
GOOG
49010.0
75
```

这个输出表明我们手动创建的类与使用标准 Python 语法创建的类的工作方式相同。这证明了类从根本上来说只是一个名称、一个基类元组以及一个包含方法和属性的字典。`type()` 函数只是从这些组件构建一个对象。

完成后退出 Python shell：

```python
exit()
```
