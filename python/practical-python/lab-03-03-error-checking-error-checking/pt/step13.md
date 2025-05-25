# Declaração `with`

Em código moderno, `try-finally` é frequentemente substituído pela declaração `with`.

```python
lock = Lock()
with lock:
    # lock acquired
    ...
# lock released
```

Um exemplo mais familiar:

```python
with open(filename) as f:
    # Use the file
    ...
# File closed
```

`with` define um _contexto_ de uso para um recurso. Quando a execução sai desse contexto, os recursos são liberados. `with` só funciona com certos objetos que foram especificamente programados para suportá-lo.
