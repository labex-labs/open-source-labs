# Adicionar Subplots ao Segundo `GridSpec` Interno

Agora adicionaremos subplots ao segundo `gridspec` interno. Criaremos três subplots: `ax4`, `ax5` e `ax6`.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
