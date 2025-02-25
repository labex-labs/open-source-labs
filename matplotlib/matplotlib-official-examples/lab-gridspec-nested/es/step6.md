# Agregar subgráficos al segundo gridspec interno

Ahora agregaremos subgráficos al segundo gridspec interno. Crearemos tres subgráficos: `ax4`, `ax5` y `ax6`.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
