# 理解生成器的生命周期和关闭操作

在这一步中，我们将探索 Python 生成器的生命周期，并学习如何正确地关闭它们。Python 中的生成器是一种特殊类型的迭代器，它允许你动态生成一系列值，而不是一次性计算所有值并将它们存储在内存中。在处理大型数据集或无限序列时，这非常有用。

## 什么是 `follow()` 生成器？

让我们首先查看项目目录中的 `follow.py` 文件。这个文件包含一个名为 `follow()` 的生成器函数。生成器函数的定义与普通函数类似，但它使用 `yield` 而不是 `return` 关键字。当调用生成器函数时，它会返回一个生成器对象，你可以对该对象进行迭代以获取它产生的值。

`follow()` 生成器函数会持续从文件中读取行，并在读取到每一行时将其产生出来。这类似于 Unix 的 `tail -f` 命令，该命令会持续监控文件以获取新行。

在 WebIDE 编辑器中打开 `follow.py` 文件：

```python
import os
import time

def follow(filename):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)    # Sleep briefly to avoid busy wait
                continue
            yield line
```

在这段代码中，`with open(filename, 'r') as f` 语句以只读模式打开文件，并确保在代码块结束时文件被正确关闭。`f.seek(0, os.SEEK_END)` 行将文件指针移动到文件末尾，这样生成器就从文件末尾开始读取。`while True` 循环会持续从文件中读取行。如果行为空，说明还没有新行，程序会休眠 0.1 秒以避免忙等待，然后继续下一次迭代。如果行不为空，则将其产生出来。

这个生成器在一个无限循环中运行，这就引出了一个重要的问题：当我们停止使用生成器或想要提前终止它时会发生什么？

## 修改生成器以处理关闭操作

我们需要修改 `follow.py` 中的 `follow()` 函数，以处理生成器被正确关闭的情况。为此，我们将添加一个 `try-except` 块来捕获 `GeneratorExit` 异常。当生成器通过垃圾回收或调用 `close()` 方法被关闭时，会引发 `GeneratorExit` 异常。

```python
import os
import time

def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)    # Sleep briefly to avoid busy wait
                    continue
                yield line
    except GeneratorExit:
        print('Following Done')
```

在这段修改后的代码中，`try` 块包含了生成器的主要逻辑。如果引发了 `GeneratorExit` 异常，`except` 块会捕获它并打印消息 'Following Done'。这是在生成器关闭时执行清理操作的一种简单方法。

完成这些更改后保存文件。

## 对生成器关闭操作进行实验

现在，让我们进行一些实验，看看生成器在被垃圾回收或显式关闭时的行为。

打开一个终端并运行 Python 解释器：

```bash
cd ~/project
python3
```

### 实验 1：运行中的生成器的垃圾回收

```python
>>> from follow import follow
>>> # Experiment: Garbage collection of a running generator
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f  # Delete the generator object
Following Done  # This message appears because of our GeneratorExit handler
```

在这个实验中，我们首先从 `follow.py` 文件中导入 `follow` 函数。然后，我们通过调用 `follow('stocklog.csv')` 创建一个生成器对象 `f`。我们使用 `next()` 函数从生成器中获取下一行。最后，我们使用 `del` 语句删除生成器对象。当生成器对象被删除时，它会自动关闭，这会触发我们的 `GeneratorExit` 异常处理程序，并打印消息 'Following Done'。

### 实验 2：显式关闭生成器

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         f.close()  # Explicitly close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
...     print(line, end='')  # No output: generator is closed
...
```

在这个实验中，我们创建一个新的生成器对象 `f`，并使用 `for` 循环对其进行迭代。在循环内部，我们打印每一行，并检查该行是否包含字符串 'IBM'。如果包含，我们调用生成器的 `close()` 方法来显式关闭它。当生成器被关闭时，会引发 `GeneratorExit` 异常，我们的异常处理程序会打印消息 'Following Done'。生成器关闭后，如果我们再次尝试对其进行迭代，将不会有输出，因为生成器已经不再活跃。

### 实验 3：跳出并恢复生成器的迭代

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break  # Break out of the loop, but don't close the generator
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
>>> # Resume iteration - the generator is still active
>>> for line in f:
...     print(line, end='')
...     if 'IBM' in line:
...         break
...
"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> del f  # Clean up
Following Done
```

在这个实验中，我们创建一个生成器对象 `f`，并使用 `for` 循环对其进行迭代。在循环内部，我们打印每一行，并检查该行是否包含字符串 'IBM'。如果包含，我们使用 `break` 语句跳出循环。跳出循环并不会关闭生成器，因此生成器仍然活跃。然后，我们可以通过对同一个生成器对象启动一个新的 `for` 循环来恢复迭代。最后，我们删除生成器对象以进行清理，这会触发 `GeneratorExit` 异常处理程序。

## 关键要点

1. 当生成器被关闭（通过垃圾回收或调用 `close()` 方法）时，会在生成器内部引发 `GeneratorExit` 异常。
2. 你可以捕获这个异常，以便在生成器关闭时执行清理操作。
3. 使用 `break` 语句跳出生成器的迭代并不会关闭生成器，因此可以在稍后恢复迭代。

通过输入 `exit()` 或按下 `Ctrl+D` 退出 Python 解释器。
