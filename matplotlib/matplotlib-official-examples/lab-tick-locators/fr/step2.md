# Préparation du graphique

Ensuite, nous allons préparer le graphique en créant une figure et un tableau de sous-graphiques. Nous définirons également une fonction `setup` qui définit les paramètres communs pour les axes dans l'exemple.

```python
fig, axs = plt.subplots(8, 1, figsize=(8, 6))

def setup(ax, title):
    """Définir les paramètres communs pour les Axes dans l'exemple."""
    # ne montrer que la ligne inférieure de l'épine
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines[['left', 'right', 'top']].set_visible(False)

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.text(0.0, 0.2, title, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')
```
