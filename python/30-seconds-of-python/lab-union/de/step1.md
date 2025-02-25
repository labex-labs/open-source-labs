# Listevereinigung

Schreiben Sie eine Python-Funktion namens `list_union(a, b)`, die zwei Listen als Eingabe nimmt und eine neue Liste zurückgibt, die alle einzigartigen Elemente aus beiden Listen enthält. Ihre Funktion sollte die folgenden Schritte ausführen:

1. Verbinden Sie die beiden Eingabelisten `a` und `b` zu einer einzelnen Liste.
2. Entfernen Sie alle Duplikate aus der kombinierten Liste.
3. Geben Sie die neue Liste mit allen einzigartigen Elementen zurück.

Ihre Funktion sollte die Eingabelisten `a` und `b` nicht modifizieren.

```python
def union(a, b):
  return list(set(a + b))
```

```python
union([1, 2, 3], [4, 3, 2]) # [1, 2, 3, 4]
```
