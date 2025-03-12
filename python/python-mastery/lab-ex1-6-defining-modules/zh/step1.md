# 理解 Python 模块

在 Python 中，模块就像是一个容器，用于存放 Python 定义和语句。它本质上是一个文件，文件名就是模块名，后面加上 `.py` 扩展名。可以把模块想象成工具箱，它们能帮助你以逻辑的方式组织 Python 代码，使其更易于复用和维护。就像你会把不同的工具放在不同的盒子里以便更好地整理一样，你可以将相关的 Python 代码分组到不同的模块中。

让我们来看看为这个实验准备的文件：

1. 首先，我们将在编辑器中打开 `stock.py` 文件，看看里面的内容。为此，我们将使用以下命令。`cd` 命令用于将目录更改为 `project` 文件夹，我们的文件就位于该文件夹中，`cat` 命令用于显示文件的内容。

```bash
cd ~/project
cat stock.py
```

这个 `stock.py` 文件定义了一个 `Stock` 类。类就像是创建对象的蓝图。在这种情况下，`Stock` 类代表一支股票。它有股票名称、股数和价格等属性（类似于特征），还有一个用于计算股票成本的方法（类似于与类关联的函数）。

2. 接下来，让我们查看 `pcost.py` 文件。我们将再次使用 `cat` 命令来查看其内容。

```bash
cat pcost.py
```

这个文件定义了一个名为 `portfolio_cost()` 的函数。函数是执行特定任务的代码块。`portfolio_cost()` 函数读取一个投资组合文件，并计算该投资组合中所有股票的总成本。

3. 现在，让我们看看示例投资组合数据。我们将使用 `cat` 命令查看 `portfolio.dat` 文件的内容。

```bash
cat portfolio.dat
```

这个文件以简单的格式包含股票数据。每行包含股票的代码、股数和每股价格。

## 使用 `import` 语句

Python 的 `import` 语句是一个强大的工具，它允许你在当前程序中使用其他模块的代码。这就像从其他工具箱中借用工具一样。让我们练习以不同的方式导入代码：

1. 首先，我们需要启动 Python 解释器。Python 解释器是执行 Python 代码的程序。我们将使用以下命令启动它。

```bash
python3
```

2. 现在，让我们导入 `pcost` 模块，看看会发生什么。当我们使用 `import` 语句时，Python 会查找 `pcost.py` 文件，并使其中的代码可供我们使用。

```python
import pcost
```

你应该会看到输出 `44671.15`。这是根据 `portfolio.dat` 文件计算出的投资组合成本。当 `pcost` 模块被导入时，`pcost.py` 文件底部的代码会自动运行。

3. 让我们尝试使用不同的投资组合文件调用 `portfolio_cost()` 函数。我们将使用 `pcost.portfolio_cost()` 语法从 `pcost` 模块调用该函数。

```python
pcost.portfolio_cost('portfolio2.dat')
```

输出应该是 `19908.75`，这代表第二个投资组合文件中股票的总成本。

4. 现在，让我们从 `stock` 模块导入特定的类。我们可以使用 `from...import` 语句只导入 `Stock` 类，而不是导入整个模块。

```python
from stock import Stock
```

5. 导入 `Stock` 类后，我们可以创建一个 `Stock` 对象。对象是类的实例。我们将创建一个名为 `GOOG`、有 100 股、价格为 `490.10` 的 `Stock` 对象。然后，我们将打印股票名称并使用 `cost()` 方法计算其成本。

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
```

输出应该是：

```
GOOG
49010.0
```

6. 最后，当我们使用完 Python 解释器后，可以使用 `exit()` 函数退出。

```python
exit()
```

这个实验展示了两种不同的导入 Python 代码的方式：

- `import module_name` - 这会导入整个模块，使该模块中的所有函数、类和变量都可供使用。
- `from module_name import specific_item` - 这只从模块中导入特定的项（如类或函数），如果你只需要模块的部分功能，这种方式很有用。
