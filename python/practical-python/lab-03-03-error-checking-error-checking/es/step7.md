# Capturando todos los errores

Para capturar cualquier excepción, use `Exception` de la siguiente manera:

```python
try:
 ...
except Exception:       # PELIGRO. Ver abajo
    print('An error occurred')
```

En general, escribir código así es una mala idea porque no tendrás idea de por qué falló.
