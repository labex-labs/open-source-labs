# Verwenden von fehlenden und auszufüllenden Werten

Die Argumente `missing_values` und `filling_values` werden verwendet, um fehlende Daten zu behandeln. Das Argument `missing_values` wird verwendet, um fehlende Daten zu erkennen, und das Argument `filling_values` wird verwendet, um einen Wert für fehlende Einträge bereitzustellen.

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
