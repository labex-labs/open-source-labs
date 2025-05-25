# Compondo uma Legenda Personalizada com Diferentes Objetos Matplotlib

Nesta etapa, criaremos uma legenda personalizada usando diferentes objetos Matplotlib, incluindo `Line2D` e `Patch`. Primeiro, importamos a classe `Patch` do módulo `matplotlib.patches`. Em seguida, criamos uma lista de objetos `Line2D` e `Patch` com atributos personalizados. Finalmente, chamamos `legend()` com os objetos personalizados e os rótulos correspondentes.

```python
# Import Line2D and Patch classes
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Create legend elements
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# Plot data and generate custom legend
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
