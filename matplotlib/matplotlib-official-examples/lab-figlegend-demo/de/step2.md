# Erstellen eines einfachen Plots

Um einen einfachen Plot zu erstellen, müssen wir die x- und y-Werte definieren und sie dann mit `plt.plot()` plotten. Hier werden wir zwei Sinuswellen plotten.

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
