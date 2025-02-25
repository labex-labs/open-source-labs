# Agregar subgráficos al GridSpec

Podemos agregar subgráficos al GridSpec utilizando la función `fig.add_subplot()`. Podemos especificar la ubicación del subgráfico en la cuadrícula utilizando la notación de índice del objeto GridSpec. Por ejemplo, `gs[0, :]` especifica la primera fila y todas las columnas.

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
