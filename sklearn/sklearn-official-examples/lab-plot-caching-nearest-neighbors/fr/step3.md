# Calculer le graphe des plus proches voisins

Dans cette étape, nous allons calculer le graphe des plus proches voisins à l'aide de KNeighborsTransformer.

```python
# Le transformateur calcule le graphe des plus proches voisins en utilisant
# le nombre maximum de voisins nécessaire dans la recherche en grille. Le modèle
# du classifieur filtre le graphe des plus proches voisins selon les
# exigences de son propre paramètre n_neighbors.
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```
