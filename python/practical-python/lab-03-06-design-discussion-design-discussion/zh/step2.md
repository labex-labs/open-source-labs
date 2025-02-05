# 深度理解：“鸭子类型”

[鸭子类型](https://en.wikipedia.org/wiki/Duck_typing) 是一种计算机编程概念，用于确定一个对象是否可用于特定目的。它是 [鸭子测试](https://en.wikipedia.org/wiki/Duck_test) 的一种应用。

> 如果它看起来像鸭子，游泳方式像鸭子，叫声也像鸭子，那么它很可能就是一只鸭子。

在上述 `read_data()` 的第二个版本中，该函数期望的是任何可迭代对象，而不仅仅是文件的各行。

```python
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records
```

这意味着我们可以将它用于其他的“行”。

```python
# 一个CSV文件
lines = open('data.csv')
data = read_data(lines)

# 一个压缩文件
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# 标准输入
lines = sys.stdin
data = read_data(lines)

# 一个字符串列表
lines = ['ACME,50,91.1','IBM,75,123.45',... ]
data = read_data(lines)
```

这种设计具有相当大的灵活性。

_问题：我们应该接受还是抵制这种灵活性？_
