# Exibir as Fronteiras de Decisão no Gráfico de Dispersão

Exibiremos as fronteiras de decisão no gráfico de dispersão usando a função `DecisionBoundaryDisplay` da biblioteca scikit-learn.

```python
_, ax = plt.subplots(figsize=(4, 3))
DecisionBoundaryDisplay.from_estimator(
    logreg,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
    xlabel="Comprimento da sépala",
    ylabel="Largura da sépala",
    eps=0.5,
)

# Plotar também os pontos de treino
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors="k", cmap=plt.cm.Paired)

plt.xticks(())
plt.yticks(())

plt.show()
```
