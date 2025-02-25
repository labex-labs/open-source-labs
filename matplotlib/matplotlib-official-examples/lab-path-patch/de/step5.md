# Kontrollpunkte und Verbindungslinien plotten

In diesem Schritt plotten wir die Kontrollpunkte und die Verbindungslinien des Pfads mit der `plot`-Methode des Achsenobjekts.

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
