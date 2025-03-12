# 理解 `yield from` 语句

在这一步中，我们将探索 Python 中的 `yield from` 语句。这个语句在处理生成器时是一个强大的工具，它简化了将操作委托给其他生成器的过程。在这一步结束时，你将理解 `yield from` 是什么、它是如何工作的，以及它如何处理不同生成器之间的值传递。

## 什么是 `yield from`？

`yield from` 语句是在 Python 3.3 中引入的。它的主要目的是简化将操作委托给子生成器（subgenerator）的过程。子生成器就是主生成器可以委托工作的另一个生成器。

通常，当你希望一个生成器从另一个生成器中产出值时，你必须使用一个循环。例如，不使用 `yield from` 时，你会编写如下代码：

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

在这段代码中，`delegating_generator` 使用一个 `for` 循环来迭代 `subgenerator` 产生的值，然后逐个产出这些值。

然而，使用 `yield from` 语句后，代码变得简单得多：

```python
def delegating_generator():
    yield from subgenerator()
```

这一行代码实现了与前一个示例中的循环相同的结果。但 `yield from` 不仅仅是一个捷径。它还管理调用者和子生成器之间的双向通信。这意味着发送给委托生成器的任何值都会直接传递给子生成器。

## 基本示例

让我们创建一个简单的示例，看看 `yield from` 是如何实际工作的。

1. 首先，你需要在编辑器中打开 `cofollow.py` 文件。为此，我们将使用 `cd` 命令导航到正确的目录。在终端中运行以下命令：

```bash
cd /home/labex/project
```

2. 接下来，我们将在 `cofollow.py` 文件中添加两个函数。`subgen` 函数是一个简单的生成器，它产出从 0 到 4 的数字。`main_gen` 函数使用 `yield from` 将这些数字的生成委托给 `subgen`，然后产出字符串 `'Done'`。将以下代码添加到 `cofollow.py` 文件的末尾：

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. 现在，让我们测试这些函数。打开一个 Python 交互式环境并运行以下代码：

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

当你运行这段代码时，你应该会看到以下输出：

```
0
1
2
3
4

0
1
2
3
4
Done
```

这个输出表明 `yield from` 允许 `main_gen` 将 `subgen` 生成的所有值直接传递给调用者。

## 使用 `yield from` 进行值传递

`yield from` 最强大的特性之一是它能够处理双向的值传递。让我们创建一个更复杂的示例来演示这一点。

1. 将以下函数添加到 `cofollow.py` 文件中：

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

`accumulator` 函数是一个协程，它跟踪一个累加的总数。它产出当前的总数，然后等待接收一个新的值。如果接收到 `None`，它就会停止循环。`caller` 函数创建一个 `accumulator` 的实例，并使用 `yield from` 将所有的发送和接收操作委托给它。

2. 在 Python 交互式环境中测试这些函数：

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

当你运行这段代码时，你应该会看到以下输出：

```
0
1
3
6
'Total accumulated'
```

这个输出表明 `yield from` 会将所有的发送和接收操作完全委托给子生成器，直到子生成器耗尽为止。

现在你已经理解了 `yield from` 的基础知识，我们将在下一步中继续探讨更实际的应用。
