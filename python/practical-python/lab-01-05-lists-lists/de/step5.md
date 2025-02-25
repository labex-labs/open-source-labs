# Sortieren von Listen

Listen können "in-place" sortiert werden.

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Umgekehrte Reihenfolge
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# Es funktioniert mit beliebig geordneten Daten
s = ['foo', 'bar','spam']
s.sort()                    # ['bar', 'foo','spam']
```

Verwenden Sie `sorted()`, wenn Sie stattdessen eine neue Liste erstellen möchten:

```python
t = sorted(s)               # s bleibt unverändert, t enthält die sortierten Werte
```
