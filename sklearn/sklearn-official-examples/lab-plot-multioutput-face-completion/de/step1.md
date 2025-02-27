# Daten laden

Der erste Schritt besteht darin, den Olivetti Faces-Datensatz zu laden, der 400 Graustufenbilder mit je 64x64 Pixeln enthält. Die Daten werden in Trainings- und Testsets unterteilt. Das Trainingsset enthält die Gesichter von 30 Personen, und das Testset enthält die Gesichter der verbleibenden Personen. Für dieses Lab werden wir die Algorithmen auf einem Teilsatz von fünf Personen testen.

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
