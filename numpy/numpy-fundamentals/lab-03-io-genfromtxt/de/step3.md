# Zerteilen der Zeilen in Spalten

Das Argument `delimiter` wird verwendet, um zu definieren, wie die Zeilen in Spalten aufgeteilt werden sollen. Standardmäßig nimmt `numpy.genfromtxt` an, dass `delimiter=None` ist, was bedeutet, dass die Zeile entlang von Leerzeichen (einschließlich Tabulatoren) aufgeteilt wird.

```python
np.genfromtxt(StringIO(data), delimiter=",")
```
