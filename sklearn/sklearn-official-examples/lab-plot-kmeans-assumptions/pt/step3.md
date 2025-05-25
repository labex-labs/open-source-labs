# Agrupamento K-Means

Usaremos a classe `KMeans` do scikit-learn para agrupar os dados. No bloco de código a seguir, criamos um gráfico 2x2 mostrando os clusters obtidos pelo k-means para cada conjunto de dados.

```python
from sklearn.cluster import KMeans

common_params = {
    "n_init": "auto",
    "random_state": random_state,
}

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

y_pred = KMeans(n_clusters=2, **common_params).fit_predict(X)
axs[0, 0].scatter(X[:, 0], X[:, 1], c=y_pred)
axs[0, 0].set_title("Número de Clusters Não Ótimo")

y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X_aniso)
axs[0, 1].scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
axs[0, 1].set_title("Blobs Distribuídos Anisotropicamente")

y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X_varied)
axs[1, 0].scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
axs[1, 0].set_title("Variância Desigual")

y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X_filtered)
axs[1, 1].scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
axs[1, 1].set_title("Blobs com Tamanhos Desiguais")

plt.suptitle("Clusters KMeans Inesperados").set_y(0.95)
plt.show()
```
