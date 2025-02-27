# Créer des ensembles d'entraînement et de test

Nous divisons l'ensemble de données en un ensemble d'entraînement avec 1000 échantillons et un ensemble de test avec 100 échantillons. Nous ajoutons du bruit gaussien à l'ensemble de test et créons deux copies des données originales ; une avec du bruit et une sans bruit.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```
