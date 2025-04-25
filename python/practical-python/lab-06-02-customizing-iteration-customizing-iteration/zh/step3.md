# 练习 6.4：一个简单的生成器

如果你发现自己想要自定义迭代，那么你应该始终考虑生成器函数。它们很容易编写——创建一个执行所需迭代逻辑的函数，并使用 `yield` 来发出值。

例如，试试这个在文件中搜索包含匹配子字符串的行的生成器：

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

这有点意思——你可以将一堆自定义处理隐藏在一个函数中，并使用它来为 for 循环提供数据。下一个示例将看看一个更不寻常的情况。
