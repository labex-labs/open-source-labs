# 理解问题

在开始探索元类之前，理解我们要解决的问题很重要。在编程中，我们经常需要为属性创建具有特定类型的结构。在之前的工作中，我们开发了一个用于类型检查结构的系统。该系统允许我们定义类，其中每个属性都有特定的类型，并且分配给这些属性的值会根据该类型进行验证。

以下是我们如何使用这个系统创建 `Stock` 类的示例：

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

在这段代码中，我们首先从 `validate` 模块导入验证器类型（`String`、`PositiveInteger`、`PositiveFloat`），并从 `structure` 模块导入 `Structure` 类。然后我们定义了 `Stock` 类，它继承自 `Structure`。在 `Stock` 类内部，我们定义了具有特定验证器类型的属性。例如，`name` 属性必须是字符串，`shares` 必须是正整数，`price` 必须是正浮点数。

然而，这种方法存在一个问题。我们需要在文件顶部导入所有的验证器类型。在实际场景中，随着我们添加越来越多的验证器类型，这些导入语句会变得很长且难以管理。这可能会导致我们使用 `from validate import *`，但这通常被认为是一种不良实践，因为它可能会导致命名冲突并使代码的可读性降低。

为了了解我们的起点，让我们看一下 `Structure` 类。你需要在编辑器中打开 `structure.py` 文件并查看其内容。这将帮助你了解在添加元类功能之前，基本的结构处理是如何实现的。

```bash
code structure.py
```

当你打开文件时，你会看到 `Structure` 类的基本实现。这个类负责处理属性初始化，但目前还没有任何元类功能。

接下来，让我们检查验证器类。这些类在 `validate.py` 文件中定义。它们已经具备描述符（descriptor）功能，这意味着它们可以控制属性的访问和设置方式。但我们需要对它们进行增强，以解决前面讨论的导入问题。

```bash
code validate.py
```

通过查看这些验证器类，你将更好地理解验证过程是如何工作的，以及我们需要做出哪些更改来改进代码。
