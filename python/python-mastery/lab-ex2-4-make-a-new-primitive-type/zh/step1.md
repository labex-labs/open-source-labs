# 创建基本的 MutInt 类

让我们从为可变整数类型创建一个基本类开始。在编程中，类就像是创建对象的蓝图。在这一步，我们将为新的原始类型奠定基础。原始类型是编程语言提供的基本数据类型，在这里我们要创建自己的自定义类型。

1. 打开 WebIDE 并导航到 `/home/labex/project` 目录。WebIDE 是一个集成开发环境，你可以在其中编写、编辑和运行代码。导航到这个目录可确保你所有的文件都组织在一处，并且能相互正确交互。

2. 打开在设置步骤中为你创建的 `mutint.py` 文件。这个文件将是我们 `MutInt` 类定义的所在之处。

3. 添加以下代码来定义一个基本的 `MutInt` 类：

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value
```

`__slots__` 属性用于定义这个类可以拥有的属性。属性就像是属于类对象的变量。通过使用 `__slots__`，我们告诉 Python 使用更节省内存的方式来存储属性。在这种情况下，我们的 `MutInt` 类将只有一个名为 `value` 的属性。这意味着 `MutInt` 类的每个对象只能保存一个数据，即整数值。

`__init__` 方法是我们类的构造函数。构造函数是一种特殊的方法，在创建类的对象时会被调用。它接受一个值参数，并将其存储在实例的 `value` 属性中。实例是根据类蓝图创建的单个对象。

让我们通过创建一个 Python 脚本来使用这个类来测试它：

4. 在同一目录下创建一个名为 `test_mutint.py` 的新文件：

```python
# test_mutint.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# Modify the value (demonstrating mutability)
a.value = 42
print(f"Modified value to: {a.value}")

# Try adding (this will fail)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

在这个测试脚本中，我们首先从 `mutint.py` 文件中导入 `MutInt` 类。然后我们创建一个初始值为 3 的 `MutInt` 类对象。我们打印初始值，然后将其修改为 42 并打印新值。最后，我们尝试将 10 加到 `MutInt` 对象上，这会导致错误，因为我们的类还不支持加法运算。

5. 在终端中执行以下命令来运行测试脚本：

```bash
python3 /home/labex/project/test_mutint.py
```

终端是一个命令行界面，你可以在其中运行各种命令来与系统和代码进行交互。运行这个命令将执行 `test_mutint.py` 脚本。

你应该会看到类似以下的输出：

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

我们的 `MutInt` 类成功地存储和更新了一个值。然而，它有几个局限性：

- 打印时显示效果不佳
- 不支持加法等数学运算
- 不支持比较操作
- 不支持类型转换

在接下来的步骤中，我们将逐一解决这些局限性，使我们的 `MutInt` 类更像一个真正的原始类型。
