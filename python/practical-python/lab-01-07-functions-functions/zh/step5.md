# 引发异常

要引发异常，可使用 `raise` 语句。

```python
raise RuntimeError('What a kerfuffle')
```

这将导致程序因异常回溯而中止。除非被 `try-except` 块捕获。

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
