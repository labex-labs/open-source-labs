# 使用生成器创建任务调度器

在编程中，任务调度器是一个重要的工具，它有助于高效地管理和执行多个任务。在本节中，我们将使用生成器构建一个简单的任务调度器，该调度器可以并发运行多个生成器函数。这将向你展示如何管理生成器以实现协作式多任务处理，即任务轮流运行并共享执行时间。

首先，你需要创建一个新文件。导航到 `/home/labex/project` 目录并创建一个名为 `multitask.py` 的文件。该文件将包含我们任务调度器的代码。

```python
# multitask.py

from collections import deque

# Task queue
tasks = deque()

# Simple task scheduler
def run():
    while tasks:
        task = tasks.popleft()  # Get the next task
        try:
            task.send(None)     # Resume the task
            tasks.append(task)  # Put it back in the queue
        except StopIteration:
            print('Task done')  # Task is complete

# Example task 1: Countdown
def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield              # Pause execution
        n -= 1

# Example task 2: Count up
def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield              # Pause execution
        x += 1
```

现在，让我们详细分析这个任务调度器的工作原理：

1. 我们使用 `deque`（双端队列）来存储生成器任务。`deque` 是一种数据结构，它允许你高效地从两端添加和移除元素。对于我们的任务队列来说，它是一个很好的选择，因为我们需要在队列尾部添加任务，并从队列头部移除任务。
2. `run()` 函数是我们任务调度器的核心。它逐个从队列中取出任务：
   - 它使用 `send(None)` 恢复每个任务的执行。这类似于对生成器使用 `next()`。它告诉生成器从上次暂停的地方继续执行。
   - 任务产生（yield）值后，会被重新添加到队列尾部。这样，该任务稍后将有机会再次运行。
   - 当一个任务完成（抛出 `StopIteration` 异常）时，它会从队列中移除。这表明该任务已完成执行。
3. 我们的生成器任务中的每个 `yield` 语句都充当一个暂停点。当生成器到达 `yield` 语句时，它会暂停执行并将控制权交还给调度器。这使得其他任务可以运行。

这种方法实现了协作式多任务处理。每个任务自愿将控制权交还给调度器，从而允许其他任务运行。通过这种方式，多个任务可以共享执行时间并并发运行。
