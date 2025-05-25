# Prever dados de modelos estimados

Preveremos os dados do modelo linear e do regressor RANSAC e compararemos os seus resultados.

```python
# Prever dados dos modelos estimados
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
