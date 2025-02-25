# Häufigstes Element

## Problem

Schreibe eine Python-Funktion namens `most_frequent(lst)`, die eine Liste von ganzen Zahlen als Eingabe nimmt und das häufigste Element in der Liste zurückgibt. Wenn es mehrere Elemente gibt, die die gleiche Anzahl von Vorkommen haben und die höchste Häufigkeit aufweisen, gib dasjenige zurück, das zuerst in der Liste erscheint.

Um dieses Problem zu lösen, kannst du die folgenden Schritte ausführen:

1. Verwende `set()`, um die eindeutigen Werte in `lst` zu erhalten.
2. Verwende `max()`, um das Element zu finden, das am häufigsten vorkommt.

Deine Funktion sollte folgende Signatur haben:

```python
def most_frequent(lst: List[int]) -> int:
```

## Beispiel

```python
assert most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) == 2
assert most_frequent([1, 2, 3, 4, 5]) == 1
assert most_frequent([1, 1, 1, 1, 1]) == 1
```
