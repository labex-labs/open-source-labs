# Générer des données

Nous allons générer un ensemble de données synthétiques avec seulement 3 caractéristiques informatives. Nous n'allons pas mélanger explicitement l'ensemble de données pour vous assurer que les caractéristiques informatives correspondront aux trois premières colonnes de X. De plus, nous allons diviser notre ensemble de données en sous-ensembles d'entraînement et de test.

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
