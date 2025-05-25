# Visualizar Clusters

Após aplicar o algoritmo K-Means Clustering, vamos visualizar os clusters formados. Usaremos um gráfico de dispersão 3D para visualizar os pontos de dados e seus respectivos clusters.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Comprimento da sépala")
ax.set_ylabel("Largura da sépala")
ax.set_zlabel("Comprimento da pétala")
plt.show()
```
