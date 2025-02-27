# Visualizar los clusters

Después de aplicar el algoritmo de agrupamiento K-Means, visualicemos los clusters que se formaron. Utilizaremos un diagrama de dispersión 3D para visualizar los puntos de datos y sus respectivos clusters.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
