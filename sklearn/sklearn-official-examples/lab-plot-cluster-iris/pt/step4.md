# Aplicar K-Means Clustering

Agora, aplicaremos o algoritmo K-Means Clustering aos nossos dados. Inicializaremos o algoritmo com 3 clusters e o ajustaremos aos nossos dados.

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
