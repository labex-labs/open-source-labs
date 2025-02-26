# Исключения

Исключения используются для сигнализации об ошибках. Чтобы вызвать исключение самостоятельно, используйте оператор `raise`.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

Чтобы перехватить исключение, используйте `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
