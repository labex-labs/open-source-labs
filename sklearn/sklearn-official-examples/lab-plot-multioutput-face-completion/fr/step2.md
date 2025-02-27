# Ajuster les estimateurs

La deuxième étape consiste à ajuster les estimateurs à plusieurs sorties aux données d'entraînement. Nous utiliserons quatre algorithmes différents : les arbres extrêmement aléatoires, les k plus proches voisins, la régression linéaire et la régression ridge. Les estimateurs prédiront la moitié inférieure des visages en fonction de la moitié supérieure.

```python
# Ajuster les estimateurs
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```
