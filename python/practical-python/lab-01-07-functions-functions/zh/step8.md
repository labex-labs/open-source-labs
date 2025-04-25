# 练习 1.31：错误处理

如果你在一个有缺失字段的文件上尝试使用你的函数，会发生什么？

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

在这个时候，你面临一个抉择。为了让程序正常运行，你可以通过删除坏行来清理原始输入文件，或者修改你的代码以某种方式处理这些坏行。

修改`pcost.py`程序，捕获异常，打印一条警告消息，然后继续处理文件的其余部分。
