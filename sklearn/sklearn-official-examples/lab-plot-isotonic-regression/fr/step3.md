# Ajuster les modèles de régression isotone et linéaire

Nous allons maintenant ajuster les modèles de régression isotone et linéaire aux données générées.

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x doit être 2D pour LinearRegression
```
