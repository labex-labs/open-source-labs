# Median

Schreiben Sie eine Python-Funktion namens `find_median`, die eine Liste von Zahlen als Argument nimmt und den Median der Liste zurückgibt. Ihre Funktion sollte die folgenden Schritte ausführen:

1. Sortieren Sie die Zahlen der Liste mit `list.sort()`.
2. Finden Sie den Median, der entweder das mittlere Element der Liste ist, wenn die Liste eine ungerade Länge hat, oder der Durchschnitt der beiden mittleren Elemente, wenn die Liste eine gerade Länge hat.
3. Geben Sie den Median zurück.

Ihre Funktion sollte keine eingebauten Python-Bibliotheken oder Funktionen verwenden, die das Problem direkt lösen.

```python
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```python
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
