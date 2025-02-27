# Exemples de GPR

GPR avec estimation du niveau de bruit : Cet exemple illustre la GPR avec un noyau somme incluant un WhiteKernel pour estimer le niveau de bruit des données.

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# Créez un modèle GPR avec un noyau RBF et un WhiteKernel
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# Ajustez le modèle aux données d'entraînement
model.fit(X_train, y_train)

# Faites des prédictions à l'aide du modèle entraîné
y_pred = model.predict(X_test)
```

Comparaison de la GPR et de la régression ridge noyau : La régression ridge noyau (KRR) et la GPR apprennent une fonction cible en utilisant le "truc du noyau". La GPR apprend un modèle probabiliste génératif et peut fournir des intervalles de confiance, tandis que la KRR ne fournit que des prédictions.

```python
from sklearn.kernel_ridge import KernelRidge

# Créez un modèle de régression ridge noyau
krr_model = KernelRidge(kernel='rbf')

# Ajustez le modèle KRR aux données d'entraînement
krr_model.fit(X_train, y_train)

# Faites des prédictions à l'aide du modèle KRR
krr_y_pred = krr_model.predict(X_test)

# Comparez les résultats avec la GPR
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

GPR sur les données de CO2 de Mauna Loa : Cet exemple démontre la conception complexe de noyau et l'optimisation d'hyperparamètres en utilisant la montée en gradient sur la log-vraisemblance marginale. Les données consistent en concentrations mensuelles moyennes de CO2 atmosphérique collectées à l'Observatoire de Mauna Loa à Hawaii. L'objectif est de modéliser la concentration de CO2 en fonction du temps.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# Créez un modèle GPR avec un noyau composé
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# Ajustez le modèle aux données
model.fit(X_train, y_train)

# Faites des prédictions à l'aide du modèle entraîné
y_pred = model.predict(X_test)
```
