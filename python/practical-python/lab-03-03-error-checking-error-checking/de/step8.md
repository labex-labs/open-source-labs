# Falsche Art, Fehler zu fangen

Hier ist die falsche Art, Ausnahmen zu verwenden.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

Dies fängt alle möglichen Fehler ab und kann es unmöglich machen, das Problem zu debuggen, wenn der Code aus einem Grund fehlschlägt, den Sie gar nicht erwartet haben (z.B. ein nicht installierter Python-Modul usw.).
