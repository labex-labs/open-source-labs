# 文本的基本内存使用情况

让我们获取处理这个数据文件所需内存的基线。首先，重启Python并尝试一个非常简单的实验，即简单地读取文件并将其数据存储在一个字符串中：

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('ctabus.csv')
>>> tracemalloc.start()
>>> data = f.read()
>>> len(data)
12361039
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
12369664
>>> peak
24730766
>>>
```

你的结果可能会有所不同，但你应该会看到当前内存使用量在12MB左右，峰值为24MB。

如果你将整个文件读入字符串列表中会发生什么呢？重启Python并尝试这个：

```python
>>> # --- RESTART
>>> import tracemalloc
>>> f = open('/home/labex/project/ctabus.csv')
>>> tracemalloc.start()
>>> lines = f.readlines()
>>> len(lines)
577564
>>> current, peak = tracemalloc.get_traced_memory()
>>> current
45828030
>>> peak
45867371
>>>
```

你应该会看到内存使用量显著增加到40 - 50MB的范围。值得思考的问题是：额外开销的来源可能是什么？
