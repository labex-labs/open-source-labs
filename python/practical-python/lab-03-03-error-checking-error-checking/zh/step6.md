# 捕获多种错误

你可以使用多个 `except` 块来捕获不同类型的异常。

```python
try:
...
except LookupError as e:
...
except RuntimeError as e:
...
except IOError as e:
...
except KeyboardInterrupt as e:
...
```

或者，如果处理这些异常的语句相同，你可以将它们分组：

```python
try:
...
except (IOError,LookupError,RuntimeError) as e:
...
```
