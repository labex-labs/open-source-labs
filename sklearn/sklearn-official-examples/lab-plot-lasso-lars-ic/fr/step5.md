# Tracer le critère AIC et BIC

Nous allons tracer le critère AIC et BIC et le paramètre de régularisation sélectionné ensuite.

```python
plt.plot(aic_criterion, color="tab:blue", marker="o", label="Critère AIC")
plt.plot(bic_criterion, color="tab:orange", marker="o", label="Critère BIC")
plt.vlines(
    index_alpha_path_bic,
    aic_criterion.min(),
    aic_criterion.max(),
    color="black",
    linestyle="--",
    label="Alpha sélectionné",
)
plt.legend()
plt.ylabel("Critère d'information")
plt.xlabel("Séquence du modèle Lasso")
_ = plt.title("Sélection du modèle Lasso via AIC et BIC")
```
