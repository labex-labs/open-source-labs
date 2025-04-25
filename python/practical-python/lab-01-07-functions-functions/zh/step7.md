# 练习 1.30：将脚本转换为函数

把你在练习 1.27 中为`pcost.py`程序编写的代码，转换成一个名为`portfolio_cost(filename)`的函数。这个函数以文件名作为输入，读取该文件中的投资组合数据，并返回投资组合的总成本，以浮点数形式表示。

为了使用你的函数，修改你的程序，使其看起来像这样：

```python
# pcost.py
def portfolio_cost(filename):
    """
    计算投资组合文件的总成本（股数*价格）
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("输入一个文件名：")

cost = portfolio_cost(filename)
print("总成本：", cost)
```

当你运行你的程序时，你应该会看到和之前一样的输出。运行程序之后，你还可以通过输入以下内容，在交互式环境中调用你的函数：

```bash
$ python3 -i pcost.py
```

这将允许你在交互式模式下调用你的函数。

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

能够在交互式环境中试验你的代码，对于测试和调试很有用。
