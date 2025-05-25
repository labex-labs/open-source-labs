# Compondo uma Legenda Personalizada

Nesta etapa, criaremos uma legenda personalizada usando objetos Matplotlib. Primeiro, importamos a classe `Line2D` do módulo `matplotlib.lines`. Em seguida, criamos uma lista de objetos `Line2D` com atributos de cor, largura e rótulo personalizados. Finalmente, plotamos os dados novamente usando a função `plot` e chamamos `legend()` com as linhas personalizadas e os rótulos correspondentes.

```python
# Import Line2D class
from matplotlib.lines import Line2D

# Create custom lines
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Plot data and generate custom legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
