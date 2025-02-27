# Загрузка данных

Первым шагом является загрузка датасета Olivetti faces, который содержит 400 серых изображений размером 64x64 пикселя каждый. Данные разделяются на обучающую и тестовую выборки. В обучающей выборке находятся лица 30 людей, а в тестовой - лица оставшихся людей. Для этого практического занятия мы проверим алгоритмы на подмножестве из пяти человек.

```python
# Load the faces datasets
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # Test on independent people

# Test on a subset of people
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Upper half of the faces
X_train = train[:, : (n_pixels + 1) // 2]
# Lower half of the faces
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```
