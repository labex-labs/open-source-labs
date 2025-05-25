# Visualizar os Clusters

Vamos visualizar os clusters formados pelo algoritmo k-means.

```python
# Obter as etiquetas dos clusters para cada ponto de dados
labels = kmeans.labels_

# Plotar os pontos de dados com clusters codificados por cores
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()
```
