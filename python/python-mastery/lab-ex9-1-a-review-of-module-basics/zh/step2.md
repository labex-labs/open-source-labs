# 模块加载与系统路径

尝试导入你刚刚创建的模块：

```python
>>> import simplemod
Loaded simplemod
>>> simplemod.foo()
x is 42
>>>
```

如果这因 `ImportError` 而失败，那么你的路径设置有问题。查看 `sys.path` 的值并进行修复。

```python
>>> import sys
>>> sys.path
... 查看结果...
>>>
```
