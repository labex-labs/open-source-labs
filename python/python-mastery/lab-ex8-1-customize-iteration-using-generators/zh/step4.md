# 创建用于流式数据的生成器

在编程中，生成器是一个强大的工具，尤其在处理像监控流式数据源这样的实际问题时。在本节中，我们将学习如何将所学的生成器知识应用到这样一个实际场景中。我们将创建一个生成器，用于监控日志文件，并在文件添加新行时将其提供给我们。

## 设置数据源

在开始创建生成器之前，我们需要设置一个数据源。在这种情况下，我们将使用一个生成股票市场数据的模拟程序。

首先，你需要在 WebIDE 中打开一个新的终端。你将在这个终端中运行启动模拟的命令。

打开终端后，你将运行股票模拟程序。以下是你需要输入的命令：

```bash
cd ~/project
python3 stocksim.py
```

第一个命令 `cd ~/project` 将当前目录更改为你主目录下的 `project` 目录。第二个命令 `python3 stocksim.py` 运行股票模拟程序。这个程序将生成股票市场数据，并将其写入当前目录下名为 `stocklog.csv` 的文件中。在我们编写监控代码时，让这个程序在后台运行。

## 创建一个简单的文件监控程序

现在我们已经设置好了数据源，让我们创建一个程序来监控 `stocklog.csv` 文件。这个程序将显示所有价格变化为负的情况。

1. 首先，在 WebIDE 中创建一个名为 `follow.py` 的新文件。为此，你需要在终端中使用以下命令将目录更改为 `project` 目录：

```bash
cd ~/project
```

2. 接下来，将以下代码添加到 `follow.py` 文件中。这段代码打开 `stocklog.csv` 文件，将文件指针移动到文件末尾，然后持续检查是否有新行。如果找到新行，并且它表示价格变化为负，则打印股票名称、价格和变化。

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

3. 添加代码后，保存文件。然后，在终端中使用以下命令运行程序：

```bash
python3 follow.py
```

你应该会看到显示价格变化为负的股票的输出。它可能看起来像这样：

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

如果你想停止程序，在终端中按 `Ctrl+C`。

## 转换为生成器函数

虽然之前的代码可以正常工作，但我们可以通过将其转换为生成器函数，使其更具可重用性和模块化。生成器函数是一种特殊类型的函数，它可以暂停和恢复，并一次产生一个值。

1. 再次打开 `follow.py` 文件，并将其修改为使用生成器函数。以下是更新后的代码：

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

`follow` 函数现在是一个生成器函数。它打开文件，移动到文件末尾，然后持续检查是否有新行。当找到新行时，它会产生该行。

2. 保存文件并再次使用以下命令运行它：

```bash
python3 follow.py
```

输出应该和之前一样。但现在，文件监控逻辑被整齐地封装在 `follow` 生成器函数中。这意味着我们可以在其他需要监控文件的程序中重用这个函数。

## 理解生成器的强大之处

通过将我们的文件读取代码转换为生成器函数，我们使其变得更加灵活和可重用。`follow()` 函数可以用于任何需要监控文件的程序，而不仅仅是用于股票数据。

例如，你可以使用它来监控服务器日志、应用程序日志或任何随时间更新的其他文件。这展示了生成器是一种以简洁和模块化的方式处理流式数据源的绝佳方法。
