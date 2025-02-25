# Créez les sous-graphiques

Maintenant, nous allons créer les sous-graphiques en utilisant la fonction `subplots`. Nous allons créer une grille de sous-graphiques avec le même rapport d'aspect, et nous allons supprimer les graduations de l'axe x et de l'axe y. Nous ajouterons également une ligne verticale et une ligne horizontale au centre de chaque sous-graphique pour aider à visualiser l'alignement.

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```
