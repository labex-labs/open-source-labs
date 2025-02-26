# Dinge definieren

Namen müssen immer definiert sein, bevor sie später verwendet werden.

```python
def square(x):
    return x*x

a = 42
b = a + 2     # Erfordert, dass `a` definiert ist

z = square(b) # Erfordert, dass `square` und `b` definiert sind
```

**Die Reihenfolge ist wichtig.** Sie setzen die Definitionen von Variablen und Funktionen fast immer ganz oben.
