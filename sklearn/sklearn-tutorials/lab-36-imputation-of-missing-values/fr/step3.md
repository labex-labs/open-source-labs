# Imputation de caractéristiques multivariées à l'aide d'IterativeImputer

La classe `IterativeImputer` est une approche plus avancée pour imputer les valeurs manquantes. Elle modélise chaque caractéristique avec des valeurs manquantes comme une fonction des autres caractéristiques et utilise cette estimation pour l'imputation. Elle apprend de manière itérative les relations entre les caractéristiques et impute les valeurs manquantes sur la base de ces relations.

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
