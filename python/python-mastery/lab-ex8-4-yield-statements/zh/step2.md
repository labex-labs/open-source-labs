# 处理生成器中的异常

在这一步中，你将学习如何处理生成器和协程中的异常。不过首先，让我们了解一下什么是异常。异常是程序执行过程中发生的事件，它会打乱程序指令的正常执行流程。在 Python 中，你可以使用 `throw()` 方法来处理生成器和协程中的异常。

## 理解协程

协程是一种特殊类型的生成器。与主要用于产生值的常规生成器不同，协程既可以消耗值（使用 `send()` 方法），也可以产生值。`cofollow.py` 文件中有一个简单的协程实现。

让我们在 WebIDE 编辑器中打开 `cofollow.py` 文件。以下是其中的代码：

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

现在，让我们来分析一下这段代码。`consumer` 是一个装饰器。装饰器是一种函数，它接受另一个函数作为参数，为其添加一些功能，然后返回修改后的函数。在这种情况下，`consumer` 装饰器会自动将生成器移动到其第一个 `yield` 语句处。这很重要，因为它使生成器准备好接收值。

`printer()` 协程使用 `@consumer` 装饰器进行定义。在 `printer()` 函数内部，有一个无限的 `while` 循环。`item = yield` 语句是关键所在。它会暂停协程的执行，并等待接收一个值。当有值发送给协程时，它会恢复执行并打印接收到的值。

## 为协程添加异常处理

现在，你要修改 `printer()` 协程以处理异常。你可以像下面这样更新 `cofollow.py` 中的 `printer()` 函数：

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

`try` 块包含可能引发异常的代码。在这个例子中，就是接收并打印值的代码。如果 `try` 块中发生异常，执行流程会跳转到 `except` 块。`except` 块会捕获异常并打印错误消息。完成这些修改后，保存文件。

## 对协程中的异常处理进行实验

让我们开始实验如何向协程中抛出异常。打开一个终端，并使用以下命令运行 Python 解释器：

```bash
cd ~/project
python3
```

### 实验 1：基本的协程使用

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

在这里，你首先从 `cofollow` 模块中导入 `printer` 协程。然后创建一个名为 `p` 的 `printer` 协程实例。你使用 `send()` 方法向协程发送值。如你所见，协程可以顺利处理你发送给它的值。

### 实验 2：向协程中抛出异常

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

在这个实验中，你使用 `throw()` 方法向协程中注入一个 `ValueError` 异常。`printer()` 协程中的 `try-except` 块会捕获该异常并打印错误消息。这表明你的异常处理按预期工作。

### 实验 3：向协程中抛出实际的异常

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

在这里，你首先尝试将字符串 `'n/a'` 转换为整数，这会引发一个 `ValueError` 异常。你捕获这个异常，然后使用 `throw()` 方法将其传递给协程。协程会捕获该异常并打印错误消息。

### 实验 4：验证协程继续运行

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

在处理完异常后，你使用 `send()` 方法向协程发送另一个值。协程仍然处于活动状态，并且可以处理新的值。这表明你的协程即使在遇到错误后也能继续运行。

## 关键要点

1. 生成器和协程可以在 `yield` 语句处处理异常。这意味着你可以捕获并处理协程在等待或处理值时发生的错误。
2. `throw()` 方法允许你向生成器或协程中注入异常。这对于测试和处理协程外部发生的错误很有用。
3. 在生成器中正确处理异常可以让你创建健壮、容错的生成器，即使发生错误也能继续运行。这会使你的代码更可靠，更易于维护。

要退出 Python 解释器，你可以输入 `exit()` 或按下 `Ctrl+D`。
