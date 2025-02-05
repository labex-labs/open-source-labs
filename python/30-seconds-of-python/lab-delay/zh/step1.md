# 延迟函数执行

编写一个函数 `delay(fn, ms, *args)`，它接受一个函数 `fn`、以毫秒为单位的时间 `ms` 以及任意数量的参数 `args`。该函数应将 `fn` 的执行延迟 `ms` 毫秒，然后使用提供的参数调用它。该函数应返回调用 `fn` 的结果。

要延迟 `fn` 的执行，请使用 `time.sleep()` 函数。此函数接受以秒为单位的数字作为参数，因此在将 `ms` 传递给 `time.sleep()` 之前，你需要将其转换为秒。

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # 一秒后打印 'later'
```
