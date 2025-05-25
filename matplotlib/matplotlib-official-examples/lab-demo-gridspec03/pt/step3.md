# Controlar o Espaçamento ao Redor e Entre os Subplots

Nesta etapa, usaremos `GridSpec` para controlar o espaçamento ao redor e entre os subplots. Criaremos uma figura com 2 gridspecs, cada um com 3 linhas e 3 colunas. Especificaremos os parâmetros `left`, `right`, `bottom`, `top`, `wspace` e `hspace` para controlar o espaçamento.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
