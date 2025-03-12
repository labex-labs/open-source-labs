# 使用你的元类

现在，我们将通过继承创建一个使用我们元类的类。这将帮助我们理解在定义类时元类是如何被调用的。

在 Python 中，元类是用于创建其他类的类。当你定义一个类时，Python 会使用一个元类来构造该类对象。通过使用继承，我们可以指定一个类应该使用哪个元类。

1. 打开 `mymeta.py` 文件，并在文件末尾添加以下代码：

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

在这里，我们定义了一个 `Stock` 类，它继承自 `myobject`。`__init__` 方法是 Python 类中的一个特殊方法，在创建类的对象时会被调用，用于初始化对象的属性。`cost` 方法用于计算股票的总成本，`sell` 方法用于减少股票的数量。

2. 按下 Ctrl+S 保存文件。保存文件可确保你所做的更改被保存，并且稍后可以运行。

3. 现在让我们运行这个文件，看看会发生什么。在 WebIDE 中打开一个终端并运行以下命令：

```bash
cd /home/labex/project
python3 mymeta.py
```

`cd` 命令将当前工作目录更改为 `/home/labex/project`，`python3 mymeta.py` 则运行 Python 脚本 `mymeta.py`。

你应该会看到类似以下的输出：

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

这个输出表明，在创建 `myobject` 和 `Stock` 类时，我们的元类都被调用了。注意以下几点：

- 对于 `Stock` 类，其基类包含 `myobject`，因为 `Stock` 继承自 `myobject`。
- 属性列表包含了我们定义的所有方法（`__init__`、`cost`、`sell`）以及一些默认属性。

4. 让我们与 `Stock` 类进行交互。创建一个名为 `test_stock.py` 的新文件，内容如下：

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

在这段代码中，我们从 `mymeta` 模块中导入 `Stock` 类，然后创建一个名为 `apple` 的 `Stock` 类实例。我们使用 `Stock` 类的方法来打印股票信息、计算总成本、卖出一些股票，然后打印更新后的信息。

5. 运行这个文件来测试我们的 `Stock` 类：

```bash
python3 test_stock.py
```

你应该会看到类似以下的输出：

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

注意，我们的元类信息会先被打印出来，然后才是测试脚本的输出。这是因为元类在类被定义时就会被调用，而类的定义发生在测试脚本中的代码执行之前。
