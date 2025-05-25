# Soluções Possíveis

Vamos discutir algumas soluções possíveis para as limitações do agrupamento k-means. No bloco de código a seguir, mostramos como encontrar o número correto de clusters para o primeiro conjunto de dados e como lidar com blobs de tamanhos irregulares aumentando o número de inicializações aleatórias.

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Número Ótimo de Clusters")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Blobs de Tamanhos Irregulares \ncom várias inicializações")
plt.show()
```
