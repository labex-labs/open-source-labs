# 创建带参数的装饰器

到目前为止，我们一直在使用 `@logged` 装饰器，它总是打印一条固定的消息。但如果你想自定义消息格式呢？在本节中，我们将学习如何创建一个可以接受参数的新装饰器，让你在使用装饰器时拥有更多的灵活性。

## 理解带参数的装饰器

带参数的装饰器是一种特殊类型的函数。它并不直接修改另一个函数，而是返回一个装饰器。带参数的装饰器的一般结构如下：

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

当你在代码中使用 `@decorator_with_args(value1, value2)` 时，Python 首先调用 `decorator_with_args(value1, value2)`。这个调用会返回实际的装饰器，然后该装饰器会应用到 `@` 语法后面的函数上。这个两步过程是带参数的装饰器工作的关键。

## 创建 `logformat` 装饰器

让我们创建一个 `@logformat(fmt)` 装饰器，它接受一个格式字符串作为参数。这将使我们能够自定义日志消息。

1. 在 WebIDE 中打开 `logcall.py` 文件，并添加新的装饰器。下面的代码展示了如何定义现有的 `logged` 装饰器和新的 `logformat` 装饰器：

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

在 `logformat` 装饰器中，外部函数 `logformat` 接受一个格式字符串 `fmt` 作为参数。然后它返回 `decorator` 函数，这是实际修改目标函数的装饰器。

2. 现在，让我们通过修改 `sample.py` 文件来测试我们的新装饰器。以下代码展示了如何在不同的函数上使用 `logged` 和 `logformat` 装饰器：

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

在这里，`add` 和 `sub` 函数使用了 `logged` 装饰器，而 `mul` 函数使用了带有自定义格式字符串的 `logformat` 装饰器。

3. 运行更新后的 `sample.py` 文件以查看结果。打开终端并运行以下命令：

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

你应该会看到类似如下的输出：

```
Calling add
5
sample.py:mul
6
```

这个输出表明，`logged` 装饰器按预期打印了函数名，而 `logformat` 装饰器使用自定义格式字符串打印了文件名和函数名。

## 使用 `logformat` 重新定义 `logged` 装饰器

既然我们有了一个更灵活的 `logformat` 装饰器，我们可以使用它来重新定义我们原来的 `logged` 装饰器。这将帮助我们复用代码并保持一致的日志格式。

1. 用以下代码更新 `logcall.py` 文件：

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

在这里，我们使用一个 lambda 函数根据 `logformat` 装饰器来定义 `logged` 装饰器。这个 lambda 函数接受一个函数 `func`，并使用特定的格式字符串应用 `logformat` 装饰器。

2. 测试重新定义的 `logged` 装饰器是否仍然有效。打开终端并运行以下命令：

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

你应该会看到：

```
Calling greet
Hello, World
```

这表明重新定义的 `logged` 装饰器按预期工作，并且我们成功复用了 `logformat` 装饰器来实现一致的日志格式。
