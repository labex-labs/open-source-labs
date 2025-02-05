# 练习6.5：监控流数据源

生成器可以是一种监控实时数据源（如日志文件或股票市场数据馈送）的有趣方式。在本部分中，我们将探讨这个想法。首先，请仔细按照以下说明操作。

程序 `stocksim.py` 是一个模拟股票市场数据的程序。作为输出，该程序会不断将实时数据写入文件 `stocklog.csv`。在一个单独的命令窗口中，进入该目录并运行此程序：

```bash
$ python3 stocksim.py
```

如果你使用的是Windows，只需找到 `stocksim.py` 程序并双击运行它。现在，先不管这个程序（让它运行就行）。在另一个窗口中，查看模拟器正在写入的文件 `stocklog.csv`。你应该会看到每隔几秒就会有新的文本行添加到文件中。同样，就让这个程序在后台运行——它会运行几个小时（你无需担心它）。

一旦上述程序运行起来，让我们编写一个小程序来打开该文件，定位到文件末尾，并监视新的输出。创建一个文件 `follow.py` 并将以下代码放入其中：

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # 将文件指针从文件末尾移动0个字节

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
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

如果你运行该程序，你将看到一个实时股票报价器。在底层，这段代码有点类似于用于监视日志文件的Unix `tail -f` 命令。

注意：在这个示例中使用 `readline()` 方法有点不寻常，因为它不是从文件中读取行的常用方式（通常你会使用 `for` 循环）。然而，在这种情况下，我们使用它来反复探测文件末尾，看看是否有更多数据被添加（`readline()` 要么返回新数据，要么返回一个空字符串）。
