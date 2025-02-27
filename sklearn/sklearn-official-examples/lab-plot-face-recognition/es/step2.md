# Cargar y explorar el conjunto de datos

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

Descargamos el conjunto de datos utilizando la función `fetch_lfw_people()` de scikit-learn. Luego exploramos el conjunto de datos obteniendo el número de muestras, la altura y el ancho de las imágenes. También obtenemos los datos de entrada `X`, la variable objetivo `y`, los nombres de las variables objetivo `target_names` y el número de clases `n_classes`.
