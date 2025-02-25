# Création d'un diagramme en boîte à encoche

Nous allons maintenant créer un diagramme en boîte à encoche avec la fonction `boxplot()`. Nous allons définir le paramètre `notch` sur `True` pour créer un diagramme en boîte à encoche.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # forme de l'encoche
                     vert=True,  # alignement vertical de la boîte
                     patch_artist=True,  # remplir avec de la couleur
                     labels=labels)  # étiquettes d'axe x
ax2.set_title('Diagramme en boîte à encoche')
```
