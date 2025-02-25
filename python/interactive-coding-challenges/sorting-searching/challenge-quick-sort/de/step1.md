# Quick Sort

## Problem

Implementieren Sie den Quick Sort-Algorithmus in Python. Der Algorithmus sollte eine unsortierte Liste als Eingabe entgegennehmen und eine sortierte Liste zurückgeben. Der Algorithmus sollte für Listen beliebiger Größe funktionieren, einschließlich leerer Listen und Listen mit doppelten Elementen. Der Algorithmus sollte auch ungültige Eingaben优雅地处理.

Der Quick Sort-Algorithmus funktioniert wie folgt:

1. Wählen Sie ein Pivot-Element aus der Liste.
2. Teilen Sie die Liste in zwei Teilfolgen auf: eine mit Elementen, die kleiner als das Pivot sind, und eine mit Elementen, die größer als das Pivot sind.
3. Wenden Sie den Quick Sort-Algorithmus rekursiv auf die Teilfolgen an.
4. Verketten Sie die sortierten Teilfolgen mit dem Pivot-Element in der Mitte.

## Anforderungen

Um den Quick Sort-Algorithmus in Python zu implementieren, sollten die folgenden Anforderungen erfüllt werden:

- Der Algorithmus sollte keine in-place-Lösung sein.
- Der Algorithmus sollte doppelten Elementen in der Liste gerecht werden.
- Der Algorithmus sollte ungültige Eingaben, wie None oder nicht-listenähnliche Eingaben, behandeln.
- Der Algorithmus sollte Listen beliebiger Größe, einschließlich leerer Listen, verarbeiten können.

## Beispielverwendung

Die folgenden sind einige Beispiele dafür, wie der Quick Sort-Algorithmus in Python verwendet werden kann:

- None -> Exception

```python
quick_sort(None)
```

- Leere Eingabe -> []

```python
quick_sort([])
```

- Ein Element -> [Element]

```python
quick_sort([5])
```

- Zwei oder mehr Elemente

```python
quick_sort([5, 2, 8, 3, 1, 9])
```
