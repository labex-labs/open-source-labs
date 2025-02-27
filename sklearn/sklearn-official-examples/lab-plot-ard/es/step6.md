# Ajustar los regresores

Probamos un polinomio de grado 10 para potencialmente sobreajustar, aunque los modelos lineales bayesianos regularizan el tamaño de los coeficientes del polinomio. Dado que `fit_intercept=True` por defecto para ARDRegression y BayesianRidge, entonces PolynomialFeatures no debe introducir una característica de sesgo adicional. Al establecer `return_std=True`, los regresores bayesianos devuelven la desviación estándar de la distribución posterior para los parámetros del modelo.

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
