# Definieren von Subplots mit subplot2grid

Um Subplots mit `subplot2grid` zu definieren, müssen wir zunächst die Größe des Gitters mithilfe eines Tuples mit der gewünschten Anzahl von Zeilen und Spalten angeben. Wir müssen auch die Position des Subplots innerhalb des Gitters mithilfe eines anderen Tuples angeben.

Zum Beispiel um ein 3x3-Gitter mit einem Subplot zu erstellen, das die gesamte erste Zeile und alle drei Spalten umfasst, verwenden wir folgenden Code:

```python
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
```

Um ein Subplot zu erstellen, das die zweite Zeile und die ersten beiden Spalten umfasst, verwenden wir:

```python
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
```

Um ein Subplot zu erstellen, das die letzten beiden Zeilen und die letzte Spalte umfasst, verwenden wir:

```python
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
```

Um ein Subplot in der letzten Zeile und der ersten Spalte zu erstellen, verwenden wir:

```python
ax4 = plt.subplot2grid((3, 3), (2, 0))
```

Um ein Subplot in der letzten Zeile und der zweiten Spalte zu erstellen, verwenden wir:

```python
ax5 = plt.subplot2grid((3, 3), (2, 1))
```
