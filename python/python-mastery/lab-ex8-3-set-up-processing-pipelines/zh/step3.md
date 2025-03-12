# 增强协程管道

既然我们已经有了一个基本的管道并使其运行起来，现在是时候让它变得更加灵活了。在编程中，灵活性至关重要，因为它能让我们的代码适应不同的需求。我们将通过修改 `coticker.py` 程序来支持各种过滤和格式化选项，从而实现这一目标。

1. 首先，在你的代码编辑器中打开 `coticker.py` 文件。代码编辑器是你对程序进行所有必要修改的地方。它为你查看、编辑和保存代码提供了一个便捷的环境。

2. 接下来，我们将添加一个新的协程，用于按股票名称过滤数据。协程是一种特殊类型的函数，它可以暂停和恢复执行。这使我们能够创建一个管道，让数据可以流经不同的处理步骤。以下是新协程的代码：

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

在这段代码中，`filter_by_name` 协程接受一个股票名称和一个目标协程作为参数。它使用 `yield` 关键字持续等待一条记录。当一条记录到达时，它会检查该记录的名称是否与指定的名称匹配。如果匹配，它就将该记录发送到目标协程。

3. 现在，让我们添加另一个基于价格阈值进行过滤的协程。这个协程将帮助我们选择特定价格范围内的股票。以下是代码：

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

与前一个协程类似，`price_threshold` 协程等待一条记录。然后，它检查该记录的价格是否在指定的最低和最高价格范围内。如果是，它就将该记录发送到目标协程。

4. 添加新的协程后，我们需要更新主程序以演示这些额外的过滤器。主程序是我们应用程序的入口点，在这里我们设置处理管道并启动数据流。以下是更新后的代码：

```python
if __name__ == '__main__':
    import sys

    # 定义要显示的字段名称
    fields = ['name', 'price', 'change', 'high', 'low']

    # 创建具有多个输出的处理管道

    # 管道 1：显示所有价格下跌的股票（与之前相同）
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # 启动第一个管道来跟踪文件
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # 等待片刻以查看一些结果
    import time
    time.sleep(5)

    # 管道 2：按名称过滤（AAPL）
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # 用第二个管道跟踪文件
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # 等待片刻以查看一些结果
    time.sleep(5)

    # 管道 3：按价格范围过滤
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # 用第三个管道跟踪文件
    follow('stocklog.csv', csv_parser3)
```

在这个更新后的代码中，我们创建了三个不同的处理管道。第一个管道显示价格下跌的股票，第二个管道按名称 'AAPL' 过滤股票，第三个管道根据 50 到 75 之间的价格范围过滤股票。我们使用线程并发运行前两个管道，这使我们能够更高效地处理数据。

5. 完成所有修改后，保存文件。保存文件可确保你所有的修改都被保留。然后，在终端中使用以下命令运行更新后的程序：

```bash
cd /home/labex/project
python3 coticker.py
```

`cd` 命令将当前目录更改为项目目录，`python3 coticker.py` 命令运行 Python 程序。

6. 运行程序后，你应该会看到三种不同的输出：
   - 首先，你会看到价格下跌的股票。
   - 然后，你会看到所有 AAPL 股票的更新信息。
   - 最后，你会看到所有价格在 50 到 75 之间的股票。

## 理解增强后的管道

增强后的程序展示了几个重要的概念：

1. **多个管道**：我们可以从同一个数据源创建多个处理管道。这使我们能够同时对同一数据进行不同类型的分析。
2. **专用过滤器**：我们可以为特定的过滤任务创建不同的协程。这些过滤器帮助我们只选择符合特定标准的数据。
3. **并发处理**：使用线程，我们可以并发运行多个管道。这通过允许程序并行处理数据来提高程序的效率。
4. **管道组合**：协程可以以不同的方式组合，以实现不同的数据处理目标。这使我们能够根据自己的需求自定义数据处理管道。

这种方法为处理流式数据提供了一种灵活且模块化的方式。它允许你在不改变程序整体架构的情况下添加或修改处理步骤。
