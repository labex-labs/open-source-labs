# Générer des données

Ensuite, nous allons générer un ensemble de données à mélange gaussien avec deux composantes. Nous allons créer un ensemble de données gaussien décalé centré sur (20, 20) et un ensemble de données gaussien étiré centré sur zéro. Nous allons ensuite concaténer les deux ensembles de données pour former l'ensemble d'entraînement final.

```python
n_samples = 300

# générer un échantillonnage aléatoire, deux composantes
np.random.seed(0)

# générer des données sphériques centrées sur (20, 20)
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# générer des données gaussiennes étirées centrées sur zéro
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# concaténer les deux ensembles de données pour former l'ensemble d'entraînement final
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```
