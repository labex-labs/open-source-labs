# Convertir l'image en un graphe avec la valeur du gradient sur les arêtes

Nous allons convertir l'image en un graphe avec la valeur du gradient sur les arêtes. Plus beta est petit, plus la segmentation est indépendante de l'image réelle. Pour beta = 1, la segmentation est proche d'un diagramme de Voronoi.

```python
# Convertir l'image en un graphe avec la valeur du gradient sur les
# arêtes.
graph = image.img_to_graph(rescaled_coins)

# Prendre une fonction décroissante du gradient : une exponentielle
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```
