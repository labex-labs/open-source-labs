# Tracer les résultats

Maintenant, nous réorganisons les données en fonction des étiquettes de ligne et de colonne attribuées par le modèle `SpectralBiclustering` dans l'ordre croissant et nous les traçons à nouveau. Les `row_labels_` vont de 0 à 3, tandis que les `column_labels_` vont de 0 à 2, représentant un total de 4 clusters par ligne et 3 clusters par colonne.

```python
# Reordonner d'abord les lignes puis les colonnes.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")
_ = plt.show()
```

En tant que dernière étape, nous voulons démontrer les relations entre les étiquettes de ligne et de colonne attribuées par le modèle. Par conséquent, nous créons une grille avec `numpy.outer`, qui prend les `row_labels_` et `column_labels_` triés et ajoute 1 à chacun pour s'assurer que les étiquettes commencent à 1 au lieu de 0 pour une meilleure visualisation.

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Checkerboard structure of rearranged data")
plt.show()
```
