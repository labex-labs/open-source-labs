# 读取文件数据的常见用法

一次性将整个文件作为字符串读取。

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` 是一个包含 `foo.txt` 中所有文本的字符串
```

通过迭代逐行读取文件。

```python
with open(filename, 'rt') as file:
    for line in file:
        # 处理该行
```
