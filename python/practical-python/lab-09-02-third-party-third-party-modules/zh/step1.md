# 模块搜索路径

`sys.path` 是一个目录，其中包含 `import` 语句检查的所有目录的列表。查看一下：

```python
>>> import sys
>>> sys.path
... 查看结果...
>>>
```

如果你导入某个内容但它不在这些目录中的任何一个中，你将得到一个 `ImportError` 异常。
