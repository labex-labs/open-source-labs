# Effectuez une Recherche en grille

Nous utiliserons la Recherche en grille pour effectuer une recherche de paramètres sur le modèle SVC. Nous utiliserons le jeu de données synthétique généré et la grille de paramètres générée dans l'Étape 1.

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
