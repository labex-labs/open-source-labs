# Définissez une méthode pour ajuster les emplacements des épines

Dans cette étape, nous allons définir une méthode qui ajuste l'emplacement des épines des axes en fonction des emplacements d'épines spécifiés.

```python
def adjust_spines(ax, spines):
    """
    Ajuste l'emplacement des épines des axes en fonction des emplacements d'épines spécifiés.

    Paramètres :
        ax (Axes) : L'objet Axes de Matplotlib pour lequel ajuster les épines.
        spines (liste de str) : Les emplacements d'épines souhaités. Les options valides sont 'left' (gauche), 'right' (droite), 'top' (haut), 'bottom' (bas).

    Retourne :
        None
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # déplacer l'épine vers l'extérieur de 10 points
        else:
            spine.set_color('none')  # ne pas tracer l'épine

    # désactiver les graduations là où il n'y a pas d'épine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        ax.xaxis.set_ticks([])
```
