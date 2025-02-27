# Diviser le jeu de données

Nous allons diviser le jeu de données en sous-ensembles d'entraînement et de test de 50% chacun en utilisant la méthode `train_test_split()` de `sklearn.model_selection`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```
