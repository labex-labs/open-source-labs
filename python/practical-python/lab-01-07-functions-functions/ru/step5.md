# Генерация исключений

Для генерации исключения используйте оператор `raise`.

```python
raise RuntimeError('What a kerfuffle')
```

Это вызовет аварийное завершение программы с трассировкой стека исключения. Если оно не будет поймано блоком `try-except`.

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
