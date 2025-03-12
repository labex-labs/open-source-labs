# 使用 `locals()` 访问函数参数

在 Python 中，理解变量作用域至关重要。变量的作用域决定了它在代码中的可访问位置。Python 提供了一个内置函数 `locals()`，对于初学者理解作用域非常有用。`locals()` 函数会返回一个包含当前作用域中所有局部变量的字典。当你想要检查函数参数时，这会非常有用，因为它能让你清楚地看到代码特定部分中可用的变量。

让我们在 Python 解释器中进行一个简单的实验，看看它是如何工作的。首先，你需要导航到项目目录并启动 Python 解释器。你可以在终端中运行以下命令来完成：

```bash
cd ~/project
python3
```

进入 Python 交互式 shell 后，我们将定义一个 `Stock` 类。在 Python 中，类就像是创建对象的蓝图。在这个类中，我们将使用特殊的 `__init__` 方法。`__init__` 方法是 Python 中的构造函数，这意味着在创建类的对象时，它会自动被调用。在这个 `__init__` 方法内部，我们将使用 `locals()` 函数来打印所有局部变量。

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

现在，让我们创建这个 `Stock` 类的一个实例。实例是根据类蓝图创建的实际对象。我们将为 `name`、`shares` 和 `price` 参数传入一些值。

```python
s = Stock('GOOG', 100, 490.1)
```

当你运行这段代码时，你应该会看到类似以下的输出：

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

这个输出表明，`locals()` 为我们提供了一个包含 `__init__` 方法中所有局部变量的字典。`self` 引用是 Python 类中的一个特殊变量，它指向类的实例本身。其他变量是我们创建 `Stock` 对象时传入的参数值。

我们可以使用 `locals()` 的这个功能来自动初始化对象属性。属性是与对象关联的变量。让我们定义一个辅助函数并修改我们的 `Stock` 类。

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

`_init` 函数接受从 `locals()` 获得的局部变量字典。它首先使用 `pop` 方法从字典中移除 `self` 引用。然后，它遍历字典中剩余的键值对，并使用 `setattr` 函数将每个变量设置为对象的属性。

现在，让我们使用位置参数和关键字参数来测试这个实现。位置参数按照函数签名中定义的顺序传递，而关键字参数则指定参数名进行传递。

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

现在这两种方法都应该可行！`_init` 函数使我们能够无缝处理位置参数和关键字参数。它还保留了函数签名中的参数名，这使得 `help()` 输出更加有用。Python 中的 `help()` 函数提供有关函数、类和模块的信息，完整的参数名会让这些信息更有意义。

当你完成实验后，你可以运行以下命令退出 Python 解释器：

```python
exit()
```
