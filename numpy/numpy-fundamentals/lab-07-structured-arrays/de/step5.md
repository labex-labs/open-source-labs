# Vergleichen von strukturierten Arrays

Wenn die Datentypen zweier strukturierten Arrays gleich sind, können wir sie mit dem Gleichheitsoperator (`==`) vergleichen. Dies gibt ein boolesches Array zurück, das angibt, welche Elemente für alle Felder die gleichen Werte haben.

```python
# Vergleichen von zwei strukturierten Arrays
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
