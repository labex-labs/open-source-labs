# Daten für das Diagramm erstellen

Als nächstes erstellen wir einige Daten, die wir zum Erstellen des Diagramms verwenden werden. Wir verwenden die `numpy.arange()`-Funktion, um ein Array von Werten von 0 bis 14 zu erstellen und es in der Variable `x` zu speichern. Wir verwenden auch die `numpy.sin()`-Funktion, um ein Array von Werten zu erstellen, die die Sinuswerte von jedem Wert in `x` geteilt durch 2 sind, und speichern es in der Variable `y`.

```python
x = np.arange(14)
y = np.sin(x / 2)
```
