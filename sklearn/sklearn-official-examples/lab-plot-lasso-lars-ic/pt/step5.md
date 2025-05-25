# Plotar os Critérios AIC e BIC

Vamos plotar os critérios AIC e BIC e o parâmetro de regularização selecionado subsequente.

```python
plt.plot(aic_criterion, color="tab:blue", marker="o", label="Critério AIC")
plt.plot(bic_criterion, color="tab:orange", marker="o", label="Critério BIC")
plt.vlines(
    index_alpha_path_bic,
    aic_criterion.min(),
    aic_criterion.max(),
    color="black",
    linestyle="--",
    label="Alfa Selecionado",
)
plt.legend()
plt.ylabel("Critério de Informação")
plt.xlabel("Sequência do modelo Lasso")
_ = plt.title("Seleção do modelo Lasso via AIC e BIC")
```
