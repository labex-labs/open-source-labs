# Sentencia `with`

En el código moderno, `try-finally` a menudo se reemplaza con la sentencia `with`.

```python
lock = Lock()
with lock:
    # lock adquirido
  ...
# lock liberado
```

Un ejemplo más familiar:

```python
with open(filename) as f:
    # Utilizar el archivo
  ...
# Archivo cerrado
```

`with` define un _contexto_ de uso para un recurso. Cuando la ejecución sale de ese contexto, los recursos se liberan. `with` solo funciona con ciertos objetos que han sido programados específicamente para soportarlo.
