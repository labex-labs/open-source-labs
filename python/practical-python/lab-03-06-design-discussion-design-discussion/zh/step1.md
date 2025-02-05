# 文件名与可迭代对象

比较这两个返回相同输出的程序。

```python
# 提供一个文件名
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
         ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# 提供各行内容
def read_data(lines):
    records = []
    for line in lines:
     ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- 你更喜欢这两个函数中的哪一个？为什么？
- 这两个函数中哪一个更灵活？
