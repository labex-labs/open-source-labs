# Exemples de GPC

Prédictions probabilistes avec la GPC : Cet exemple illustre la probabilité prédite de la GPC avec différents choix d'hyperparamètres.

```python
# Créez un modèle GPC avec un noyau RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Ajustez le modèle aux données d'entraînement
model.fit(X_train, y_train)

# Prédisez les probabilités de classe des données de test
y_prob = model.predict_proba(X_test)
```

Illustration de la GPC sur l'ensemble de données XOR : Cet exemple démontre l'utilisation de la GPC sur l'ensemble de données XOR. Nous comparons les résultats de l'utilisation d'un noyau stationnaire, isotrope (RBF) et d'un noyau non stationnaire (DotProduct).

```python
# Créez des modèles GPC avec différents noyaux
isotropic_kernel = RBF(length_scale=1.0)
non_stationary_kernel = DotProduct(sigma_0=1.0)

# Ajustez les modèles à l'ensemble de données XOR
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
non_stationary_model = GaussianProcessClassifier(kernel=non_stationary_kernel)
isotropic_model.fit(X_xor, y_xor)
non_stationary_model.fit(X_xor, y_xor)

# Faites des prédictions à l'aide des modèles entraînés
isotropic_y_pred = isotropic_model.predict(X_test)
non_stationary_y_pred = non_stationary_model.predict(X_test)
```

GPC sur l'ensemble de données iris : Cet exemple illustre la GPC sur l'ensemble de données iris en utilisant un noyau RBF isotrope et un noyau RBF anisotrope. Il montre comment différents choix d'hyperparamètres peuvent affecter la probabilité prédite.

```python
# Créez des modèles GPC avec différents noyaux et ajustez-les à l'ensemble de données iris
isotropic_kernel = RBF(length_scale=1.0)
anisotropic_kernel = RBF(length_scale=[1.0, 2.0])
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
anisotropic_model = GaussianProcessClassifier(kernel=anisotropic_kernel)
isotropic_model.fit(X_train, y_train)
anisotropic_model.fit(X_train, y_train)

# Prédisez les probabilités de classe
isotropic_y_prob = isotropic_model.predict_proba(X_test)
anisotropic_y_prob = anisotropic_model.predict_proba(X_test)
```
