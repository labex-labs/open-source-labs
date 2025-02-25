# Définition d'un graphique d'exemple

Nous définissons une fonction qui crée un graphique linéaire simple avec des étiquettes pour l'axe x et l'axe y et un titre.

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
