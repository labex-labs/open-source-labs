# Hinzufügen einer Linie, um die maskierten Bereiche zu markieren

Schließlich fügen wir eine Linie hinzu, um die maskierten Bereiche zu markieren. Wir erstellen ein Array von theta-Werten und zeichnen einen Kreis mit dem Radius `r0` mithilfe von `np.cos(theta)` und `np.sin(theta)`.

```python
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
```
