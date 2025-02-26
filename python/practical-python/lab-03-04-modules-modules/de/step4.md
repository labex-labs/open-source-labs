# Module als Umgebungen

Module bilden eine umschließende Umgebung für den gesamten darin definierten Code.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

_Globale_ Variablen sind immer an das umschließende Modul (selbe Datei) gebunden. Jede Quelldatei ist ein eigenes kleines Universum.
