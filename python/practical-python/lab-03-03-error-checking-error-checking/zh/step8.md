# 捕获错误的错误方式

以下是使用异常的错误方式。

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

这会捕获所有可能的错误，并且当代码由于你完全没有预料到的原因（例如，未安装的 Python 模块等）而失败时，可能会导致无法调试。
