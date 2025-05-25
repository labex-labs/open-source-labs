# Plotando Valores de AIC e BIC

Finalmente, plotaremos os valores de AIC e BIC para os diferentes valores de alfa. As linhas verticais no gráfico correspondem ao alfa escolhido para cada critério. O alfa selecionado corresponde ao mínimo do critério AIC ou BIC.

```python
ax = results.plot()
ax.vlines(
    alpha_aic,
    results["AIC criterion"].min(),
    results["AIC criterion"].max(),
    label="alpha: estimativa AIC",
    linestyles="--",
    color="tab:blue",
)
ax.vlines(
    alpha_bic,
    results["BIC criterion"].min(),
    results["BIC criterion"].max(),
    label="alpha: estimativa BIC",
    linestyle="--",
    color="tab:orange",
)
ax.set_xlabel(r"$\alpha$")
ax.set_ylabel("critério")
ax.set_xscale("log")
ax.legend()
_ = ax.set_title(
    f"Critério de informação para seleção de modelo (tempo de treinamento {fit_time:.2f}s)"
)
```
