# Création d'un maillage pour le tracé

Maintenant, nous allons créer un maillage pour le tracé. Le maillage sera utilisé pour tracer les probabilités prédites pour chaque point du maillage. Nous allons également définir la taille d'étape pour le maillage.

```python
h = 0.02  # taille d'étape dans le maillage

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```
