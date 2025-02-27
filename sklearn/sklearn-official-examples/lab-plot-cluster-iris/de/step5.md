# Cluster visualisieren

Nachdem wir den K-Means-Clustering-Algorithmus angewendet haben, lassen Sie uns die gebildeten Cluster visualisieren. Wir werden einen 3D-Streuplot verwenden, um die Datenpunkte und ihre jeweiligen Cluster zu visualisieren.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
