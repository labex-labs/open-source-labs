# 理解代码重复问题

让我们先看看 `reader.py` 文件中的现有代码。在编程中，检查现有代码是理解程序运行方式并找出改进点的重要步骤。你可以在 WebIDE 中打开 `reader.py` 文件，有两种方式可以实现。你可以在文件资源管理器中点击该文件，也可以在终端中运行以下命令。这些命令会先导航到项目目录，然后显示 `reader.py` 文件的内容。

```bash
cd ~/project
cat reader.py
```

当你查看代码时，会注意到有两个函数。Python 中的函数是执行特定任务的代码块。以下是这两个函数及其功能：

1. `csv_as_dicts()`：该函数接收 CSV 数据并将其转换为字典列表。Python 中的字典是键值对的集合，对于以结构化方式存储数据很有用。
2. `csv_as_instances()`：该函数接收 CSV 数据并将其转换为实例列表。实例是从类创建的对象，类是创建对象的蓝图。

现在，让我们更仔细地看看这两个函数。你会发现它们非常相似。这两个函数都遵循以下步骤：

- 首先，它们初始化一个空的 `records` 列表。Python 中的列表是可以包含不同类型项的集合。初始化一个空列表意味着创建一个没有任何项的列表，用于存储处理后的数据。
- 然后，它们使用 `csv.reader()` 来解析输入。解析意味着分析输入数据以提取有意义的信息。在这种情况下，`csv.reader()` 帮助我们逐行读取 CSV 数据。
- 它们以相同的方式处理表头。CSV 文件中的表头是第一行，通常包含列名。
- 之后，它们遍历 CSV 数据中的每一行。循环是一种编程结构，允许你多次执行一个代码块。
- 对于每一行，它们对其进行处理以创建一条记录。这条记录可以是字典或实例，具体取决于函数。
- 它们将记录追加到 `records` 列表中。追加意味着将一个项添加到列表的末尾。
- 最后，它们返回 `records` 列表，其中包含所有处理后的数据。

代码重复会带来一些问题，原因如下：

- 代码维护变得更加困难。如果你需要对代码进行更改，就必须在多个地方进行相同的更改，这会花费更多的时间和精力。
- 任何更改都必须在多个地方实现，这增加了你可能会忘记在某个地方进行更改的可能性，从而导致行为不一致。
- 这也增加了引入 bug 的可能性。Bug 是代码中的错误，可能会导致代码出现意外行为。

这两个函数之间唯一真正的区别在于它们如何将一行数据转换为一条记录。这是高阶函数非常有用的典型场景。高阶函数是可以接受另一个函数作为参数或返回一个函数作为结果的函数。

让我们看一些这些函数的示例用法，以便更好地理解它们的工作原理。以下代码展示了如何使用 `csv_as_dicts()` 和 `csv_as_instances()`：

```python
# Example of using csv_as_dicts
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # {'name': 'AA', 'shares': 100, 'price': 32.2}

# Example of using csv_as_instances
class Stock:
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

with open('portfolio.csv') as f:
    portfolio = csv_as_instances(f, Stock)
print(portfolio[0].name, portfolio[0].shares, portfolio[0].price)  # AA 100 32.2
```

在下一步中，我们将创建一个高阶函数来消除这种代码重复。这将使代码更易于维护，并且更不容易出错。
