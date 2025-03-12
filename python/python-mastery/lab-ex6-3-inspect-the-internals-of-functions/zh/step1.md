# 探究函数属性

在 Python 中，函数被视为一等对象（first-class objects）。这是什么意思呢？这就好比在现实世界中有不同类型的对象，比如一本书或一支笔。在 Python 里，函数也是对象，并且和其他对象一样，它们有自己的一组属性。这些属性可以为我们提供很多关于函数的有用信息，比如函数的名称、定义位置以及实现方式。

让我们通过打开一个 Python 交互式 shell 来开始探究。这个 shell 就像一个游乐场，你可以立即在其中编写和运行 Python 代码。为此，你首先要导航到项目目录，然后启动 Python 解释器。以下是在终端中要运行的命令：

```bash
cd ~/project
python3
```

现在你已经进入了 Python 交互式 shell，让我们定义一个简单的函数。这个函数将接受两个数字并将它们相加。以下是定义该函数的方法：

```python
def add(x, y):
    'Adds two things'
    return x + y
```

在这段代码中，你创建了一个名为 `add` 的函数。它接受两个参数 `x` 和 `y`，并返回它们的和。字符串 `'Adds two things'` 被称为文档字符串（docstring），用于记录函数的功能。

## 使用 `dir()` 检查函数属性

在 Python 中，`dir()` 函数是一个非常实用的工具。它可以用来获取对象拥有的所有属性和方法的列表。让我们用它来看看 `add` 函数有哪些属性。在 Python 交互式 shell 中运行以下代码：

```python
dir(add)
```

当你运行这段代码时，你会看到一长串属性。以下是输出可能的样子：

```
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

这个列表展示了与 `add` 函数相关的所有属性和方法。

## 访问基本的函数信息

现在，让我们仔细看看一些基本的函数属性。这些属性可以告诉我们关于函数的重要信息。在 Python 交互式 shell 中运行以下代码：

```python
print(add.__name__)
print(add.__module__)
print(add.__doc__)
```

当你运行这段代码时，你会看到以下输出：

```
add
__main__
Adds two things
```

让我们来理解一下这些属性的含义：

- `__name__`：这个属性给出了函数的名称。在我们的例子中，函数名为 `add`。
- `__module__`：它告诉我们函数定义所在的模块。当你在交互式 shell 中运行代码时，模块通常是 `__main__`。
- `__doc__`：这是函数的文档字符串（docstring），它简要描述了函数的功能。

## 检查函数代码

函数的 `__code__` 属性非常有趣。它包含了关于函数实现方式的信息，包括字节码（bytecode）和其他细节。让我们看看能从它那里了解到什么。在 Python 交互式 shell 中运行以下代码：

```python
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)
```

输出将是：

```
('x', 'y')
2
```

这些属性告诉我们以下信息：

- `co_varnames`：它是一个元组，包含函数使用的所有局部变量的名称。在我们的 `add` 函数中，局部变量是 `x` 和 `y`。
- `co_argcount`：这个属性告诉我们函数期望的参数数量。我们的 `add` 函数期望两个参数，所以值为 2。

如果你想进一步探究 `__code__` 对象的更多属性，可以再次使用 `dir()` 函数。运行以下代码：

```python
dir(add.__code__)
```

这将显示代码对象的所有属性，其中包含了关于函数实现的底层细节。
