# Sentencia `finally`

Especifica código que debe ejecutarse independientemente de si se produce una excepción o no.

```python
lock = Lock()
...
lock.acquire()
try:
  ...
finally:
    lock.release()  # esto SIEMPRE se ejecutará. Con o sin excepción.
```

Comúnmente se utiliza para administrar de manera segura los recursos (especialmente los candados, archivos, etc.).
