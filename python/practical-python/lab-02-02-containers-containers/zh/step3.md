# 列表构建

从头开始创建一个列表。

```python
records = []  # 初始为空列表

# 使用.append() 添加更多项
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

从文件读取记录时的一个示例。

```python
records = []  # 初始为空列表

with open('portfolio.csv', 'rt') as f:
    next(f) # 跳过标题行
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
