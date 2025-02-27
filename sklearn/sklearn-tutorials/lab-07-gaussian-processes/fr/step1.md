# Régression par processus gaussien (GPR)

La classe GaussianProcessRegressor implémente des processus gaussiens pour les tâches de régression. Il est nécessaire de spécifier une loi a priori pour le processus gaussien, telle que les fonctions de moyenne et de covariance. Les hyperparamètres du noyau sont optimisés pendant le processus d'ajustement. Voyons un exemple d'utilisation de la GPR pour la régression.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Créez un modèle GPR avec un noyau RBF
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# Ajustez le modèle aux données d'entraînement
model.fit(X_train, y_train)

# Faites des prédictions à l'aide du modèle entraîné
y_pred = model.predict(X_test)
```
