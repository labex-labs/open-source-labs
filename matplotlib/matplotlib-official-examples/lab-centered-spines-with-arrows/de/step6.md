# Hinzufügen von Daten zum Diagramm

Schließlich können Sie dem Diagramm einige Daten hinzufügen, um sie zu visualisieren. In diesem Fall können Sie die Funktion `plot()` verwenden, um eine Sinuswelle zu zeichnen.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
