# Création de jeux de données

Nous allons créer trois jeux de données synthétiques en utilisant les fonctions make_classification, make_moons et make_circles de scikit-learn. Nous allons diviser chaque jeu de données en ensembles d'entraînement et de test en utilisant train_test_split.

```python
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=0, n_clusters_per_class=1
)
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
linearly_separable = (X, y)

datasets = [
    make_moons(noise=0.3, random_state=0),
    make_circles(noise=0.2, factor=0.5, random_state=1),
    linearly_separable,
]

figure = plt.figure(figsize=(17, 9))
i = 1
# itère sur les jeux de données
for X, y in datasets:
    # divise en parties d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )
```
