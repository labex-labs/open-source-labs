# Ajuster les régresseurs

Nous essayons un polynôme de degré 10 pour risquer de surajuster, bien que les modèles linéaires bayésiens régularisent la taille des coefficients du polynôme. Comme `fit_intercept=True` par défaut pour ARDRegression et BayesianRidge, alors PolynomialFeatures ne devrait pas introduire une fonction de biais supplémentaire. En définissant `return_std=True`, les régresseurs bayésiens renvoient l'écart-type de la distribution postérieure pour les paramètres du modèle.

```python
ard_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    ARDRegression(),
).fit(X, y)
brr_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    BayesianRidge(),
).fit(X, y)

y_ard, y_ard_std = ard_poly.predict(X_plot, return_std=True)
y_brr, y_brr_std = brr_poly.predict(X_plot, return_std=True)
```
