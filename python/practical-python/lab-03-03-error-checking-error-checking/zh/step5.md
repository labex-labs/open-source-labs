# 异常值

异常有一个关联的值。它包含有关错误情况的更具体信息。

```python
raise RuntimeError('Invalid user name')
```

此值是异常实例的一部分，该异常实例会被放入提供给 `except` 的变量中。

```python
try:
 ...
except RuntimeError as e:   # `e` 保存引发的异常
 ...
```

`e` 是异常类型的一个实例。不过，打印时它通常看起来像一个字符串。

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
