# Capturando múltiples errores

Puedes capturar diferentes tipos de excepciones utilizando múltiples bloques `except`.

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

Alternativamente, si las instrucciones para manejarlas son las mismas, puedes agruparlas:

```python
try:
...
except (IOError,LookupError,RuntimeError) as e:
...
```
