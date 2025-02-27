# Evaluar los coeficientes del modelo lineal con validación cruzada

Los coeficientes del modelo lineal muestran que la mayor parte del peso está en la característica en el índice de columna 0, que es la característica informativa. Ejecute el siguiente código para evaluar los coeficientes del modelo lineal con validación cruzada:

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```
