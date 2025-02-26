# Lokale Variablen

Beobachten Sie, wie die innere Funktion auf Variablen verweist, die von der äußeren Funktion definiert wurden.

```python
def add(x, y):
    def do_add():
        # `x` und `y` sind oberhalb von `add(x, y)` definiert
        print('Adding', x, y)
        return x + y
    return do_add
```

Beobachten Sie weiter, dass diese Variablen irgendwie am Leben bleiben, nachdem `add()` abgeschlossen ist.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # Woher kommen diese Werte?
7
```
