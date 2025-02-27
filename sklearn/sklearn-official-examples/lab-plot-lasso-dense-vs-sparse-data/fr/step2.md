# Générer des données denses

Ensuite, nous générons quelques données denses que nous utiliserons pour la régression Lasso. Nous utilisons la fonction `make_regression` de Scikit-learn pour générer 200 échantillons avec 5000 caractéristiques.

```python
X, y = make_regression(n_samples=200, n_features=5000, random_state=0)
```
