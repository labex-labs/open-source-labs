# Ajustar el Modelo K-Means

Ajustaremos el modelo K-Means en una pequeña submuestra de los datos de la imagen y lo usaremos para predecir los índices de color en la imagen completa.

```python
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

n_colors = 64

# Ajustar el modelo K-Means en una pequeña submuestra de los datos
print("Ajustando el modelo en una pequeña submuestra de los datos")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"hecho en {time() - t0:0.3f}s.")

# Obtener etiquetas para todos los puntos
print("Predecir índices de color en la imagen completa (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"hecho en {time() - t0:0.3f}s.")
```
