# Traçage des valeurs AIC et BIC

Enfin, nous allons tracer les valeurs AIC et BIC pour les différentes valeurs d'alpha. Les lignes verticales dans le tracé correspondent à l'alpha choisi pour chaque critère. L'alpha sélectionné correspond au minimum du critère AIC ou BIC.

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
