# 创建上下文管理器

上下文管理器是 Python 中的一种特殊对象。在 Python 中，对象可以有不同的方法来定义其行为。上下文管理器特别定义了两个重要的方法：`__enter__` 和 `__exit__`。这些方法与 `with` 语句一起使用。`with` 语句用于为一段代码设置特定的上下文。可以将其看作是创建一个小环境，在这个环境中会发生某些事情，当代码块执行完毕后，上下文管理器会负责清理工作。

在这一步中，我们将创建一个具有非常实用功能的上下文管理器。它将临时重定向标准输出（`sys.stdout`）。标准输出是 Python 程序的正常输出所指向的地方，通常是控制台。通过重定向它，我们可以将输出发送到文件中。当你想保存原本只会显示在控制台的输出时，这非常有用。

首先，我们需要创建一个新文件来编写上下文管理器代码。我们将这个文件命名为 `redirect.py`。你可以在终端中使用以下命令创建它：

```bash
touch /home/labex/project/redirect.py
```

现在文件已经创建好了，在编辑器中打开它。打开后，将以下 Python 代码添加到文件中：

```python
import sys

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
```

让我们来分析一下这个上下文管理器的作用：

1. `__init__`：这是初始化方法。当我们创建 `redirect_stdout` 类的实例时，会传入一个文件对象。这个方法将该文件对象存储在实例变量 `self.out_file` 中。这样，它就记住了我们要将输出重定向到的位置。
2. `__enter__`：
   - 首先，它保存当前的 `sys.stdout`。这很重要，因为我们稍后需要恢复它。
   - 然后，它将当前的 `sys.stdout` 替换为我们的文件对象。从这一点开始，任何原本会输出到控制台的内容都将输出到文件中。
   - 最后，它返回文件对象。这很有用，因为我们可能想在 `with` 代码块中使用这个文件对象。
3. `__exit__`：
   - 这个方法恢复原来的 `sys.stdout`。因此，在 `with` 代码块执行完毕后，输出将像往常一样回到控制台。
   - 它接受三个参数：异常类型（`ty`）、异常值（`val`）和回溯信息（`tb`）。这些参数是上下文管理器协议所要求的。它们用于处理 `with` 代码块中可能发生的任何异常。

现在，让我们测试一下我们的上下文管理器。我们将使用它将表格的输出重定向到一个文件中。首先，启动 Python 解释器：

```bash
python3
```

然后，在解释器中运行以下 Python 代码：

```python
>>> import stock, reader, tableformat
>>> from redirect import redirect_stdout
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
...     tableformat.print_table(portfolio, ['name','shares','price'], formatter)
...     file.close()
...
>>> # Let's check the content of the output file
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

太棒了！我们的上下文管理器按预期工作。它成功地将表格输出重定向到了 `out.txt` 文件中。

上下文管理器是 Python 中非常强大的特性。它们有助于你正确地管理资源。以下是上下文管理器的一些常见用例：

- 文件操作：当你打开一个文件时，上下文管理器可以确保文件被正确关闭，即使发生错误也不例外。
- 数据库连接：它可以确保在你使用完数据库连接后将其关闭。
- 线程程序中的锁：上下文管理器可以以安全的方式处理资源的加锁和解锁。
- 临时更改环境设置：你可以为一段代码更改某些设置，然后自动恢复它们。

这种模式非常重要，因为它确保了即使在 `with` 代码块中发生异常，资源也能被正确清理。

测试完成后，你可以退出 Python 解释器：

```python
>>> exit()
```
