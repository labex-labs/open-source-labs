# Definieren der Kurve

Als nächstes definieren wir die Kurve, um die wir die Fehlerbande zeichnen möchten. In diesem Beispiel verwenden wir eine parametrisierte Kurve. Eine parametrisierte Kurve x(t), y(t) kann direkt mit `~.Axes.plot` gezeichnet werden.

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
