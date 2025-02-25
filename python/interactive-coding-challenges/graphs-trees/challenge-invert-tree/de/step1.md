# Baum invertieren

## Problem

Gegeben einen binären Baum, schreiben Sie eine Funktion, um den Baum zu invertieren. Die Funktion sollte den Wurzelknoten des Baumes als Eingabe entgegennehmen und den neuen Wurzelknoten des invertierten Baumes zurückgeben.

## Anforderungen

Um dieses Problem zu lösen, müssen Sie die folgenden Anforderungen erfüllen:

- Sie sollten eine Node-Klasse haben, die einen Knoten im binären Baum repräsentiert.
- Sie sollten alle linken und rechten Knotenpaare im binären Baum austauschen.
- Sie sollten ungültige Eingaben优雅地 (gracefully) behandeln.
- Ihre Lösung sollte in den Speicher passen.

## Beispielverwendung

Angenommen, wir haben folgenden binären Baum:

```txt
     5
   /   \
  2     7
 / \   / \
1   3 6   9
```

Nachdem wir den Baum invertiert haben, sollten wir erhalten:

```txt
     5
   /   \
  7     2
 / \   / \
9   6 3   1
```
