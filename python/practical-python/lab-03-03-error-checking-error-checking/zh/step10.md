# 重新引发异常

使用 `raise` 来传播捕获到的错误。

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

这使你能够采取行动（例如记录日志）并将错误传递给调用者。
