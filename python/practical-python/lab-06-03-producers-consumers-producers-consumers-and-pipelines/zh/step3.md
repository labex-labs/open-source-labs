# 练习 6.8：设置一个简单的管道

让我们看看管道这个概念是如何实际应用的。编写以下函数：

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

这个函数与上一个练习中的第一个生成器示例几乎完全相同，只是它不再打开文件 —— 它只是对作为参数提供给它的一系列行进行操作。现在，试试这个：

```python
>>> from follow import follow
>>> lines = follow('stocklog.csv')
>>> goog = filematch(lines, 'GOOG')
>>> for line in goog:
        print(line)

... 等待输出...
```

可能需要一些时间才会出现输出，但最终你应该会看到一些包含 GOOG 数据的行。

注意：这些练习必须在两个单独的终端上同时进行。
