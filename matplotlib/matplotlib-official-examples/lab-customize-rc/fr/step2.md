# Personnaliser les paramètres par défaut

Pour personnaliser les paramètres par défaut pour une figure spécifique, vous pouvez à nouveau utiliser la méthode `rcParams.update()`. Cette fois-ci, vous passerez un dictionnaire de noms et de valeurs de paramètres que vous voulez définir pour cette figure. Voici un exemple qui définit certains paramètres par défaut pour une figure spécifique :

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
