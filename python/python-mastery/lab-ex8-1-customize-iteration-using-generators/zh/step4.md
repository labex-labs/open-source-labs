# 监控流数据源

生成器也是一种生成数据流的有用方式。在本部分中，我们将通过编写一个生成器来监控日志文件，探索这一概念。首先，请仔细按照以下说明操作。

程序 `stocksim.py` 是一个模拟股票市场数据的程序。作为输出，该程序会持续将实时数据写入文件 `stocklog.csv`。在命令窗口（而非 IDLE）中，进入该目录并运行此程序：

    % python3 stocksim.py

如果你使用的是 Windows，只需找到 `stocksim.py` 程序并双击运行它。现在，先不用管这个程序（让它运行即可）。再次强调，就让这个程序在后台运行 —— 它会运行几个小时（你无需担心）。

上述程序运行后，让我们编写一个小程序来打开该文件，定位到文件末尾，并监控新的输出。创建一个文件 `follow.py`，并将以下代码放入其中：

```python
# follow.py
import os
import time
f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # 将文件指针从文件末尾移动 0 字节

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # 短暂休眠并重试
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

运行该程序后，你将看到一个实时股票报价器。实际上，这段代码类似于用于监控日志文件的 Unix `tail -f` 命令。

**注意**：本示例中对 `readline()` 方法的使用有些不同寻常，因为它并非从文件读取行的常用方式（通常你会使用 `for` 循环）。然而，在这种情况下，我们使用它来反复探测文件末尾，查看是否有更多数据被添加（`readline()` 要么返回新数据，要么返回空字符串）。

仔细观察代码，代码的第一部分生成数据行，而 `while` 循环末尾的语句则处理这些数据。生成器函数的一个主要特性是，你可以将所有数据生成代码移动到一个可复用的函数中。

修改代码，使文件读取由生成器函数 `follow(filename)` 执行。确保以下代码能够正常工作：

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... 此处应能看到输出的行...
```

将股票报价器代码修改如下：

```python
for line in follow('stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

**讨论**

这里发生了一件非常强大的事情。你将一种有趣的迭代模式（在文件末尾读取行）移动到了它自己的小函数中。`follow()` 函数现在成为了一个完全通用的实用工具，你可以在任何程序中使用。例如，你可以用它来监控服务器日志、调试日志以及其他类似的数据源。这相当酷。
