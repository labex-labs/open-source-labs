# Calcular sementes a partir do k-means++

Usaremos a função `kmeans_plusplus` da biblioteca scikit-learn para calcular as sementes a partir do k-means++. Esta função retorna os centros iniciais dos clusters que são usados para o agrupamento k-means. Calcularemos 4 clusters usando o k-means++.

```python
# Calcular sementes a partir do k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
