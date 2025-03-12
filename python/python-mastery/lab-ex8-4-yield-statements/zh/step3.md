# 生成器管理的实际应用

在这一步中，我们将探索如何把所学的生成器管理和异常处理概念应用到实际场景中。理解这些实际应用将帮助你编写更健壮、高效的 Python 代码。

## 创建一个健壮的文件监控系统

让我们构建一个更可靠的文件监控系统。这个系统能够处理不同的情况，例如超时和用户的停止请求。

首先，打开 WebIDE 编辑器，创建一个名为 `robust_follow.py` 的新文件。你需要在这个文件中编写以下代码：

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

在这段代码中，我们首先定义了一个自定义的 `TimeoutError` 类。`timeout_handler` 函数用于在超时发生时抛出这个错误。`follow` 函数是一个生成器，它读取文件并产生新的行。如果指定了超时时间，它会使用 `signal` 模块设置一个警报。如果文件中没有新数据，它会短暂等待后再尝试。`try - except - finally` 块用于处理不同的异常，并确保进行适当的清理。

编写完代码后，保存文件。

## 测试健壮的文件监控系统

现在，让我们测试改进后的文件监控系统。打开一个终端，使用以下命令运行 Python 解释器：

```bash
cd ~/project
python3
```

### 实验 1：基本使用

在 Python 解释器中，我们将测试 `follow` 生成器的基本功能。运行以下代码：

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

在这里，我们从 `robust_follow.py` 文件中导入 `follow` 函数。然后创建一个生成器对象 `f`，用于监控 `stocklog.csv` 文件。我们使用 `for` 循环迭代生成器产生的行，并打印前 3 行。

### 实验 2：使用超时功能

让我们看看超时功能是如何工作的。在 Python 解释器中运行以下代码：

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

在这个实验中，我们创建了一个带有 3 秒超时时间的生成器。我们通过在每行处理之间休眠 1 秒来缓慢处理每行。大约 3 秒后，生成器抛出超时异常，`finally` 块中的清理代码会被执行。

### 实验 3：显式关闭

让我们测试生成器如何处理显式关闭。运行以下代码：

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

在这里，我们创建一个生成器并开始迭代其行。处理 2 行后，我们使用 `close` 方法显式关闭生成器。然后生成器会处理 `GeneratorExit` 异常并执行必要的清理操作。

## 创建一个带有错误处理的数据处理管道

接下来，我们将使用协程创建一个简单的数据处理管道。这个管道能够在不同阶段处理错误。

打开 WebIDE 编辑器，创建一个名为 `pipeline.py` 的新文件。在这个文件中编写以下代码：

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

在这段代码中，`consumer` 装饰器用于初始化协程。`grep` 协程过滤包含特定模式的行，并将它们发送到另一个协程。`printer` 协程打印接收到的项。`follow_and_process` 函数读取文件，使用 `grep` 协程过滤其行，并使用 `printer` 协程打印匹配的行。它还处理 `KeyboardInterrupt` 异常，并确保进行适当的清理。

编写完代码后，保存文件。

## 测试数据处理管道

让我们测试数据处理管道。在终端中运行以下命令：

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

你应该会看到类似以下的输出：

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

这个输出表明管道正常工作，过滤并打印了包含 "IBM" 模式的行。

要停止这个进程，按 `Ctrl+C`。你应该会看到以下消息：

```
Processing stopped by user
```

## 关键要点

1. 在生成器中进行适当的异常处理可以让你创建能够优雅处理错误的健壮系统。这意味着当出现问题时，你的程序不会意外崩溃。
2. 你可以使用超时等技术来防止生成器无限运行。这有助于管理系统资源，并确保你的程序不会陷入无限循环。
3. 生成器和协程可以形成强大的数据处理管道，在其中可以在适当的级别传播和处理错误。这使得构建复杂的数据处理系统变得更容易。
4. 生成器中的 `finally` 块确保无论生成器如何终止，都会执行清理操作。这有助于维护程序的完整性，并防止资源泄漏。
