# Plotar Dados Brutos

Plotamos os dados brutos para visualizar os círculos e as etiquetas.

```python
plt.figure(figsize=(4, 4))
plt.scatter(
    X[labels == outer, 0],
    X[labels == outer, 1],
    color="navy",
    marker="s",
    lw=0,
    label="externo rotulado",
    s=10,
)
plt.scatter(
    X[labels == inner, 0],
    X[labels == inner, 1],
    color="c",
    marker="s",
    lw=0,
    label="interno rotulado",
    s=10,
)
plt.scatter(
    X[labels == -1, 0],
    X[labels == -1, 1],
    color="darkorange",
    marker=".",
    label="não rotulado",
)
plt.legend(scatterpoints=1, shadow=False, loc="center")
_ = plt.title("Dados brutos (2 classes=externo e interno)")
```
