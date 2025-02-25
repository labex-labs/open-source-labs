# Création d'un diagramme en boîte rectangulaire

Nous allons maintenant créer un diagramme en boîte rectangulaire à l'aide de la fonction `boxplot()` de Matplotlib. Nous allons définir le paramètre `patch_artist` sur `True` pour remplir la boîte de couleur.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # alignement vertical de la boîte
                     patch_artist=True,  # remplir avec de la couleur
                     labels=labels)  # étiquettes d'axe x
ax1.set_title('Diagramme en boîte rectangulaire')
```
