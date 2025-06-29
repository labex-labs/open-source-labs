# 创建协程管道组件

在这一步中，我们将创建更多用于处理股票数据的专用协程（coroutine）。协程是一种特殊类型的函数，它可以暂停和恢复执行，这对于构建数据处理管道非常有用。我们创建的每个协程都将在整个处理管道中执行特定的任务。

1. 首先，你需要创建一个新文件。导航到 `/home/labex/project` 目录并创建一个名为 `coticker.py` 的文件。这个文件将包含我们基于协程的数据处理的所有代码。

2. 现在，让我们开始在 `coticker.py` 文件中编写代码。我们首先导入必要的模块并定义基本结构。模块是预先编写的代码库，提供有用的函数和类。以下代码实现了这一点：

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. 当你查看上面的代码时，会注意到有与 `String()`、`Float()` 和 `Integer()` 相关的错误。这些是我们需要导入的类。因此，我们将在文件顶部添加所需的导入语句。这样，Python 就知道在哪里可以找到这些类。以下是更新后的代码：

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. 接下来，我们将添加构成数据处理管道的协程组件。每个协程在管道中都有特定的任务。以下是添加这些协程的代码：

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. 让我们来理解每个协程的作用：
   - `to_csv`：它的任务是将原始文本行转换为解析后的 CSV 行。这很重要，因为我们的数据最初是文本格式，我们需要将其拆分为结构化的 CSV 数据。
   - `create_ticker`：这个协程接收 CSV 行并从中创建 `Ticker` 对象。`Ticker` 对象以更有条理的方式表示股票数据。
   - `negchange`：它对 `Ticker` 对象进行过滤。它只传递价格变化为负的股票。这有助于我们关注那些正在贬值的股票。
   - `ticker`：这个协程对行情数据进行格式化并显示。它使用格式化器将数据以美观、易读的表格形式呈现。

6. 最后，我们需要添加将所有这些组件连接在一起的主程序代码。这段代码将设置数据在管道中的流动。以下是代码：

```python
if __name__ == '__main__':
    import sys

    # 定义要显示的字段名称
    fields = ['name', 'price', 'change']

    # 创建处理管道
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # 将管道连接到数据源
    follow('stocklog.csv', csv_parser)
```

7. 编写完所有代码后，保存 `coticker.py` 文件。然后，打开终端并运行以下命令。`cd` 命令将目录更改为我们文件所在的位置，`python3` 命令运行我们的 Python 脚本：

```bash
cd /home/labex/project
python3 coticker.py
```

8. 如果一切顺利，你应该会在终端中看到一个格式化的表格。这个表格显示了价格变化为负的股票。输出将类似于以下内容：

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

请记住，表格中的实际值可能会根据生成的股票数据而有所不同。

## 理解管道流程

这个程序最重要的部分是数据如何通过协程流动。让我们逐步分解：

1. `follow` 函数首先从 `stocklog.csv` 文件中读取行。这是我们的数据源。
2. 读取的每一行随后被发送到 `csv_parser` 协程。`csv_parser` 接收原始文本行并将其解析为 CSV 字段。
3. 解析后的 CSV 数据随后被发送到 `tick_creator` 协程。这个协程从 CSV 行创建 `Ticker` 对象。
4. `Ticker` 对象随后被发送到 `neg_filter` 协程。这个协程检查每个 `Ticker` 对象。如果股票的价格变化为负，它就传递该对象；否则，它将其丢弃。
5. 最后，经过过滤的 `Ticker` 对象被发送到 `ticker` 协程。`ticker` 协程对数据进行格式化并以表格形式显示。

这种管道架构非常有用，因为它允许每个组件专注于单一任务。这使得代码更具模块化，意味着它更易于理解、修改和维护。
