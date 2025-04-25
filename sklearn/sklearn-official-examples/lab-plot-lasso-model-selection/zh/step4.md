# 存储结果并检查最优 alpha

我们将存储在 `fit` 过程中使用的每个 alpha 值的 AIC 指标。然后，我们将使用 BIC 准则进行相同的分析。最后，我们将检查哪个 `alpha` 值会导致最小的 AIC 和 BIC。

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
