# 创建你的第一个元类

创建一个名为 `mymeta.py` 的文件，并将以下代码放入其中（来自幻灯片）：

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("创建类 :", name)
        print("基类         :", bases)
        print("属性         :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

完成此操作后，定义一个从 `myobject` 继承而不是从 `object` 继承的类。例如：

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares -= nshares
```

尝试运行你的代码并创建 `Stock` 的实例。看看会发生什么。当定义 `Stock` 类时，你应该会看到 `mytype` 中的打印语句运行一次。

如果你从 `Stock` 继承会发生什么？

```python
class MyStock(Stock):
    pass
```

你应该仍然会看到你的元类在起作用。元类具有“粘性”，因为它们会应用于整个继承层次结构。

**讨论**

你为什么想要做这样的事情呢？元类的主要强大之处在于，它使程序员能够在类创建之前捕获有关类的详细信息。例如，在 `__new__()` 方法中，你会获得所有基本详细信息，包括类名、基类和方法数据。如果你检查这些数据，就可以执行各种类型的诊断检查。如果你更有冒险精神，还可以修改数据并更改类创建时放入类定义中的内容。不用说，这里有很多机会可以做出极其邪恶的事情。
