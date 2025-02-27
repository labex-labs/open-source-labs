# Graficar el criterio AIC y BIC

Graficaremos el criterio AIC y BIC y el parámetro de regularización seleccionado posteriormente.

```python
plt.plot(aic_criterion, color="tab:blue", marker="o", label="Criterio AIC")
plt.plot(bic_criterion, color="tab:orange", marker="o", label="Criterio BIC")
plt.vlines(
    index_alpha_path_bic,
    aic_criterion.min(),
    aic_criterion.max(),
    color="black",
    linestyle="--",
    label="Alpha seleccionado",
)
plt.legend()
plt.ylabel("Criterio de información")
plt.xlabel("Secuencia del modelo Lasso")
_ = plt.title("Selección del modelo Lasso a través de AIC y BIC")
```
