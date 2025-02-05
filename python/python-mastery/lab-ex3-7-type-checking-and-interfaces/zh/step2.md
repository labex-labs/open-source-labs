# 抽象基类

修改`TableFormatter`基类，使其使用`abc`模块定义为一个恰当的抽象基类。完成此操作后，尝试进行以下实验：

```python
>>> class NewFormatter(TableFormatter):
        def headers(self, headings):
            pass
        def row(self, rowdata):
            pass

>>> f = NewFormatter()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 无法实例化具有抽象方法headings的抽象类NewFormatter
>>>
```

在此处，抽象基类捕获到了类中的一个拼写错误——即`headings()`方法被错误地写成了`headers()`。
