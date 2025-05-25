# Gráfico de Hachuras sem Cor com uma Legenda

Nesta etapa, criaremos um gráfico de hachuras sem cor e adicionaremos uma legenda. Usaremos a função `contour` para criar as linhas de contorno e a função `contourf` para especificar as hachuras sem cor.

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```
