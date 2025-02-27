# Visualiser les clusters

Après avoir appliqué l'algorithme de regroupement K-Means, visualisons les clusters qui ont été formés. Nous utiliserons un nuage de points en 3D pour visualiser les points de données et leurs clusters respectifs.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
