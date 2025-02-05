# 第三方模块

第三方模块通常位于专门的 `site-packages` 目录中。如果你执行与上述相同的步骤，就会看到它：

```python
>>> import numpy
>>> numpy
<module 'numpy' from '/usr/local/lib/python3.6/site-packages/numpy/__init__.py'>
>>>
```

同样，如果你试图弄清楚与 `import` 相关的某些内容为何未按预期工作，查看模块是一个很好的调试技巧。
