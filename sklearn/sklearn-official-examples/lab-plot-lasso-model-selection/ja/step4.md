# 結果の保存と最適な alpha の確認

`fit` 中に使用された各 alpha の値に対する AIC 指標を保存します。次に、BIC 基準を使用して同じ分析を行います。最後に、どの `alpha` の値が最小の AIC と BIC につながるかを確認します。

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
