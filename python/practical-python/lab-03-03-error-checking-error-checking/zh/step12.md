# `finally` 语句

它指定了无论是否发生异常都必须运行的代码。

```python
lock = Lock()
...
lock.acquire()
try:
  ...
finally:
    lock.release()  # 这将始终被执行。无论是否有异常。
```

通常用于安全地管理资源（特别是锁、文件等）。
