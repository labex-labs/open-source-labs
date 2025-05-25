# Gerar Subplots com `GridSpec`

Nesta etapa, usaremos `GridSpec` para gerar subplots. Criaremos uma figura com 2 linhas e 2 colunas. Também especificaremos os `width_ratios` e `height_ratios` para controlar os tamanhos relativos dos subplots.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
