# Produzent-Verbraucher-Probleme

Generatoren stehen in enger Beziehung zu verschiedenen Formen von _Produzent-Verbraucher_-Problemen.

```python
# Produzent
def follow(f):
 ...
    while True:
     ...
        yield line        # Erzeugt den Wert in `line` unten
     ...

# Verbraucher
for line in follow(f):    # Verbraucht den Wert von `yield` oben
 ...
```

`yield` erzeugt Werte, die `for` verbraucht.
