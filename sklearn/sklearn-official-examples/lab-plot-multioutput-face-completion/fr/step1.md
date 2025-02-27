# Charger les données

La première étape consiste à charger l'ensemble de données des visages Olivetti, qui contient 400 images en niveaux de gris de 64x64 pixels chacune. Les données sont divisées en ensembles d'entraînement et de test. L'ensemble d'entraînement contient les visages de 30 personnes, et l'ensemble de test contient les visages des personnes restantes. Pour ce laboratoire, nous testerons les algorithmes sur un sous-ensemble de cinq personnes.

```python
# Charger les ensembles de données de visages
data, targets = fetch_olivetti_faces(return_X_y=True)

train = data[targets < 30]
test = data[targets >= 30]  # Tester sur des personnes indépendantes

# Tester sur un sous-ensemble de personnes
n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

n_pixels = data.shape[1]
# Première moitié des visages
X_train = train[:, : (n_pixels + 1) // 2]
# Seconde moitié des visages
y_train = train[:, n_pixels // 2 :]
X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]
```
