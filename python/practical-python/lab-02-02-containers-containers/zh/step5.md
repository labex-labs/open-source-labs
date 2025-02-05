# 字典构建

从头开始构建字典的示例。

```python
prices = {} # 初始为空字典

# 插入新项
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

从文件内容填充字典的示例。

```python
prices = {} # 初始为空字典

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

注意：如果你在 `prices.csv` 文件上尝试此操作，你会发现它几乎能正常工作——但文件末尾有一个空行，这会导致程序崩溃。你需要想办法修改代码来处理这个问题（见练习2.6）。
