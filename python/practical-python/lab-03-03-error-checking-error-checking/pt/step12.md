# Declaração `finally`

Especifica o código que deve ser executado, independentemente de uma exceção ocorrer ou não.

```python
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.
```

Comumente usado para gerenciar recursos com segurança (especialmente locks, arquivos, etc.).
