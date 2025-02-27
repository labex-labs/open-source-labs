# Visualizar datos

Antes de aplicar el algoritmo de agrupamiento K-Means, primero visualicemos los datos para entenderlos mejor. Utilizaremos un diagrama de dispersión 3D para visualizar los datos.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
