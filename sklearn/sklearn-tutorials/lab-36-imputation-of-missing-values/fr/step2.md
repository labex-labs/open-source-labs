# Imputation de caractéristiques univariées à l'aide de SimpleImputer

La classe `SimpleImputer` fournit des stratégies de base pour imputer les valeurs manquantes d'une manière univariée. Nous pouvons choisir parmi différentes stratégies, telles que remplacer les valeurs manquantes par une valeur constante ou utiliser la moyenne, la médiane ou la valeur la plus fréquente de chaque colonne pour imputer les valeurs manquantes.

Commencons par considérer la stratégie de moyenne. Nous allons créer une instance de `SimpleImputer` et l'ajuster sur nos données pour apprendre la stratégie d'imputation. Ensuite, nous pouvons utiliser la méthode `transform` pour imputer les valeurs manquantes en fonction de la stratégie apprise.

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
