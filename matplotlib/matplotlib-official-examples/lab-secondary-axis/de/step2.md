# Zeichnen der Daten

Wir werden eine einfache Sinuswelle erstellen, um die Verwendung einer Sekundärachse zu demonstrieren. Wir werden die Sinuswelle mit Grad als x-Achse zeichnen.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```
