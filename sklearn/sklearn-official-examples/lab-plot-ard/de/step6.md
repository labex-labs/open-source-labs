# Die Regressoren anpassen

Wir versuchen ein Polynom vom Grad 10, um möglicherweise zu überanpassen, obwohl die bayes'schen linearen Modelle die Größe der Polynomkoeffizienten regulieren. Da `fit_intercept=True` standardmäßig für ARDRegression und BayesianRidge gesetzt ist, sollte PolynomialFeatures keine zusätzliche Bias-Feature einführen. Indem `return_std=True` gesetzt wird, geben die bayes'schen Regressoren die Standardabweichung der posterioren Verteilung für die Modellparameter zurück.

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
