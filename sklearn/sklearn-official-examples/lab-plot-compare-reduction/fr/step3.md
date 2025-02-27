# Créez un objet GridSearchCV et ajustez les données

Nous allons créer un objet `GridSearchCV` en utilisant le pipeline et la grille de paramètres que nous avons définis dans l'étape précédente. Nous allons ensuite ajuster les données à l'objet.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```
