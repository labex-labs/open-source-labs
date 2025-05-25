# 결과 저장 및 최적 alpha 확인

`fit` 과정에서 사용된 각 alpha 값에 대한 AIC 지표를 저장합니다. 그런 다음 BIC 기준을 사용하여 동일한 분석을 수행합니다. 마지막으로 AIC 와 BIC 가 최소가 되는 alpha 값을 확인합니다.

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
