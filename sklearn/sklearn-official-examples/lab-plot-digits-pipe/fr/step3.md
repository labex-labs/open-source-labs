# Charger l'ensemble de données et définir les paramètres pour GridSearchCV

Nous allons charger l'ensemble de données des chiffres et définir les paramètres pour GridSearchCV. Nous allons définir le paramètre pour la troncature de la PCA et la régularisation du classifieur.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```
