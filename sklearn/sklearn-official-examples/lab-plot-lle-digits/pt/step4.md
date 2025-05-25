# Plotar Resultados

Vamos plotar a projeção resultante de cada método.

```python
for name in timing:
    title = f"{name} (tempo {timing[name]:.3f}s)"
    plot_embedding(projections[name], title)

plt.show()
```
