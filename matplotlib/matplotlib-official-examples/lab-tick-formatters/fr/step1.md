# Importation de Matplotlib et configuration du tracé

Tout d'abord, nous devons importer la bibliothèque Matplotlib et configurer le tracé. Nous allons créer un tracé vide avec un axe y et un axe x. Nous allons également configurer l'axe pour ne montrer que la ligne inférieure, définir les positions des étiquettes et définir la longueur des étiquettes.

```python
import matplotlib.pyplot as plt
from matplotlib import ticker

def setup(ax, title):
    """Configure les paramètres communs pour les Axes dans l'exemple."""
    # ne montrer que la ligne inférieure
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    # définir les positions des étiquettes
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, ax = plt.subplots(figsize=(8, 2))
setup(ax, "Formatteurs d'étiquettes")
```
