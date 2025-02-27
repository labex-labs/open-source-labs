# Créer un graphe

Crée un graphe capturant la connectivité locale. Un nombre plus élevé de voisins donnera des grappes plus homogènes au détriment du temps de calcul. Un nombre très élevé de voisins donne des tailles de grappe plus uniformément réparties mais peut ne pas imposer la structure manifold locale des données.

```python
knn_graph = kneighbors_graph(X, 30, include_self=False)
```
