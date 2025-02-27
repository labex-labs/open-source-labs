# Evaluar los coeficientes del modelo lineal sin validación cruzada

El modelo Ridge se sobreajusta porque asigna más peso a la característica de cardinalidad extremadamente alta en relación con la característica informativa. Ejecute el siguiente código para evaluar los coeficientes del modelo lineal sin validación cruzada:

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
