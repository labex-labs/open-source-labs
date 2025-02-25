# Potenzmenge

Schreiben Sie eine Python-Funktion namens `powerset(iterable)`, die ein Iterierbares als Argument nimmt und die Potenzmenge des Iterierbaren zurückgibt. Die Funktion sollte die folgenden Schritte ausführen:

1. Konvertieren Sie den gegebenen Wert in eine Liste.
2. Verwenden Sie `range()` und `itertools.combinations()`, um einen Generator zu erstellen, der alle Teilmengen zurückgibt.
3. Verwenden Sie `itertools.chain.from_iterable()` und `list()`, um den Generator zu verbrauchen und eine Liste zurückzugeben.

```python
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
