# 创建基本的可调用对象

在 Python 中，可调用对象是一种可以像函数一样使用的对象。你可以把它想象成一个在后面加上括号就能“调用”的东西，就像调用普通函数一样。要让 Python 中的类表现得像可调用对象，我们需要实现一个名为 `__call__` 的特殊方法。当你使用带括号的对象时，这个方法会自动被调用，就像调用函数一样。

让我们从修改 `validate.py` 文件开始。我们将在这个文件中添加一个名为 `ValidatedFunction` 的新类，这个类将作为我们的可调用对象。要在代码编辑器中打开该文件，请在终端中运行以下命令：

```bash
code /home/labex/project/validate.py
```

文件打开后，滚动到文件末尾并添加以下代码：

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

让我们来分析一下这段代码的作用。`ValidatedFunction` 类有一个 `__init__` 方法，它是构造函数。当你创建这个类的实例时，需要传入一个函数。这个函数随后会作为实例的一个属性存储起来，属性名为 `self.func`。

`__call__` 方法是使这个类可调用的关键部分。当你调用 `ValidatedFunction` 类的实例时，`__call__` 方法会被执行。以下是它的具体执行步骤：

1. 它会打印一条消息，告诉你正在调用哪个函数。这对于调试和理解程序运行情况很有帮助。
2. 它会使用你调用实例时传入的参数来调用存储在 `self.func` 中的函数。`*args` 和 `**kwargs` 允许你传入任意数量的位置参数和关键字参数。
3. 它会返回函数调用的结果。

现在，让我们来测试这个 `ValidatedFunction` 类。我们将创建一个名为 `test_callable.py` 的新文件来编写测试代码。要在代码编辑器中打开这个新文件，请运行以下命令：

```bash
code /home/labex/project/test_callable.py
```

在 `test_callable.py` 文件中添加以下代码：

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

在这段代码中，我们首先从 `validate.py` 文件中导入 `ValidatedFunction` 类。然后定义了一个简单的函数 `add`，它接受两个数字并返回它们的和。

我们创建了 `ValidatedFunction` 类的一个实例，并将 `add` 函数作为参数传入。这样就把 `add` 函数“包装”在了 `ValidatedFunction` 实例中。

然后我们两次调用这个包装后的函数，一次传入参数 `2` 和 `3`，另一次传入 `10` 和 `20`。每次调用包装后的函数时，`ValidatedFunction` 类的 `__call__` 方法都会被调用，进而调用原始的 `add` 函数。

要运行测试代码，请在终端中执行以下命令：

```bash
python3 /home/labex/project/test_callable.py
```

你应该会看到类似以下的输出：

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

这个输出表明我们的可调用对象正在按预期工作。当我们调用 `validated_add(2, 3)` 时，实际上是在调用 `ValidatedFunction` 类的 `__call__` 方法，该方法随后调用原始的 `add` 函数。

目前，我们的 `ValidatedFunction` 类只是打印一条消息并将调用传递给原始函数。在下一步中，我们将改进这个类，使其能够根据函数的注解进行类型验证。
