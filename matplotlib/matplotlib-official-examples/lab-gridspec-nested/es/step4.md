# Agregar subgráficos al gridspec interno

Ahora agregaremos subgráficos al gridspec interno. Crearemos tres subgráficos: `ax1`, `ax2` y `ax3`.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
