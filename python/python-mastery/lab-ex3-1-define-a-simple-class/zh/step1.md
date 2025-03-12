# 为 Stock 类添加 sell 方法

在这一步中，我们将通过添加一个新方法来增强 `Stock` 类。方法类似于属于某个类的特殊函数，它可以对从该类创建的对象进行操作。我们将创建一个名为 `sell(nshares)` 的方法，该方法将帮助我们模拟出售股票的操作。当你出售股票时，你持有的股票数量会减少，这个方法将为我们处理这种数量的减少。

## 什么是方法？

让我们首先了解一下什么是方法。方法是定义在类内部的函数。它旨在对该类的实例（类似于单个副本）进行操作。当在对象上调用方法时，它可以访问该对象的所有属性（特征）。这是通过 `self` 参数实现的。`self` 参数是对调用该方法的对象的引用。因此，当你在方法内部使用 `self` 时，你指的是该方法正在操作的特定对象。

## 实现说明

1. 首先，你需要在编辑器中打开 `stock.py` 文件。为此，我们将使用命令行。打开你的终端并运行以下命令。此命令将目录更改为包含 `stock.py` 文件的 `project` 文件夹。

```bash
cd ~/project
```

2. 打开 `stock.py` 文件后，你需要在 `Stock` 类中找到一个特定的注释。查找注释 `# TODO: Add sell(nshares) method here`。这个注释是一个占位符，指示我们应该在哪里添加新的 `sell` 方法。

3. 现在，是时候添加 `sell` 方法了。这个方法将接受一个名为 `nshares` 的参数，该参数表示你要出售的股票数量。这个方法的主要任务是将 `Stock` 对象的 `shares` 属性减少你要出售的股票数量。

以下是你需要添加的 `sell` 方法的代码：

```python
def sell(self, nshares):
    self.shares -= nshares
```

在这段代码中，`self.shares` 指的是 `Stock` 对象的 `shares` 属性。`-=` 运算符从 `self.shares` 的当前值中减去 `nshares` 的值。

4. 添加 `sell` 方法后，你需要保存 `stock.py` 文件。你可以通过按下键盘上的 `Ctrl+S` 组合键，或者在编辑器的菜单中选择“文件 > 保存”来完成保存操作。

5. 为了确保我们的 `sell` 方法能正常工作，我们将创建一个测试脚本。创建一个名为 `test_sell.py` 的新 Python 文件，并在其中添加以下代码：

```python
# test_sell.py
from stock import Stock

# Create a stock object
s = Stock('GOOG', 100, 490.10)
print(f"Initial shares: {s.shares}")

# Sell 25 shares
s.sell(25)
print(f"Shares after selling: {s.shares}")
```

在这个脚本中，我们首先从 `stock.py` 文件中导入 `Stock` 类。然后，我们创建一个名为 `s` 的 `Stock` 对象，其股票代码为 `GOOG`，持有 100 股，价格为 490.10。我们打印初始的股票数量。之后，我们在 `s` 对象上调用 `sell` 方法来出售 25 股。最后，我们打印出售后的股票数量。

6. 现在，我们将运行测试脚本，看看我们的 `sell` 方法是否按预期工作。再次打开你的终端并运行以下命令：

```bash
python3 test_sell.py
```

如果一切正常，你应该会看到类似于以下的输出：

```
Initial shares: 100
Shares after selling: 75
```

这个输出确认了我们的 `sell` 方法工作正常。它已成功将股票数量减少了我们指定的数量。
