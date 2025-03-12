# 使用函数注解实现类型验证

在 Python 中，你可以为函数参数添加类型注解。这些注解用于表明参数和函数返回值的预期数据类型。默认情况下，它们不会在运行时强制检查类型，但可用于验证目的。

让我们看一个例子：

```python
def add(x: int, y: int) -> int:
    return x + y
```

在这段代码中，`x: int` 和 `y: int` 表明参数 `x` 和 `y` 应该是整数。末尾的 `-> int` 表示函数 `add` 返回一个整数。这些类型注解存储在函数的 `__annotations__` 属性中，这是一个将参数名映射到其注解类型的字典。

现在，我们要增强 `ValidatedFunction` 类，使其利用这些类型注解进行验证。为此，我们需要使用 Python 的 `inspect` 模块。该模块提供了一些有用的函数，可用于获取关于实时对象（如模块、类、方法、函数等）的信息。在我们的例子中，我们将使用它来将函数参数与对应的参数名进行匹配。

首先，我们需要修改 `validate.py` 文件中的 `ValidatedFunction` 类。你可以使用以下命令打开该文件：

```bash
code /home/labex/project/validate.py
```

将现有的 `ValidatedFunction` 类替换为以下改进版本：

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

这个改进版本的类的功能如下：

1. 使用 `inspect.signature()` 获取函数参数的信息，如参数名、默认值和注解类型。
2. 使用签名的 `bind()` 方法将提供的参数与对应的参数名进行匹配。这有助于我们将每个参数与函数中正确的参数关联起来。
3. 检查每个参数是否符合其类型注解（如果存在）。如果找到注解，则从注解中获取验证器类，并使用 `check()` 方法进行验证。
4. 最后，使用经过验证的参数调用原始函数。

现在，让我们使用一些在类型注解中使用了我们的验证器类的函数来测试这个增强后的 `ValidatedFunction` 类。使用以下命令打开 `test_validation.py` 文件：

```bash
code /home/labex/project/test_validation.py
```

在文件中添加以下代码：

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

在这段代码中，我们定义了一个 `greet` 函数，其类型注解为 `name: String` 和 `times: Integer`。这意味着 `name` 参数应该使用 `String` 类进行验证，`times` 参数应该使用 `Integer` 类进行验证。然后，我们使用 `ValidatedFunction` 类包装 `greet` 函数，以启用类型验证。

我们进行了三个测试用例：一个有效调用、一个 `name` 参数类型错误的无效调用，以及一个 `times` 参数类型错误的无效调用。每个调用都包裹在 `try-except` 块中，以捕获验证过程中可能引发的任何 `TypeError` 异常。

要运行测试文件，请使用以下命令：

```bash
python3 /home/labex/project/test_validation.py
```

你应该会看到类似于以下的输出：

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

这个输出表明，我们的 `ValidatedFunction` 可调用对象现在能够根据函数注解执行类型验证。当我们传入错误类型的参数时，验证器类会检测到错误并引发 `TypeError`。这样，我们可以确保函数使用正确的数据类型进行调用，有助于防止错误并使我们的代码更加健壮。
