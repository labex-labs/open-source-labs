# Personalizar subgráficos

Personalizamos los subgráficos estableciendo el color de fondo de los subgráficos inferiores en negro, configurando las marcas de la escala del eje x y agregando un título a cada subgráfico.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
