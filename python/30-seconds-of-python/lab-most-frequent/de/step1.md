# Häufigstes Element

Schreiben Sie eine Python-Funktion namens `most_frequent(lst)`, die eine Liste von ganzen Zahlen als Eingabe erhält und das häufigste Element in der Liste zurückgibt. Wenn es mehrere Elemente gibt, die die gleiche Anzahl von Vorkommen haben und die höchste Häufigkeit aufweisen, geben Sie das Element zurück, das zuerst in der Liste erscheint.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `set()`, um die eindeutigen Werte in `lst` zu erhalten.
2. Verwenden Sie `max()`, um das Element zu finden, das am häufigsten vorkommt.

Ihre Funktion sollte folgende Signatur haben:

```python
def most_frequent(lst: List[int]) -> int:
```

```python
def most_frequent(lst):
  return max(set(lst), key = lst.count)
```

```python
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
```
