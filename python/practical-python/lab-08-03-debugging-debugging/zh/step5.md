# Python调试器

你可以在程序中手动启动调试器。

```python
def some_function():
 ...
    breakpoint()      # 进入调试器（Python 3.7+）
 ...
```

这会在`breakpoint()`调用处启动调试器。

在早期的Python版本中，你是这样做的。你有时会在其他调试指南中看到这种方法。

```python
import pdb
...
pdb.set_trace()       # 代替 `breakpoint()`
...
```
