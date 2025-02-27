# Définition de la matrice de connectivité

Dans cette étape, nous allons définir la matrice de connectivité en utilisant la fonction `grid_to_graph` de scikit-learn. Cette fonction crée un graphe de connectivité sur la base de la grille de pixels des images.

```python
connectivity = grid_to_graph(*images[0].shape)
```
