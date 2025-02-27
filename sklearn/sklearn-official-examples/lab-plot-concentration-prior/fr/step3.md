# Définir les paramètres pour le jeu de données d'entraînement

Dans cette étape, nous définissons les paramètres pour le jeu de données d'entraînement, qui comprennent l'état aléatoire, le nombre de composants, le nombre de caractéristiques, les couleurs, les covariances, les échantillons et les moyennes.

```python
random_state, n_components, n_features = 2, 3, 2
colors = np.array(["#0072B2", "#F0E442", "#D55E00"])
covars = np.array(
    [[[0.7, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]]]
)
samples = np.array([200, 500, 200])
means = np.array([[0.0, -0.70], [0.0, 0.0], [0.0, 0.70]])
```
