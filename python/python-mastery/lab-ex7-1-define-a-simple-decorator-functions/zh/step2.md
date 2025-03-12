# 构建一个验证装饰器

在这一步中，我们将创建一个更实用的装饰器。Python 中的装饰器是一种特殊类型的函数，它可以修改另一个函数的行为。我们要创建的装饰器将根据类型注解（type annotations）来验证函数的参数。类型注解是一种指定函数参数和返回值预期数据类型的方式。这在实际应用中是一个常见的用例，因为它有助于确保函数接收到正确的输入类型，从而避免许多错误。

## 理解验证类

我们已经为你创建了一个名为 `validate.py` 的文件，它包含了一些验证类。验证类用于检查一个值是否满足某些条件。要查看这个文件的内容，你需要在 VSCode 编辑器中打开它。你可以在终端中运行以下命令来实现：

```bash
cd /home/labex/project
code validate.py
```

该文件包含三个类：

1. `Validator` - 这是一个基类。基类提供了一个通用的框架或结构，其他类可以继承它。在这种情况下，它为验证提供了基本结构。
2. `Integer` - 这个验证器类用于确保一个值是整数。如果你将非整数值传递给使用这个验证器的函数，它将引发一个错误。
3. `PositiveInteger` - 这个验证器类确保一个值是正整数。因此，如果你传递一个负整数或零，它也将引发一个错误。

## 添加验证装饰器

现在，我们要在 `validate.py` 文件中添加一个名为 `validated` 的装饰器函数。这个装饰器将执行几个重要的任务：

1. 它将检查函数的类型注解。类型注解就像小注释，告诉我们函数期望什么样的数据。
2. 它将根据这些类型注解验证传递给函数的参数。这意味着它将检查传递给函数的值是否为正确的类型。
3. 它还将根据函数的注解验证函数的返回值。因此，它确保函数返回它应该返回的数据类型。
4. 如果验证失败，它将引发信息丰富的错误消息。这些消息将准确地告诉你哪里出了问题，比如哪个参数的类型错误。

将以下代码添加到 `validate.py` 文件的末尾：

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

这段代码使用了 Python 的 `inspect` 模块。`inspect` 模块允许我们获取关于实时对象（如函数）的信息。在这里，我们使用它来检查函数的签名，并根据类型注解验证参数。我们还使用了 `functools.wraps`。这是一个辅助函数，它可以保留原函数的元数据，如函数名和文档字符串。元数据就像是关于函数的额外信息，有助于我们理解函数的作用。

## 测试验证装饰器

让我们创建一个文件来测试我们的验证装饰器。我们将创建一个名为 `test_validate.py` 的新文件，并向其中添加以下代码：

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

现在，我们将在 Python 解释器中测试我们的装饰器。首先，导航到项目目录并在终端中运行以下命令来启动 Python 解释器：

```bash
cd /home/labex/project
python3
```

然后，在 Python 解释器中，我们可以运行以下代码来测试我们的装饰器：

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

如你所见，我们的 `validated` 装饰器成功地对函数参数和返回值执行了类型检查。这非常有用，因为它使我们的代码更加健壮。我们可以在函数边界处捕获类型错误，而不是让它们在代码中进一步传播并导致难以发现的错误。
