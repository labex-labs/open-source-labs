# 创建动态的 `__init__()` 方法

现在，我们将把所学的关于 `exec()` 函数的知识应用到一个实际的编程场景中。在 Python 里，`exec()` 函数允许你执行存储在字符串中的 Python 代码。在这一步，我们将修改 `Structure` 类，以动态创建一个 `__init__()` 方法。`__init__()` 方法是 Python 类中的一个特殊方法，当类的对象被实例化时会调用该方法。我们将基于 `_fields` 类变量来创建这个方法，该变量包含了类的字段名列表。

首先，让我们看一下现有的 `structure.py` 文件。这个文件包含了 `Structure` 类的当前实现，以及一个继承自它的 `Stock` 类。要查看文件内容，在 WebIDE 中使用以下命令打开它：

```bash
cat /home/labex/project/structure.py
```

在输出中，你会看到当前的实现采用手动方式处理对象的初始化。这意味着初始化对象属性的代码是显式编写的，而不是动态生成的。

现在，我们要修改 `Structure` 类。我们将添加一个 `create_init()` 类方法，该方法将动态生成 `__init__()` 方法。要进行这些更改，在 WebIDE 编辑器中打开 `structure.py` 文件，并按照以下步骤操作：

1. 从 `Structure` 类中移除现有的 `_init()` 和 `set_fields()` 方法。这些方法是手动初始化方式的一部分，由于我们要采用动态方式，所以不再需要它们。

2. 向 `Structure` 类添加 `create_init()` 类方法。以下是该方法的代码：

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

在这个方法中，我们首先创建一个字符串 `argstr`，它包含所有用逗号分隔的字段名。这个字符串将用作 `__init__()` 方法的参数列表。然后，我们将 `__init__()` 方法的代码创建为一个字符串。我们遍历字段名，并向代码中添加行，将每个参数赋值给相应的对象属性。之后，我们使用 `exec()` 函数执行代码，并将生成的函数存储在 `locs` 字典中。最后，我们使用 `setattr()` 函数将生成的函数设置为类的 `__init__()` 方法。

3. 修改 `Stock` 类以使用这种新方法：

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

在这里，我们为 `Stock` 类定义 `_fields`，然后调用 `create_init()` 方法为 `Stock` 类生成 `__init__()` 方法。

你完整的 `structure.py` 文件现在应该类似于以下内容：

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

现在，让我们测试我们的实现，确保它能正常工作。我们将运行单元测试文件，检查所有测试是否都通过。使用以下命令：

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

如果你的实现正确，你应该会看到所有测试都通过。这意味着动态生成的 `__init__()` 方法按预期工作。

你也可以在 Python 交互式环境中手动测试这个类。以下是具体操作方法：

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

在 Python 交互式环境中，我们首先从 `structure.py` 文件中导入 `Stock` 类。然后，我们创建一个 `Stock` 类的实例并打印它。我们还可以修改对象的 `shares` 属性。然而，当我们尝试设置一个不在 `_fields` 列表中的属性时，应该会得到一个 `AttributeError`。

恭喜你！你已经成功使用 `exec()` 函数基于类属性动态创建了一个 `__init__()` 方法。这种方法可以让你的代码更具灵活性，也更易于维护，尤其是在处理具有可变数量属性的类时。
