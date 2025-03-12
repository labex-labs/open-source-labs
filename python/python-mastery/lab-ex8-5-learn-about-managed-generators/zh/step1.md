# 理解 Python 生成器

让我们先回顾一下 Python 中生成器的概念。在 Python 里，生成器是一种特殊类型的函数，它们与普通函数有所不同。当你调用一个普通函数时，它会从头到尾执行，并返回一个单一的值。然而，生成器函数会返回一个迭代器（iterator），这是一个可以进行迭代的对象，意味着我们可以逐个访问其值。

生成器使用 `yield` 语句来返回值。与普通函数一次性返回所有值不同，生成器会一次返回一个值。在生成一个值之后，生成器会暂停执行。下次我们请求一个值时，它会从上次暂停的地方继续执行。

## 创建一个简单的生成器

现在，让我们来创建一个简单的生成器。在 WebIDE 中，你需要创建一个新文件，该文件将包含我们生成器的代码。将文件命名为 `generator_demo.py`，并将其放在 `/home/labex/project` 目录下。以下是你应该放入文件中的内容：

```python
# Generator function that counts down from n
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Countdown complete!")

# Create a generator object
counter = countdown(5)

# Drive the generator manually
print(next(counter))  # 5
print(next(counter))  # 4
print(next(counter))  # 3

# Iterate through remaining values
for value in counter:
    print(value)  # 2, 1
```

在这段代码中，我们首先定义了一个名为 `countdown` 的生成器函数。这个函数接受一个数字 `n` 作为参数，并从 `n` 开始倒数到 1。在函数内部，我们使用一个 `while` 循环来递减 `n` 并生成每个值。当我们调用 `countdown(5)` 时，它会创建一个名为 `counter` 的生成器对象。

然后，我们使用 `next()` 函数手动从生成器中获取值。每次调用 `next(counter)` 时，生成器会从上次暂停的地方继续执行，并生成下一个值。在手动获取三个值之后，我们使用一个 `for` 循环来迭代生成器中剩余的值。

要运行这段代码，打开终端并执行以下命令：

```bash
python3 /home/labex/project/generator_demo.py
```

当你运行代码时，你应该会看到以下输出：

```
Starting countdown from 5
5
4
3
2
1
Countdown complete!
```

让我们注意一下生成器函数的行为：

1. 当我们首次调用 `next(counter)` 时，生成器函数开始执行。在此之前，函数只是被定义，实际的倒计时并未开始。
2. 它会在每个 `yield` 语句处暂停。在生成一个值之后，它会停止并等待下一次调用 `next()`。
3. 当我们再次调用 `next()` 时，它会从上次暂停的地方继续执行。例如，在生成 5 之后，它会记住状态，继续递减 `n` 并生成下一个值。
4. 在生成最后一个值之后，生成器函数完成执行。在我们的例子中，在生成 1 之后，它会打印 "Countdown complete!"。

这种暂停和恢复执行的能力正是生成器强大的原因。它对于任务调度和异步编程等任务非常有用，在这些任务中，我们需要以高效的方式执行多个任务，而不会阻塞其他任务的执行。
