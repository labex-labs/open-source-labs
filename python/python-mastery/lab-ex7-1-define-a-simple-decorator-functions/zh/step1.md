# 创建你的第一个装饰器

## 什么是装饰器？

在 Python 中，装饰器（decorators）是一种特殊的语法，对初学者来说非常有用。它们允许你修改函数或方法的行为。你可以把装饰器看作是一个函数，它接受另一个函数作为输入，然后返回一个新的函数。这个新函数通常会扩展或改变原函数的行为。

装饰器使用 `@` 符号来应用。你将这个符号和装饰器名称直接放在函数定义的上方。这是一种简单的方式，用于告诉 Python 你想在特定的函数上使用该装饰器。

## 创建一个简单的日志记录装饰器

让我们创建一个简单的装饰器，它在函数被调用时记录信息。日志记录是实际应用中常见的任务，使用装饰器来实现这一点是理解它们如何工作的好方法。

1. 首先，打开 VSCode 编辑器。在 `/home/labex/project` 目录下，创建一个名为 `logcall.py` 的新文件。这个文件将包含我们的装饰器函数。

2. 将以下代码添加到 `logcall.py` 中：

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

让我们来分析一下这段代码的作用：

- `logged` 函数是我们的装饰器。它接受另一个函数（我们称之为 `func`）作为参数。这个 `func` 就是我们想要添加日志记录功能的函数。
- 当装饰器应用到一个函数时，它会打印一条消息。这条消息告诉我们正在为具有给定名称的函数添加日志记录功能。
- 在 `logged` 函数内部，我们定义了一个名为 `wrapper` 的内部函数。这个 `wrapper` 函数将取代原函数。
  - 当被装饰的函数被调用时，`wrapper` 函数会打印一条消息，表明该函数正在被调用。
  - 然后，它使用传递给它的所有参数调用原函数（`func`）。`*args` 和 `**kwargs` 用于接受任意数量的位置参数和关键字参数。
  - 最后，它返回原函数的结果。
- `logged` 函数返回 `wrapper` 函数。现在，这个 `wrapper` 函数将代替原函数使用，从而添加了日志记录功能。

## 使用装饰器

3. 现在，在同一目录（`/home/labex/project`）下，创建另一个名为 `sample.py` 的文件，并添加以下代码：

```python
# sample.py

from logcall import logged

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y
```

这里的 `@logged` 语法非常重要。它告诉 Python 将 `logged` 装饰器应用到 `add` 和 `sub` 函数上。因此，每当调用这些函数时，装饰器添加的日志记录功能就会被执行。

## 测试装饰器

4. 要测试你的装饰器，在 VSCode 中打开一个终端。首先，使用以下命令将目录更改为项目目录：

```bash
cd /home/labex/project
```

然后，启动 Python 解释器：

```bash
python3
```

5. 在 Python 解释器中，导入 `sample` 模块并测试被装饰的函数：

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3, 4)
Calling add
7
>>> sample.sub(2, 3)
Calling sub
-1
>>> exit()
```

注意，当你导入 `sample` 模块时，会打印出“Adding logging to...”消息。这是因为装饰器在模块导入时就会被应用。每次调用被装饰的函数时，都会打印出“Calling...”消息。这表明装饰器正在按预期工作。

这个简单的装饰器展示了装饰器的基本概念。它在不改变原函数代码的情况下，用额外的功能（这里是日志记录）包装了原函数。这是 Python 中一个强大的特性，你可以在许多不同的场景中使用它。
