# Converter a imagem num grafo com o valor do gradiente nas arestas

Converteremos a imagem num grafo, com o valor do gradiente nas arestas. Quanto menor for o beta, mais independente será a segmentação da imagem real. Para beta=1, a segmentação aproxima-se de uma Voronoi.

```python
# Converter a imagem num grafo com o valor do gradiente nas
# arestas.
graph = image.img_to_graph(rescaled_coins)

# Aplicar uma função decrescente do gradiente: uma exponencial
beta = 10
eps = 1e-6
graph.data = np.exp(-beta * graph.data / graph.data.std()) + eps
```
