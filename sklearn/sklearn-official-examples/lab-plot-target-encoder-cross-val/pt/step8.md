# Avaliar os Coeficientes do Modelo Linear sem Validação Cruzada

O modelo Ridge apresenta sobreajuste porque atribui mais peso à característica de alta cardinalidade extremamente alta em relação à característica informativa. Execute o código a seguir para avaliar os coeficientes do modelo linear sem validação cruzada:

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
