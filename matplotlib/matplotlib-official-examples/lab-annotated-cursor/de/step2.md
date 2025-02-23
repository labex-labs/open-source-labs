# Erstellen eines Diagramms

Wir erstellen ein einfaches Diagramm einer Parabel, indem wir die `linspace`-Funktion von NumPy verwenden, um 1000 Werte zwischen -5 und 5 für x zu generieren, und berechnen dann y als das Quadrat von x.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
