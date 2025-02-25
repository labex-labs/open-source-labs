# Application de TickedStroke aux lignes

Dans cette étape, nous allons appliquer TickedStroke aux lignes.

```python
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Ligne",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
ax.plot(x, y, label="Courbe", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```

Ce code créera une ligne et une courbe avec l'effet de tracé rayé TickedStroke.
