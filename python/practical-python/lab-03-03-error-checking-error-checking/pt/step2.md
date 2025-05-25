# Exceções (Exceptions)

Exceções são usadas para sinalizar erros. Para lançar uma exceção (raise an exception) você mesmo, use a instrução `raise`.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

Para capturar uma exceção, use `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
