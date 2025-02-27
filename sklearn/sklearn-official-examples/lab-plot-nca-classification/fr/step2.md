# Charger et préparer les données

Ensuite, nous allons charger et préparer les données. Nous chargerons le jeu de données Iris à l'aide de scikit-learn et ne sélectionnerons que deux caractéristiques. Nous diviserons ensuite les données en un ensemble d'entraînement et un ensemble de test.

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# we only take two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
