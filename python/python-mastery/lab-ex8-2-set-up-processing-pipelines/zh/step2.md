# 创建 Ticker 类

在数据处理中，处理原始数据可能颇具挑战。为了让我们对股票数据的处理更加有序和高效，我们将定义一个合适的类来表示股票报价。这个类将作为我们股票数据的蓝图，使我们的数据处理管道更加健壮且易于管理。

## 创建 ticker.py 文件

1. 首先，你需要在 WebIDE 中创建一个新文件。你可以点击“New File”图标，或者在文件资源管理器中右键单击并选择“New File”。将这个文件命名为 `ticker.py`。这个文件将包含我们 `Ticker` 类的代码。

2. 现在，将以下代码添加到你新创建的 `ticker.py` 文件中。这段代码将定义我们的 `Ticker` 类，并设置一个简单的处理管道来测试它。

```python
# ticker.py

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

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

3. 添加代码后，保存文件。你可以按 `Ctrl+S`，或者从菜单中选择“File” → “Save”。保存文件可确保你的更改得以保留，并且之后可以运行。

## 代码解析

让我们逐步详细了解这段代码的功能：

1. 在代码开头，我们从 `structure.py` 模块导入 `Structure` 和字段类型。这个模块已经为你设置好了。这些导入非常重要，因为它们为我们的 `Ticker` 类提供了构建块。`Structure` 类将作为我们 `Ticker` 类的基类，而 `String`、`Float` 和 `Integer` 等字段类型将定义我们股票数据字段的数据类型。

2. 接下来，我们定义一个继承自 `Structure` 的 `Ticker` 类。这个类有几个字段，代表了股票数据的不同方面：

   - `name`：这个字段存储股票代码，例如“IBM”或“AAPL”。它帮助我们识别所处理的是哪家公司的股票。
   - `price`：它保存股票的当前价格。这对投资者来说是至关重要的信息。
   - `date` 和 `time`：这些字段告诉我们股票报价的生成时间。了解时间和日期对于分析股票价格随时间的走势很重要。
   - `change`：这代表股票的价格变化。它显示了与之前某个时间点相比，股票价格是上涨还是下跌。
   - `open`、`high`、`low`：这些字段分别代表股票在某一时期的开盘价、最高价和最低价。它们让我们了解股票的价格范围。
   - `volume`：这个字段存储交易的股票数量。高交易量可能表明市场对某只特定股票有强烈的兴趣。

3. 在 `if __name__ == '__main__':` 代码块中，我们设置了一个处理管道。当我们直接运行 `ticker.py` 文件时，这段代码将被执行。
   - `follow('stocklog.csv')` 是一个函数，它从 `stocklog.csv` 文件中生成行。它允许我们逐行读取文件。
   - `csv.reader(lines)` 获取这些行并将它们解析为行数据。CSV（逗号分隔值）是一种常见的用于存储表格数据的文件格式，这个函数帮助我们从每行中提取数据。
   - `(Ticker.from_row(row) for row in rows)` 是一个生成器表达式。它将每行数据转换为一个 `Ticker` 对象。这样，我们就将原始的 CSV 数据转换为更易于处理的结构化对象。
   - `for` 循环遍历这些 `Ticker` 对象并打印每个对象。这让我们可以看到结构化数据的实际效果。

## 运行代码

让我们运行代码，看看它是如何工作的：

1. 首先，你需要确保在终端中位于项目目录。如果你还不在该目录，可以使用以下命令导航到那里：

   ```bash
   cd /home/labex/project
   ```

2. 一旦你位于正确的目录中，使用以下命令运行 `ticker.py` 脚本：

   ```bash
   python3 ticker.py
   ```

3. 运行脚本后，你应该会看到类似以下的输出（你的数据会有所不同）：
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

当你看到足够的输出后，可以按 `Ctrl+C` 停止脚本的执行。

注意原始的 CSV 数据是如何被转换为结构化的 `Ticker` 对象的。这种转换使得数据在我们的处理管道中更易于处理，因为我们现在可以使用 `Ticker` 类中定义的字段来访问和操作股票数据。
