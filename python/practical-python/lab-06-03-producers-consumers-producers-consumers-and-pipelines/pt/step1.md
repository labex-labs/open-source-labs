# Problemas Produtor-Consumidor (Producer-Consumer Problems)

Geradores estão intimamente relacionados a várias formas de problemas _produtor-consumidor_ (producer-consumer).

```python
# Produtor (Producer)
def follow(f):
    ...
    while True:
        ...
        yield line        # Produz valor em `line` abaixo (Produces value in `line` below)
        ...

# Consumidor (Consumer)
for line in follow(f):    # Consome valor de `yield` acima (Consumes value from `yield` above)
    ...
```

`yield` produz valores que o `for` consome.
