# Armazenando Resultados e Verificando Alfa Ótimo

Armazenaremos a métrica AIC para cada valor de alfa usado durante o `fit`. Em seguida, realizaremos a mesma análise usando o critério BIC. Finalmente, verificaremos qual valor de `alpha` leva ao AIC e BIC mínimos.

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
