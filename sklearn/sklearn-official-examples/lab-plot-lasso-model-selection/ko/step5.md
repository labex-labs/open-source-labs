# AIC 및 BIC 값 플롯

마지막으로, 서로 다른 alpha 값에 대한 AIC 및 BIC 값을 플롯합니다. 플롯의 수직선은 각 기준에 대해 선택된 alpha 값에 해당합니다. 선택된 alpha 는 AIC 또는 BIC 기준의 최소값에 해당합니다.

```python
ax = results.plot()
ax.vlines(
    alpha_aic,
    results["AIC criterion"].min(),
    results["AIC criterion"].max(),
    label="alpha: AIC estimate",
    linestyles="--",
    color="tab:blue",
)
ax.vlines(
    alpha_bic,
    results["BIC criterion"].min(),
    results["BIC criterion"].max(),
    label="alpha: BIC estimate",
    linestyle="--",
    color="tab:orange",
)
ax.set_xlabel(r"$\alpha$")
ax.set_ylabel("criterion")
ax.set_xscale("log")
ax.legend()
_ = ax.set_title(
    f"Information-criterion for model selection (training time {fit_time:.2f}s)"
)
```
