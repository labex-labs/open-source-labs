# Criando Subplots

Agora, criaremos uma grade 2x2 de subplots usando a função `subplots`. Isso nos dará quatro gráficos para visualizar o padrão de esparsidade (sparsity pattern) do array.

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```
