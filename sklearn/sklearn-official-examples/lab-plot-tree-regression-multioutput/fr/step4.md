# Prédire

Dans cette étape, nous allons effectuer des prédictions à l'aide des modèles que nous avons créés dans l'étape précédente. Nous utiliserons `np.arange` pour créer un nouveau tableau de valeurs allant de -100 à 100 avec un intervalle de 0,01, puis utiliser la méthode `predict` de nos modèles pour prédire la sortie.

```python
# Predict
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```
