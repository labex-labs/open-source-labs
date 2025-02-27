# Сохранение результатов и проверка оптимального alpha

Мы сохраним метрику AIC для каждого значения alpha, используемого при вызове `fit`. Затем мы проведем аналогичный анализ с использованием критерия BIC. Наконец, мы проверим, какое значение `alpha` приводит к минимальному AIC и BIC.

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
