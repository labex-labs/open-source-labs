# Adicionar linhas de grade e rótulos

Adicionaremos linhas de grade horizontais, definiremos rótulos para o eixo x (x-labels) e para o eixo y (y-labels) nos gráficos.

```python
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], labels=['x1', 'x2', 'x3', 'x4'])
    ax.set_xlabel('Four separate samples')
    ax.set_ylabel('Observed values')
```
