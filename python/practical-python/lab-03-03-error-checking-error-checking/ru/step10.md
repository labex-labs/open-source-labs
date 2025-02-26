# Переброс исключения

Используйте `raise`, чтобы распространить пойманную ошибку.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

Это позволяет вам предпринять действия (например, логирование) и передать ошибку вызывающему.
