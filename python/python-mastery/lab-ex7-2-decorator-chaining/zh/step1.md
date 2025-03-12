# 在装饰器中保留函数元数据

在 Python 中，装饰器是一个强大的工具，可用于修改函数的行为。然而，当你使用装饰器包装函数时，会出现一个小问题。默认情况下，原始函数的元数据（如函数名、文档字符串（docstring）和注解）会丢失。元数据很重要，因为它有助于内省（检查代码结构）和生成文档。让我们先来验证这个问题。

在 WebIDE 中打开你的终端。我们将运行一些 Python 命令，看看使用装饰器时会发生什么。以下命令将创建一个用装饰器包装的简单函数 `add`，然后打印该函数及其文档字符串。

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

当你运行这些命令时，你会看到类似如下的输出：

```
<function wrapper at 0x...>
None
```

注意，函数名显示为 `wrapper`，而不是 `add`。并且文档字符串本应是 `'Adds two things'`，现在却为 `None`。当你使用依赖这些元数据的工具（如内省工具或文档生成器）时，这可能会成为一个大问题。

## 使用 `functools.wraps` 解决问题

Python 的 `functools` 模块可以解决这个问题。它提供了一个 `wraps` 装饰器，可帮助我们保留函数元数据。让我们看看如何修改 `logged` 装饰器以使用 `wraps`。

1. 首先，在 WebIDE 中打开 `logcall.py` 文件。你可以在终端中使用以下命令导航到项目目录：

```bash
cd ~/project
```

2. 现在，用以下代码更新 `logcall.py` 中的 `logged` 装饰器。`@wraps(func)` 装饰器是关键所在。它将原始函数 `func` 的所有元数据复制到包装函数中。

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. `@wraps(func)` 装饰器起着重要作用。它从原始函数 `func` 中获取所有元数据（如名称、文档字符串和注解），并将其附加到 `wrapper` 函数上。这样，当我们使用被装饰的函数时，它将拥有正确的元数据。

4. 让我们测试改进后的装饰器。在终端中运行以下命令：

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

现在你应该会看到：

```
<function add at 0x...>
Adds two things
```

太棒了！函数名和文档字符串都被保留下来了。这意味着我们的装饰器现在按预期工作，原始函数的元数据完好无损。

## 修复 `validate.py` 中的装饰器

现在，让我们对 `validate.py` 中的 `validated` 装饰器应用同样的修复。这个装饰器用于根据函数的注解验证函数参数和返回值的类型。

1. 在 WebIDE 中打开 `validate.py` 文件。

2. 用 `@wraps` 装饰器更新 `validated` 装饰器。以下代码展示了如何操作。在 `validated` 装饰器内部的 `wrapper` 函数上添加 `@wraps(func)` 装饰器，以保留元数据。

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper
```

3. 让我们测试一下，看看 `validated` 装饰器现在是否保留了元数据。在终端中运行以下命令：

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

你应该会看到：

```
<function multiply at 0......>
Multiplies two integers
```

现在，`logged` 和 `validated` 这两个装饰器都能正确保留它们所装饰函数的元数据。这确保了你在使用这些装饰器时，函数仍然会保留其原始名称、文档字符串和注解，这对代码的可读性和可维护性非常有用。
