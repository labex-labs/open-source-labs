# Arithmetische Progression

Schreiben Sie eine Funktion `arithmetic_progression(n, lim)`, die zwei positive ganze Zahlen `n` und `lim` entgegennimmt und eine Liste von Zahlen in der arithmetischen Progression zurückgibt, beginnend mit `n` und bis zu `lim`. Die Funktion sollte `range()` und `list()` mit den entsprechenden Start-, Schritt- und Endwerten verwenden, um die Liste zu generieren.

### Eingabe

- Zwei positive ganze Zahlen `n` und `lim`, wobei `n` die Startzahl und `lim` die Obergrenze ist.

### Ausgabe

- Eine Liste von Zahlen in der arithmetischen Progression, beginnend mit `n` und bis zu `lim`.

```python
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
```

```python
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```
