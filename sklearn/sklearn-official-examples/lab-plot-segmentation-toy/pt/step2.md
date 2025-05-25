# Converter a imagem em um grafo

Usaremos `img_to_graph` de `sklearn.feature_extraction.image` para converter a imagem em um grafo. O valor do gradiente nas arestas também será calculado.

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
