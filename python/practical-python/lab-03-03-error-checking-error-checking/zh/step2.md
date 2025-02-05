# 异常

异常用于表示错误。要自行引发异常，请使用 `raise` 语句。

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

要捕获异常，请使用 `try-except`。

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
