# Utiliser les noms de caractéristiques pour spécifier les contraintes monotones

Si les données d'entraînement ont des noms de caractéristiques, il est possible de spécifier les contraintes monotones en passant un dictionnaire. Nous allons maintenant le démontrer en utilisant les mêmes données et en spécifiant les contraintes à l'aide des noms de caractéristiques.

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
