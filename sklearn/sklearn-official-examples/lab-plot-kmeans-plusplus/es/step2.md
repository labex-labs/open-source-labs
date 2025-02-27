# Calcular semillas a partir de K-Means++

Utilizaremos la función `kmeans_plusplus` de la biblioteca scikit-learn para calcular las semillas a partir de K-Means++. Esta función devuelve los centros iniciales de los clusters que se utilizan para el agrupamiento k-means. Calcularemos 4 clusters utilizando K-Means++.

```python
# Calculate seeds from k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
