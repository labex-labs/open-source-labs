# 练习 1.33：从命令行读取

在`pcost.py`程序中，输入文件的名称被硬编码到了代码中：

```python
# pcost.py

def portfolio_cost(filename):
 ...
    # 你的代码在这里
 ...

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)
```

这对于学习和测试来说没问题，但在实际程序中你可能不会这样做。

相反，你可能会将文件名作为参数传递给脚本。尝试将程序的底部部分修改如下：

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    计算投资组合文件的总成本（股数*价格）
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # 跳过标题行
        for row in rows:
            if len(row) < 3:
                print("跳过无效行：", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("跳过无效行：", row)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
```

`sys.argv`是一个列表，它包含命令行上传递的参数（如果有的话）。

要运行你的程序，你需要在终端中运行 Python。

例如，在 Unix 上的 bash 中：

```bash
$ python3 pcost.py portfolio.csv
Total cost: 44671.15
bash %
```
