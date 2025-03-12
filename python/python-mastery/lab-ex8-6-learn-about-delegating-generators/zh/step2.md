# 在协程中使用 `yield from`

在这一步中，我们将探索如何在协程中使用 `yield from` 语句，以实现更实际的应用。协程是 Python 中一个强大的概念，了解如何将 `yield from` 与协程结合使用可以极大地简化你的代码。

## 协程与消息传递

协程是一种特殊的函数，它可以通过 `yield` 语句接收值。它们在数据处理和事件处理等任务中非常有用。在 `cofollow.py` 文件中，有一个 `consumer` 装饰器。这个装饰器可以帮助设置协程，自动将协程推进到第一个 `yield` 点。这意味着你不必手动启动协程，装饰器会帮你完成这个操作。

让我们创建一个协程，它可以接收值并验证其类型。你可以按照以下步骤操作：

1. 首先，在编辑器中打开 `cofollow.py` 文件。你可以在终端中使用以下命令导航到正确的目录：

```bash
cd /home/labex/project
```

2. 接下来，在 `cofollow.py` 文件的末尾添加以下 `receive` 函数。这个函数是一个协程，它将接收一条消息并验证其类型。

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

这个函数的功能如下：

- 它使用不带表达式的 `yield` 来接收一个值。当协程接收到一个值时，这个 `yield` 语句会捕获它。
- 它使用 `isinstance` 函数检查接收到的值是否为预期的类型。如果类型不匹配，它会引发一个 `AssertionError`。
- 如果类型检查通过，它会返回该值。

3. 现在，让我们创建一个协程，它使用 `yield from` 调用我们的 `receive` 函数。这个新的协程将只接收并打印整数。

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. 为了测试这个协程，打开一个 Python 交互式环境并运行以下代码：

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

你应该会看到以下输出：

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## 理解 `yield from` 在协程中的工作原理

当我们在 `print_ints` 协程中使用 `yield from receive(int)` 时，会发生以下步骤：

1. 控制权被委托给 `receive` 协程。这意味着 `print_ints` 协程暂停，`receive` 协程开始执行。
2. `receive` 协程使用 `yield` 来接收一个值。它会等待一个值被发送给它。
3. 当一个值被发送给 `print_ints` 时，实际上是由 `receive` 接收的。`yield from` 语句负责将值从 `print_ints` 传递给 `receive`。
4. `receive` 协程验证接收到的值的类型。如果类型正确，它会返回该值。
5. 返回的值成为 `print_ints` 协程中 `yield from` 表达式的结果。这意味着 `print_ints` 中的 `val` 变量会被赋值为 `receive` 返回的值。

使用 `yield from` 使代码比直接处理 `yield` 和 `receive` 更具可读性。它抽象掉了协程之间传递值的复杂性。

## 创建更高级的类型检查协程

让我们扩展我们的实用函数，以处理更复杂的类型验证。你可以按照以下步骤操作：

1. 在 `cofollow.py` 文件中添加以下函数：

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. 为了测试新的协程，打开一个 Python 交互式环境并运行以下代码：

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

你应该会看到如下输出：

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

`yield from` 语句使代码更简洁、更易读。它让我们能够专注于程序的高级逻辑，而不必陷入协程之间消息传递的细节中。
