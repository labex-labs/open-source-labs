# Générer des données fictives

Nous allons maintenant générer un ensemble de données fictives à l'aide de la fonction make_regression de scikit-learn. Nous allons générer un ensemble de données avec 20 échantillons, une caractéristique et une graine aléatoire de 0. Nous ajouterons également du bruit à l'ensemble de données.

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
