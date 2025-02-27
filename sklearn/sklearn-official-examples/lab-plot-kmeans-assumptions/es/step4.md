# Posibles soluciones

Discutiremos algunas posibles soluciones a las limitaciones del agrupamiento k - means. En el siguiente bloque de código, mostramos cómo encontrar el número correcto de clusters para el primer conjunto de datos y cómo lidiar con cúmulos de tamaños desiguales aumentando el número de inicializaciones aleatorias.

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Optimal Number of Clusters")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs \nwith several initializations")
plt.show()
```
