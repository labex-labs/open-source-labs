# Generar conjunto de datos

Generaremos un conjunto de datos de 3 clases usando la función `make_blobs` de scikit-learn. Usaremos 1000 muestras y estableceremos los centros de los grupos en `[-5, 0], [0, 1.5], [5, -1]`. Luego transformaremos el conjunto de datos usando una matriz de transformación para que el conjunto de datos sea más difícil de clasificar.

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```
