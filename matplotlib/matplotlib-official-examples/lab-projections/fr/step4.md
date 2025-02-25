# Tracer les données

Tracez les données sur chacun des trois sous-graphiques à l'aide de `plot_wireframe`.

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
