# Symmetrische Differenz

## Problem

Schreiben Sie eine Funktion `symmetric_difference(a, b)`, die zwei Listen als Argumente nimmt und ihre symmetrische Differenz als Liste zurückgibt. Die Funktion sollte doppelte Werte nicht ausschließen.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie aus jeder Liste einen Satz.
2. Verwenden Sie eine List Comprehension für jede von ihnen, um nur die Werte zu behalten, die nicht in der zuvor erstellten Menge der anderen Liste enthalten sind.
3. Verketten Sie die beiden Listen, die in Schritt 2 erhalten wurden.

## Beispiel

```python
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
