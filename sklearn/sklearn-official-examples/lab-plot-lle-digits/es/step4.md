# Graficar los resultados

Graficaremos la proyección resultante dada por cada método.

```python
for name in timing:
    title = f"{name} (tiempo {timing[name]:.3f}s)"
    plot_embedding(projections[name], title)

plt.show()
```
