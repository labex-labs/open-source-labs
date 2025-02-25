# Setzen der Grenzen und Anzeigen des Gitters

In diesem Schritt werden wir die Grenzen für die Achsen setzen und das Gitter anzeigen. Wir werden `set_aspect()` verwenden, um das Seitenverhältnis der Achsen festzulegen, und `grid()` verwenden, um das Gitter anzuzeigen.

```python
# Setzen der Grenzen und Anzeigen des Gitters
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
