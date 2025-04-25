# 练习 1.26：文件基础操作

首先，尝试一次性将整个文件作为一个大字符串读取：

```python
>>> with open('portfolio.csv', 'rt') as f:
        data = f.read()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

在上述示例中，需要注意的是 Python 有两种输出模式。在第一种模式下，当你在提示符处输入 `data` 时，Python 会向你展示原始字符串表示形式，包括引号和转义码。当你输入 `print(data)` 时，你会得到字符串的实际格式化输出。

虽然一次性读取整个文件很简单，但这通常不是最合适的方法 —— 特别是当文件非常大或者包含你想要一次处理一行的文本行时。

要逐行读取文件，可以使用如下的 `for` 循环：

```python
>>> with open('portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

当你像这样使用这段代码时，行会一直被读取，直到到达文件末尾，此时循环停止。

在某些情况下，你可能想要手动读取或跳过 _一行_ 文本（例如，也许你想要跳过第一行的列标题）。

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()` 会返回文件中的下一行文本。如果你重复调用它，你会得到连续的行。不过，要知道，`for` 循环已经在使用 `next()` 来获取其数据了。因此，通常你不会直接调用它，除非你像这样试图明确地跳过或读取一行。

一旦你开始读取文件的行，你就可以开始进行更多的处理，比如分割。例如，试试这个：

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name','shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
```

_注意：在这些示例中，显式调用了 `f.close()`，因为没有使用 `with` 语句。_
