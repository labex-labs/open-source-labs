# Définir le style des axes

Enfin, nous allons définir le style de l'axe des x en spécifiant les étiquettes et les limites des graduations. Nous définirons une fonction d'aide `set_axis_style` pour y parvenir.

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```
