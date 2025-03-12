# 创建你的第一个元类

现在，我们要创建自己的第一个元类。在开始编码之前，让我们先了解一下什么是元类。在 Python 中，元类是用于创建其他类的类，就像是类的蓝图。当你在 Python 中定义一个类时，Python 会使用一个元类来创建该类。默认情况下，Python 使用 `type` 元类。在这一步中，我们将定义一个自定义元类，它会打印出正在创建的类的相关信息。这将帮助我们理解元类在底层是如何工作的。

1. 在 WebIDE 中打开 VSCode，并在 `/home/labex/project` 目录下创建一个名为 `mymeta.py` 的新文件。我们将在这个文件中编写元类的代码。

2. 在文件中添加以下代码：

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

让我们来分析一下这段代码的作用：

- 首先，我们定义了一个名为 `mytype` 的新类，它继承自 `type`。由于 `type` 是 Python 中的默认元类，通过继承它，我们创建了自己的自定义元类。
- 接下来，我们重写了 `__new__` 方法。在 Python 中，`__new__` 方法是一个特殊方法，在创建新对象时会被调用。在元类的上下文中，它在创建新类时被调用。
- 在我们的 `__new__` 方法内部，我们打印了一些关于正在创建的类的信息，包括类名、基类和属性。之后，我们使用 `super().__new__(meta, name, bases, __dict__)` 调用父类的 `__new__` 方法。这一点很重要，因为它实际上创建了类。
- 最后，我们创建了一个名为 `myobject` 的基类，并指定它应该使用我们的自定义元类 `mytype`。

`__new__` 方法接受以下参数：

- `meta`：这指的是元类本身。在我们的例子中，它是 `mytype`。
- `name`：这是正在创建的类的名称。
- `bases`：这是一个包含新类所继承的基类的元组。
- `__dict__`：这是一个包含类属性的字典。

3. 按下 Ctrl+S 或点击“文件”>“保存”来保存文件。保存文件可确保你的代码被保留，并且稍后可以运行。
