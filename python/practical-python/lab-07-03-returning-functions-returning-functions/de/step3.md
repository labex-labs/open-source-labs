# Closures

Wenn eine innere Funktion als Ergebnis zurückgegeben wird, ist diese innere Funktion als _Closure_ bekannt.

```python
def add(x, y):
    # `do_add` ist ein Closure
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

_Wesentliches Merkmal: Ein Closure behält die Werte aller Variablen bei, die das spätere ordnungsgemäße Ausführen der Funktion erforderlich macht._ Denken Sie sich ein Closure als eine Funktion plus eine zusätzliche Umgebung, die die Werte der Variablen enthält, auf die es angewiesen ist.
