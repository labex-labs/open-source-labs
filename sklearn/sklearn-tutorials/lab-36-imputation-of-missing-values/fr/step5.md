# Conserver le nombre de caractéristiques constant

Par défaut, les imputeurs de scikit-learn éliminent les colonnes ne contenant que des valeurs manquantes. Cependant, dans certains cas, il est nécessaire de conserver les caractéristiques vides pour maintenir la forme des données. Nous pouvons le faire en définissant le paramètre `keep_empty_features` sur True.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
