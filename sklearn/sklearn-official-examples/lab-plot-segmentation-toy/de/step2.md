# Das Bild in einen Graphen umwandeln

Wir werden `img_to_graph` aus `sklearn.feature_extraction.image` verwenden, um das Bild in einen Graphen umzuwandeln. Der Wert des Gradienten an den Kanten wird ebenfalls berechnet.

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
