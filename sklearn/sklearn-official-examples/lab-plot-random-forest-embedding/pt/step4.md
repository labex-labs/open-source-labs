# Visualizar o Resultado Após Redução de Dimensionalidade usando Truncated SVD

Neste passo, visualizaremos o resultado após a redução de dimensionalidade usando Truncated SVD.

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
