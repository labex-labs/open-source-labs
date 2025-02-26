# Problemas de Productor-Consumidor

Los generadores están estrechamente relacionados con diversas formas de problemas de _productor-consumidor_.

```python
# Productor
def follow(f):
 ...
    while True:
     ...
        yield line        # Produce el valor en `line` a continuación
     ...

# Consumidor
for line in follow(f):    # Consume el valor del `yield` anterior
 ...
```

`yield` produce valores que `for` consume.
