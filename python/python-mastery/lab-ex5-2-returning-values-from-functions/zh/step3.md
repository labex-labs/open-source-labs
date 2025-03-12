# 使用 Future 进行并发编程

在 Python 中，当你需要同时（即并发）运行函数时，Python 提供了像线程（threads）和进程（processes）这样有用的工具。但你会面临一个常见问题：当一个函数在不同的线程中运行时，你如何获取它返回的值呢？这就是 `Future` 概念变得非常重要的地方。

`Future` 就像是一个占位符，代表着稍后会得到的结果。它是一种表示函数在未来会产生的值的方式，即使函数还未运行完成。让我们通过一个简单的例子来更好地理解这个概念。

### 步骤 1：创建一个新文件

首先，你需要创建一个新的 Python 文件。我们将其命名为 `futures_demo.py`。你可以在终端中使用以下命令来创建这个文件：

```
touch ~/project/futures_demo.py
```

### 步骤 2：添加基本函数代码

现在，打开 `futures_demo.py` 文件并添加以下 Python 代码。这段代码定义了一个简单的函数，并展示了普通函数调用是如何工作的。

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

在这段代码中，`worker` 函数接受两个数字，将它们相加，但首先它会通过暂停 5 秒来模拟一个耗时的任务。当你以普通方式调用这个函数时，程序会等待函数完成，然后获取返回值。

### 步骤 3：运行基本代码

保存文件并在终端中使用以下命令运行它：

```
python ~/project/futures_demo.py
```

你应该会看到如下输出：

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

这表明普通的函数调用会等待函数完成，然后返回结果。

### 步骤 4：在单独的线程中运行函数

接下来，让我们看看当我们在单独的线程中运行 `worker` 函数时会发生什么。将以下代码添加到 `futures_demo.py` 文件中：

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

在这里，我们使用 `threading.Thread` 类在一个新线程中启动 `worker` 函数。主线程不会等待 `worker` 函数完成，而是继续执行。然而，当 `worker` 线程完成时，我们没有简单的方法来获取返回值。

### 步骤 5：运行线程代码

再次保存文件并使用相同的命令运行它：

```
python ~/project/futures_demo.py
```

你会注意到主线程继续执行，工作线程也在运行，但我们无法访问 `worker` 函数的返回值。

### 步骤 6：手动使用 `Future`

为了解决从线程中获取返回值的问题，我们可以使用 `Future` 对象。将以下代码添加到 `futures_demo.py` 文件中：

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

在这段代码中，我们创建了一个 `Future` 对象，并将其传递给一个新函数 `do_work_with_future`。这个函数调用 `worker` 函数，然后将结果设置到 `Future` 对象中。然后主线程可以使用 `Future` 对象的 `result()` 方法在结果可用时获取结果。

### 步骤 7：运行使用 `Future` 的代码

保存文件并再次运行它：

```
python ~/project/futures_demo.py
```

现在你会看到我们可以成功地从线程中运行的函数获取返回值。

### 步骤 8：使用 `ThreadPoolExecutor`

Python 中的 `ThreadPoolExecutor` 类让处理并发任务变得更加容易。将以下代码添加到 `futures_demo.py` 文件中：

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

`ThreadPoolExecutor` 会为你创建和管理 `Future` 对象。你只需要提交函数及其参数，它就会返回一个 `Future` 对象，你可以使用该对象来获取结果。

### 步骤 9：运行完整代码

最后一次保存文件并运行它：

```
python ~/project/futures_demo.py
```

### 解释

1. **普通函数调用**：当你以普通方式调用函数时，程序会等待函数完成并直接获取返回值。
2. **线程问题**：在单独的线程中运行函数有一个缺点，即没有内置的方法来获取该线程中运行的函数的返回值。
3. **手动使用 Future**：通过创建一个 `Future` 对象并将其传递给线程，我们可以将结果设置到 `Future` 中，然后从主线程获取结果。
4. **ThreadPoolExecutor**：这个类简化了并发编程。它为你处理 `Future` 对象的创建和管理，使你更容易并发运行函数并获取它们的返回值。

`Future` 对象有几个有用的方法：

- `result()`：这个方法用于获取函数的结果。如果结果还未准备好，它会一直等待直到结果可用。
- `done()`：你可以使用这个方法来检查函数的计算是否完成。
- `add_done_callback()`：这个方法允许你注册一个函数，当结果准备好时会调用该函数。

这种模式在并发编程中非常重要，特别是当你需要从并行运行的函数中获取结果时。
