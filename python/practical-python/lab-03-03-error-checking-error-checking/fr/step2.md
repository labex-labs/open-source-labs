# Exceptions

Les exceptions sont utilisées pour signaler des erreurs. Pour lever une exception vous-même, utilisez l'instruction `raise`.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

Pour attraper une exception, utilisez `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
