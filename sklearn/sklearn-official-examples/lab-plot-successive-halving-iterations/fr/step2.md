# Chargement du jeu de données

La fonction `make_classification` du module `sklearn.datasets` est utilisée pour générer un jeu de données de classification. Le jeu de données contient 400 échantillons avec 12 caractéristiques. Le code pour charger le jeu de données est le suivant :

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
