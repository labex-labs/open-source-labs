# Adicionar subplots ao GridSpec

Podemos adicionar subplots ao GridSpec usando a função `fig.add_subplot()`. Podemos especificar a localização do subplot na grade usando a notação de indexação do objeto GridSpec. Por exemplo, `gs[0, :]` especifica a primeira linha e todas as colunas.

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
