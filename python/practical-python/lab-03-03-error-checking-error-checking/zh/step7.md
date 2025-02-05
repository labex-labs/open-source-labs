# 捕获所有错误

要捕获任何异常，可以像这样使用 `Exception`：

```python
try:
  ...
except Exception:       # 危险。请见下文
    print('An error occurred')
```

一般来说，编写这样的代码不是个好主意，因为你根本不知道它为什么会失败。
