# Almacenar resultados y comprobar el alfa óptimo

Almacenaremos la métrica AIC para cada valor de alfa utilizado durante `fit`. Luego realizaremos el mismo análisis utilizando el criterio BIC. Finalmente, comprobaremos qué valor de `alfa` conduce al AIC y BIC mínimos.

```python
results = pd.DataFrame(
    {
        "alphas": lasso_lars_ic[-1].alphas_,
        "AIC criterion": lasso_lars_ic[-1].criterion_,
    }
).set_index("alphas")
alpha_aic = lasso_lars_ic[-1].alpha_

lasso_lars_ic.set_params(lassolarsic__criterion="bic").fit(X, y)
results["BIC criterion"] = lasso_lars_ic[-1].criterion_
alpha_bic = lasso_lars_ic[-1].alpha_

def highlight_min(x):
    x_min = x.min()
    return ["font-weight: bold" if v == x_min else "" for v in x]

results.style.apply(highlight_min)
```
