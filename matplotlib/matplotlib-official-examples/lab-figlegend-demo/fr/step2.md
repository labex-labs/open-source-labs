# Création d'un tracé de base

Pour créer un tracé de base, nous devons définir les valeurs de x et y puis les tracer à l'aide de `plt.plot()`. Ici, nous allons tracer deux ondes sinusoïdales.

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
