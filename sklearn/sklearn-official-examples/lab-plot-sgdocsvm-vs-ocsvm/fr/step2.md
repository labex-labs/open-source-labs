# Générer des données

Nous allons générer un jeu de données simple pour ce laboratoire. Nous allons générer 500 échantillons d'entraînement et 20 échantillons de test. Nous allons également générer 20 échantillons anormaux.

```python
random_state = 42
rng = np.random.RandomState(random_state)

# Générer les données d'entraînement
X = 0.3 * rng.randn(500, 2)
X_train = np.r_[X + 2, X - 2]
# Générer quelques observations nouvelles régulières
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# Générer quelques observations nouvelles anormales
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
```
