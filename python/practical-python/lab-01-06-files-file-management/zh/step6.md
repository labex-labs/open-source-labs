# 练习 1.28：其他类型的“文件”

如果你想读取一个非文本文件，比如一个 gzip 压缩的数据文件，该怎么办呢？内置的 `open()` 函数在这里帮不了你，但 Python 有一个库模块 `gzip`，它可以读取 gzip 压缩文件。

试试看：

```python
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... 查看输出结果...
>>>
```

注意：这里包含 `'rt'` 文件模式至关重要。如果你忘了这一点，你得到的将是字节串而不是普通的文本字符串。
