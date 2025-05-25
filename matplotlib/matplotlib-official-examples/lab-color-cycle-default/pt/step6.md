# Personalizar subplots

Personalizamos os subplots definindo a cor de fundo dos subplots inferiores para preto, definindo os ticks do eixo x e adicionando um título a cada subplot.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
