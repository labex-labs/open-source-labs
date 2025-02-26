# Manera incorrecta de capturar errores

A continuación se muestra la manera incorrecta de utilizar excepciones.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

Esto captura todos los posibles errores y puede hacer imposible el depuración cuando el código falla por alguna razón que no esperabas en absoluto (por ejemplo, un módulo de Python desinstalado, etc.).
