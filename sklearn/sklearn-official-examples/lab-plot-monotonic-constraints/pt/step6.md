# Utilizando Nomes de Características para Especificar Restrições Monótonas

Se os dados de treino tiverem nomes de características, é possível especificar as restrições monótonas passando um dicionário. Agora demonstraremos isso usando os mesmos dados e especificando as restrições usando os nomes das características.

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
