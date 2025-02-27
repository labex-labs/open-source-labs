# Cargar los datos

El primer paso es cargar el conjunto de datos de rostros Olivetti, que contiene 400 imágenes en escala de grises de 64x64 píxeles cada una. Los datos se dividen en conjuntos de entrenamiento y prueba. El conjunto de entrenamiento contiene los rostros de 30 personas, y el conjunto de prueba contiene los rostros de las personas restantes. Para esta práctica, probaremos los algoritmos en un subconjunto de cinco personas.

```python
# Cargar los conjuntos de datos de rostros
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # Probar en personas independientes

# Probar en un subconjunto de personas
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Mitad superior de los rostros
X_train = train[:, : (n_pixels + 1) // 2]
# Mitad inferior de los rostros
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```
