# Vorkommen zählen

Schreiben Sie eine Funktion `count_occurrences(lst, val)`, die eine Liste `lst` und einen Wert `val` als Argumente übernimmt und die Anzahl der Vorkommen von `val` in `lst` zurückgibt. Ihre Funktion sollte die integrierte `list.count()`-Methode verwenden, um die Anzahl der Vorkommen zu zählen.

```python
def count_occurrences(lst, val):
  return lst.count(val)
```

```python
count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3
```
