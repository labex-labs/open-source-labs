# 创建带参数的类型强制装饰器

在前面的步骤中，我们学习了 `@validated` 装饰器。这个装饰器用于在 Python 函数中强制实施类型注解。类型注解是一种指定函数参数和返回值预期类型的方式。现在，我们要更进一步。我们将创建一个更灵活的装饰器，它可以接受类型规范作为参数。这意味着我们可以更明确地为每个参数和返回值定义所需的类型。

## 理解目标

我们的目标是创建一个 `@enforce()` 装饰器。这个装饰器允许我们使用关键字参数指定类型约束。以下是它的工作示例：

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

在这个例子中，我们使用 `@enforce` 装饰器指定 `add` 函数的 `x` 和 `y` 参数应该是 `Integer` 类型，返回值也应该是 `Integer` 类型。这个装饰器的行为与我们之前的 `@validated` 装饰器类似，但它让我们对类型规范有更多的控制权。

## 创建 `enforce` 装饰器

1. 首先，在 WebIDE 中打开 `validate.py` 文件。我们将把新的装饰器添加到这个文件中。以下是我们要添加的代码：

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

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

让我们来分析一下这段代码的作用。`Integer` 类用于定义一个自定义类型。`validated` 装饰器根据函数的类型注解检查函数参数和返回值的类型。`enforce` 装饰器是我们正在创建的新装饰器。它接受关键字参数，这些参数指定了每个参数和返回值的类型。在 `enforce` 装饰器的 `wrapper` 函数内部，我们检查参数和返回值的类型是否与指定的类型匹配。如果不匹配，我们就抛出一个 `TypeError` 异常。

2. 现在，让我们测试一下新的 `@enforce` 装饰器。我们将运行一些测试用例，看看它是否按预期工作。以下是运行测试的代码：

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

在这段测试代码中，我们首先使用 `@enforce` 装饰器定义了一个 `add` 函数。然后，我们用有效的参数调用 `add` 函数，这应该能正常工作而不会出错。接下来，我们用一个无效的参数调用 `add` 函数，这应该会抛出一个 `TypeError` 异常。最后，我们定义了一个 `bad_add` 函数，它返回一个错误类型的值，这也应该抛出一个 `TypeError` 异常。

当你运行这段测试代码时，你应该会看到类似以下的输出：

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

这个输出表明我们的 `@enforce` 装饰器工作正常。当参数或返回值的类型与指定的类型不匹配时，它会抛出一个 `TypeError` 异常。

## 比较两种方法

`@validated` 和 `@enforce` 装饰器都实现了强制类型约束的目标，但它们的实现方式不同。

1. `@validated` 装饰器使用 Python 的内置类型注解。以下是一个示例：

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   使用这种方法，我们在函数定义中直接使用类型注解指定类型。这是 Python 的内置特性，在集成开发环境（IDE）中提供了更好的支持。IDE 可以使用这些类型注解来提供代码补全、类型检查和其他有用的功能。

2. 另一方面，`@enforce` 装饰器使用关键字参数来指定类型。以下是一个示例：

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   这种方法更明确，因为我们直接将类型规范作为参数传递给装饰器。当与依赖其他注解系统的库一起使用时，这种方法很有用。

每种方法都有其优点。类型注解是 Python 的原生部分，提供了更好的 IDE 支持，而 `@enforce` 方法则给我们更多的灵活性和明确性。你可以根据正在进行的项目选择最适合你需求的方法。
