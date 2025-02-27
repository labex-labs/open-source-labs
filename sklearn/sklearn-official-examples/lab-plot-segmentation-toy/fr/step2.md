# Convertir l'image en graphe

Nous allons utiliser `img_to_graph` de `sklearn.feature_extraction.image` pour convertir l'image en graphe. La valeur du gradient sur les arêtes sera également calculée.

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
