# Modulladung und Systempfad

Versuchen Sie, das gerade erstellte Modul zu importieren:

```python
>>> import simplemod
simplemod geladen
>>> simplemod.foo()
x ist 42
>>>
```

Wenn dies mit einem `ImportError` fehlschlägt, ist Ihre Pfadkonfiguration fehlerhaft. Schauen Sie sich den Wert von `sys.path` an und beheben Sie den Fehler.

```python
>>> import sys
>>> sys.path
... schauen Sie sich das Ergebnis an...
>>>
```
