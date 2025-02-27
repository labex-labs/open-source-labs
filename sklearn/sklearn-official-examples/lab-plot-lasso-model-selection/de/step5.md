# Plotten von AIC- und BIC-Werten

Schließlich werden wir die AIC- und BIC-Werte für die verschiedenen Alpha-Werte plotten. Die vertikalen Linien im Plot entsprechen dem für jedes Kriterium gewählten Alpha. Das ausgewählte Alpha entspricht dem Minimum des AIC- oder BIC-Kriteriums.

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
