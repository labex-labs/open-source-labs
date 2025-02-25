# Diagramm zeichnen

Wir werden nun das Diagramm mit `np.linspace` und `np.sin` zeichnen.

```python
x = np.linspace(-0.5, 1., 100)
ax.plot(x, np.sin(x*np.pi))
```
