# Dessiner la bande d'erreur

Nous pouvons maintenant tracer la bande d'erreur en appelant la fonction `draw_error_band` et en passant les paramètres appropriés.

```python
fig, axs = plt.subplots(1, 2, layout='constrained', sharex=True, sharey=True)
errs = [
    (axs[0], "erreur constante", 0.05),
    (axs[1], "erreur variable", 0.05 * np.sin(2 * t) ** 2 + 0.04),
]
for i, (ax, title, err) in enumerate(errs):
    ax.set(title=title, aspect=1, xticks=[], yticks=[])
    ax.plot(x, y, "k")
    draw_error_band(ax, x, y, err=err,
                    facecolor=f"C{i}", edgecolor="none", alpha=.3)

plt.show()
```
