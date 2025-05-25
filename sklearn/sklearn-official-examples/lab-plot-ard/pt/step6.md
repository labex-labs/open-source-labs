# Ajustar os Regressores

Experimentamos um polinómio de grau 10 para potencialmente sobreajustar, embora os modelos lineares bayesianos regularizem o tamanho dos coeficientes polinomiais. Como `fit_intercept=True` por defeito para ARDRegression e BayesianRidge, então PolynomialFeatures não deve introduzir um recurso de viés adicional. Ao definir `return_std=True`, os regressores bayesianos retornam o desvio padrão da distribuição posterior para os parâmetros do modelo.

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
