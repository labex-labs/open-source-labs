# 通过文件跟踪器理解协程

让我们先了解一下什么是协程（coroutine），以及它们在 Python 中是如何工作的。协程是生成器函数的一种特殊形式。在 Python 中，函数通常每次被调用时都会从头开始执行。但协程不同，它们既可以消费数据，也可以产生数据，并且能够暂停和恢复执行。这意味着协程可以在某个特定点暂停操作，之后再从暂停处继续执行。

## 创建一个基本的协程文件跟踪器

在这一步中，我们将创建一个文件跟踪器，它使用协程来监控文件的新内容并进行处理。这类似于 Unix 的 `tail -f` 命令，该命令会持续显示文件的末尾，并在添加新行时进行更新。

1. 打开代码编辑器，在 `/home/labex/project` 目录下创建一个名为 `cofollow.py` 的新文件。我们将在这里编写 Python 代码，使用协程来实现文件跟踪器。

2. 将以下代码复制到文件中：

```python
# cofollow.py
import os
import time

# 数据源
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # 移动到文件末尾
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # 将行发送到目标协程
            else:
                time.sleep(0.1)  # 如果没有新内容，短暂休眠

# 协程函数的装饰器
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # 预激活协程（必要的第一步）
        return f
    return start

# 示例协程
@consumer
def printer():
    while True:
        item = yield     # 接收发送给我的项
        print(item)

# 示例用法
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. 让我们来理解这段代码的关键部分：
   - `follow(filename, target)`：这个函数负责打开文件。它首先使用 `f.seek(0, os.SEEK_END)` 将文件指针移动到文件末尾。然后，它进入一个无限循环，在该循环中持续尝试从文件中读取新行。如果找到新行，它会使用 `send` 方法将该行发送到目标协程。如果没有新内容，它会使用 `time.sleep(0.1)` 暂停一小段时间（0.1 秒），然后再次检查。
   - `@consumer` 装饰器：在 Python 中，协程在开始接收数据之前需要被“预激活”。这个装饰器负责处理这个问题。它会自动向协程发送一个初始的 `None` 值，这是让协程准备好接收实际数据的必要第一步。
   - `printer()` 协程：这是一个简单的协程。它有一个无限循环，在循环中使用 `yield` 关键字来接收发送给它的项。一旦接收到项，它就会将其打印出来。

4. 保存文件并从终端运行它：

```bash
cd /home/labex/project
python3 cofollow.py
```

5. 你应该会看到脚本打印出股票日志文件的内容，并且随着新行添加到文件中，它会继续打印新行。按 `Ctrl+C` 停止程序。

这里的关键概念是，数据通过 `send` 方法从 `follow` 函数流入 `printer` 协程。这种“推送”数据的方式与生成器相反，生成器是通过迭代“拉取”数据。在生成器中，你通常使用 `for` 循环来迭代它产生的值。但在这个协程示例中，数据是从代码的一部分主动发送到另一部分的。
