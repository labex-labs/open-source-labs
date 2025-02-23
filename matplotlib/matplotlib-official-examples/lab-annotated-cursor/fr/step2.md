# Créez un tracé

Nous créons un tracé simple d'une parabole en utilisant la fonction `linspace` de NumPy pour générer 1000 valeurs entre -5 et 5 pour x, puis en calculant y comme le carré de x.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
