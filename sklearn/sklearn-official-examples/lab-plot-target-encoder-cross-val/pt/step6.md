# Avaliar os Coeficientes do Modelo Linear com Validação Cruzada

Os coeficientes do modelo linear demonstram que a maior parte do peso está na característica na coluna de índice 0, que é a característica informativa. Execute o código a seguir para avaliar os coeficientes do modelo linear com validação cruzada:

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```
