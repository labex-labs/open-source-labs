# 写入文件的常见用法

写入字符串数据。

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
 ...
```

重定向 `print` 函数。

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
 ...
```

这些练习依赖于一个名为 `portfolio.csv` 的文件。该文件包含一系列行，每行都有关于一个股票投资组合的信息。假设你在 `~/project/` 目录下工作。如果你不确定，可以通过以下方式查看 Python 认为它正在运行的位置：

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # 输出可能不同
>>>
```
