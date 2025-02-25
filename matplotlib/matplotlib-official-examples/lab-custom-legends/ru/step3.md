# Составление пользовательской легенды с различными объектами Matplotlib

В этом шаге мы создадим пользовательскую легенду с использованием различных объектов Matplotlib, включая `Line2D` и `Patch`. Сначала мы импортируем класс `Patch` из модуля `matplotlib.patches`. Затем мы создаем список объектов `Line2D` и `Patch` с пользовательскими атрибутами. Наконец, мы вызываем `legend()` с пользовательскими объектами и соответствующими метками.

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
