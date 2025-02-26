# Re-lanzando una excepción

Utiliza `raise` para propagar un error capturado.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

Esto te permite tomar medidas (por ejemplo, registrar) y pasar el error al llamador.
