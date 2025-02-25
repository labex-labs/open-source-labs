# Grundlegendes Indexieren

NumPy-Arrays können mit der standardmäßigen Python-Syntax `x[obj]` indiziert werden, wobei `x` das Array und `obj` die Auswahl ist. Es gibt verschiedene Arten des Indexierens, je nachdem, welchen Typ `obj` hat.

## Einzelnes Element-Indexieren

Das Einzelnelement-Indexieren funktioniert genauso wie das Indexieren für andere standardmäßige Python-Sequenzen. Es basiert auf 0 und akzeptiert negative Indizes für das Indexieren von Ende des Arrays aus.

```python
x = np.arange(10)
print(x[2])  # Ausgabe: 2
print(x[-2])  # Ausgabe: 8
```

## Mehrdimensionales Indexieren

Arrays können mehrere Dimensionen haben, und das Indexieren funktioniert für jede Dimension auf die gleiche Weise. Sie können Elemente in einem mehrdimensionalen Array erreichen, indem Sie die Indizes jeder Dimension durch ein Komma trennen.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Ausgabe: 8
print(x[1, -1])  # Ausgabe: 9
```

## Indexieren von Unterdimensionen-Arrays

Wenn Sie ein mehrdimensionales Array mit weniger Indizes als Dimensionen indizieren, erhalten Sie ein Unterdimensionen-Array. Jeder angegebene Index wählt das Array aus, das den restlichen Dimensionen entspricht, die ausgewählt wurden.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Ausgabe: [0, 1, 2, 3, 4]
```
