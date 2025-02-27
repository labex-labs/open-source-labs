# Tracer les résultats

Nous allons tracer la projection résultante donnée par chaque méthode.

```python
for name in timing:
    title = f"{name} (time {timing[name]:.3f}s)"
    plot_embedding(projections[name], title)

plt.show()
```
