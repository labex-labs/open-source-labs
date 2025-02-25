# Zeichnen von etwas in den Teilplots

Wir werden etwas in den Teilplots zeichnen, damit der Benutzer die Wirkung des RectangleSelector und des EllipseSelector sehen kann.

```python
N = 100000  # Wenn N groß ist, kann man die Verbesserung durch das Verwenden von Blitting sehen.
x = np.linspace(0, 10, N)

for ax in axs:
    ax.plot(x, np.sin(2*np.pi*x))  # zeichnet etwas
```
