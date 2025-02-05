# `itertools` 模块

`itertools` 是一个库模块，包含各种用于帮助处理迭代器/生成器的函数。

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1,... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1,..., sN)
```

所有函数都以迭代方式处理数据。它们实现了各种迭代模式。

更多信息请参考 PyCon '08 的教程 [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) 。

在之前的练习中，你编写了一些代码来跟踪写入日志文件的行，并将它们解析成一系列行。本练习在此基础上继续进行。确保 `stocksim.py` 仍在运行。
