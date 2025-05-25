# Adicionar Subplots ao `GridSpec` Interno

Agora adicionaremos subplots ao `gridspec` interno. Criaremos três subplots: `ax1`, `ax2` e `ax3`.

```python
ax1 = fig.add_subplot(gs00[:-1, :])
ax2 = fig.add_subplot(gs00[-1, :-1])
ax3 = fig.add_subplot(gs00[-1, -1])
```
