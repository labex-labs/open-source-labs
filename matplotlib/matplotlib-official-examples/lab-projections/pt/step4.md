# Plotar os Dados

Plote os dados em cada um dos três subplots usando `plot_wireframe`.

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
