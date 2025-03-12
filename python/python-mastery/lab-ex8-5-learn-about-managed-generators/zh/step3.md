# 测试我们的任务调度器

现在，我们要在 `multitask.py` 文件中添加一个测试。这个测试的目的是同时运行多个任务，这被称为并发执行。并发执行允许不同的任务看似同时取得进展，尽管在单线程环境中，这些任务实际上是轮流运行的。

为了进行这个测试，在 `multitask.py` 文件的末尾添加以下代码：

```python
# Test our scheduler
if __name__ == '__main__':
    # Add tasks to the queue
    tasks.append(countdown(10))  # Count down from 10
    tasks.append(countdown(5))   # Count down from 5
    tasks.append(countup(20))    # Count up to 20

    # Run all tasks
    run()
```

在这段代码中，我们首先使用 `if __name__ == '__main__':` 检查脚本是否是直接运行的。然后，我们向 `tasks` 队列中添加三个不同的任务。`countdown` 任务会从给定的数字开始倒计时，而 `countup` 任务会计数到指定的数字。最后，我们调用 `run()` 函数来开始执行这些任务。

添加代码后，在终端中使用以下命令运行它：

```bash
python3 /home/labex/project/multitask.py
```

当你运行代码时，你应该会看到类似以下的输出（具体的行顺序可能会有所不同）：

```
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
...
```

注意不同任务的输出是如何混合在一起的。这清楚地表明我们的调度器正在并发运行所有三个任务。每次一个任务到达 `yield` 语句时，调度器会暂停该任务并切换到另一个任务，从而使所有任务随着时间的推移都能取得进展。

## 工作原理

让我们更仔细地看看我们的调度器运行时会发生什么：

1. 首先，我们向队列中添加三个生成器任务：`countdown(10)`、`countdown(5)` 和 `countup(20)`。这些生成器任务是特殊的函数，它们可以在 `yield` 语句处暂停和恢复执行。
2. 然后，`run()` 函数开始工作：
   - 它从队列中取出第一个任务 `countdown(10)`。
   - 它运行这个任务，直到到达 `yield` 语句。当遇到 `yield` 时，它会打印 "T-minus 10"。
   - 之后，它将 `countdown(10)` 任务重新添加到队列中，以便稍后可以再次运行。
   - 接下来，它从队列中取出 `countdown(5)` 任务。
   - 它运行 `countdown(5)` 任务，直到遇到 `yield` 语句，打印 "T-minus 5"。
   - 这个过程会持续进行……

这个循环会一直持续，直到所有任务都完成。每个任务都有机会运行一小段时间，这就产生了并发执行的错觉，而无需使用线程或回调。线程是一种更复杂的实现并发的方式，而回调则用于异步编程。我们的简单调度器使用生成器以更直接的方式实现了类似的效果。
