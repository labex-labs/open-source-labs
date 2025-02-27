# Régression par processus gaussien

Dans cette étape, nous allons créer un régresseur par processus gaussien en utilisant un noyau additif en ajoutant les noyaux RBF et WhiteKernel. Le noyau WhiteKernel est un noyau qui sera capable d'estimer la quantité de bruit présent dans les données tandis que le RBF servira à ajuster la non-linéarité entre les données et la cible.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

kernel = 1.0 * RBF(length_scale=1e-1, length_scale_bounds=(1e-2, 1e3)) + WhiteKernel(
    noise_level=1e-2, noise_level_bounds=(1e-10, 1e1)
)
gpr = GaussianProcessRegressor(kernel=kernel, alpha=0.0)
gpr.fit(X_train, y_train)
y_mean, y_std = gpr.predict(X, return_std=True)
```
