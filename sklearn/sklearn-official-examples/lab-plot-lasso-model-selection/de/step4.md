# Speichern von Ergebnissen und Prüfen des optimalen Alpha

Wir werden die AIC-Metrik für jeden Wert von Alpha, der während `fit` verwendet wird, speichern. Anschließend werden wir die gleiche Analyse mit dem BIC-Kriterium durchführen. Schließlich werden wir überprüfen, welcher Wert von `alpha` zu dem minimalen AIC und BIC führt.

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
