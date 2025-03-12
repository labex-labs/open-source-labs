# 理解类初始化的问题

在编程领域，类是一个基本概念，它允许你创建自定义数据类型。在之前的练习中，你可能已经创建了一个 `Structure` 类。这个类是一个实用工具，可用于轻松定义数据结构。数据结构是一种组织和存储数据的方式，以便能够高效地访问和使用数据。`Structure` 类作为基类，会根据预定义的字段名列表来初始化属性。属性是属于对象的变量，而字段名则是我们赋予这些属性的名称。

让我们仔细看看 `Structure` 类的当前实现。为此，你需要在代码编辑器中打开 `structure.py` 文件。这个文件包含了 `Structure` 类的代码。以下是导航到项目目录并打开文件的命令：

```bash
cd ~/project
code structure.py
```

`Structure` 类为定义简单的数据结构提供了一个基本框架。当我们创建一个子类，如 `Stock` 类时，我们可以为该子类定义特定的字段。子类会继承其基类（在这种情况下是 `Structure` 类）的属性和方法。例如，在 `Stock` 类中，我们定义了字段 `name`、`shares` 和 `price`：

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
```

现在，让我们打开 `stock.py` 文件，看看 `Stock` 类在整个代码上下文中是如何实现的。这个文件可能包含使用 `Stock` 类并与之交互的代码。使用以下命令打开文件：

```bash
code stock.py
```

尽管使用 `Structure` 类及其子类的这种方法可行，但它有几个局限性。为了找出这些问题，我们将运行 Python 解释器，探索 `Stock` 类的行为。以下命令将导入 `Stock` 类并显示其帮助信息：

```bash
python3 -c "from stock import Stock; help(Stock)"
```

当你运行这个命令时，你会注意到帮助输出中显示的签名并不是很有用。它没有显示实际的参数名，如 `name`、`shares` 和 `price`，而只显示了 `*args`。这种缺乏清晰参数名的情况使得用户难以理解如何正确创建 `Stock` 类的实例。

让我们也尝试使用关键字参数来创建一个 `Stock` 实例。关键字参数允许你通过参数名来指定参数的值，这可以使代码更具可读性。运行以下命令：

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

你应该会得到如下错误信息：

```
TypeError: __init__() got an unexpected keyword argument 'name'
```

这个错误的出现是因为我们当前负责初始化 `Stock` 类对象的 `__init__` 方法不处理关键字参数。它只接受位置参数，这意味着你必须按照特定的顺序提供值，而不能使用参数名。这是我们在这个实验中想要修复的一个局限性。

在这个实验中，我们将探索不同的方法，使我们的 `Structure` 类更加灵活和用户友好。通过这样做，我们可以提高 `Stock` 类和 `Structure` 类的其他子类的可用性。
