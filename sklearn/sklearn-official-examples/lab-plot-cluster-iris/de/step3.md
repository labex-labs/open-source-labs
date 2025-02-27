# Daten visualisieren

Bevor wir den K-Means-Clustering-Algorithmus anwenden, lassen Sie uns zunächst die Daten visualisieren, um eine bessere Vorstellung davon zu bekommen. Wir werden einen 3D-Streuplot verwenden, um die Daten zu visualisieren.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
