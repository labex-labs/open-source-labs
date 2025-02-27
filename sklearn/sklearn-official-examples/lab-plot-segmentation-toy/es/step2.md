# Convertir la imagen en un gráfico

Usaremos `img_to_graph` de `sklearn.feature_extraction.image` para convertir la imagen en un gráfico. También se calculará el valor del gradiente en los bordes.

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
