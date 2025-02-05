# 重复加载模块

要确保你理解模块只会被加载一次。尝试重复导入并注意你不会再看到 `print` 函数的输出：

```python
>>> import simplemod
>>>
```

尝试更改 `x` 的值，看看重复导入没有效果。

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> import simplemod
>>> simplemod.x
13
>>>
```

如果你想强制重新加载模块，可以使用 `importlib.reload()`。

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module'simplemod' from'simplemod.py'>
>>> simplemod.x
42
>>>
```

`sys.modules` 是所有已加载模块的字典。查看一下它，删除你的模块，然后尝试重复导入。

```python
>>> sys.modules
... 查看输出...
>>> sys.modules['simplemod']
<module'simplemod' from'simplemod.py'>
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>>
```
