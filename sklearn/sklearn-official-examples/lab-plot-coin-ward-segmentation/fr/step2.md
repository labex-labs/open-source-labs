# Définir la structure des données

Les pixels dans une image sont connectés à leurs voisins. Pour effectuer une agrégation hiérarchique sur une image, nous devons définir la structure des données. Nous pouvons utiliser la fonction `grid_to_graph` de scikit-learn pour créer une matrice de connectivité qui définit la structure des données.

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```
