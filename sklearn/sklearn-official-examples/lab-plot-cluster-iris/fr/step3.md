# Visualisation des données

Avant d'appliquer l'algorithme de regroupement K-Means, visualisons d'abord les données pour mieux les comprendre. Nous utiliserons un nuage de points en 3D pour visualiser les données.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
