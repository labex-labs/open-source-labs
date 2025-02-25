# Slicing und Schrittweite

Das grundlegende Slicing in NumPy erweitert das Slicing-Konzept von Python auf N Dimensionen. Es ermöglicht es Ihnen, einen Bereich von Elementen entlang jeder Dimension eines Arrays auszuwählen.

## Grundlegendes Slicing

Das grundlegende Slicing tritt auf, wenn `obj` ein Slice-Objekt ist (konstruiert durch die `start:stop:step`-Notation innerhalb von eckigen Klammern), eine Ganzzahl oder ein Tupel aus Slice-Objekten und Ganzzahlen.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])  # Ausgabe: [1, 3, 5]
```

## Negative Indizes

Negative Indizes können verwendet werden, um von Ende des Arrays aus zu indexieren. Beispielsweise bezieht sich `-1` auf das letzte Element, `-2` auf das vorletzte Element usw.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[-2:10])  # Ausgabe: [8, 9]
print(x[-3:3:-1])  # Ausgabe: [7, 6, 5, 4]
```

## Standardwerte für Slicing

Wenn der Startindex nicht angegeben ist, wird er standardmäßig auf 0 für positive Schrittwerte und auf `-n-1` für negative Schrittwerte gesetzt. Wenn der Stopindex nicht angegeben ist, wird er standardmäßig auf `n` für positive Schrittwerte und auf `-n-1` für negative Schrittwerte gesetzt. Wenn der Schritt nicht angegeben ist, wird er standardmäßig auf 1 gesetzt.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[5:])  # Ausgabe: [5, 6, 7, 8, 9]
```
