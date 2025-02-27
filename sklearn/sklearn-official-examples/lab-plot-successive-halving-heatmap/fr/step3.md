# Effectuez la Décimation successive

Nous allons maintenant effectuer une recherche de paramètres en utilisant la Décimation successive sur le même modèle SVC et le même jeu de données utilisés dans l'Étape 2.

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
